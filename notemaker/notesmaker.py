import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Set the Tesseract executable path if it's not in your PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf_page(page):
    pix = page.get_pixmap()
    img = Image.open(io.BytesIO(pix.tobytes()))
    page_text = pytesseract.image_to_string(img)
    return page_text

def summarize_text(text, num_sentences=5):
    sentences = sent_tokenize(text, language='english')
    stop_words = set(stopwords.words('english'))
    word_frequencies = Counter(word.lower() for word in text.split() if word.lower() not in stop_words)
    sentence_scores = {sentence: sum(word_frequencies[word.lower()] for word in sentence.split()) for sentence in sentences}
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return summarized_sentences

def format_notes_as_markdown(notes):
    markdown_notes = "# Summary Notes\n\n"
    for i, note in enumerate(notes, 1):
        markdown_notes += f"## Note {i}\n\n{note}\n\n"
    return markdown_notes

def save_notes_to_file(notes, file_path):
    with open(file_path, 'w') as file:
        file.write(notes)
    print(f"Notes saved to {file_path}")

pdf_path = "yourpdflocation"
start_page = 0  # Specify the start page (0-indexed)
end_page = 37   # Specify the end page (0-indexed, exclusive)

try:
    doc = fitz.open(pdf_path)
    all_notes = []
    for page_num in range(start_page, end_page):
        page = doc.load_page(page_num)
        page_text = extract_text_from_pdf_page(page)
        print(f"Extracted text from page {page_num}:")
        print(page_text[:500])  # Print the first 500 characters of the extracted text for debugging
        summarized_sentences = summarize_text(page_text)
        page_notes = format_notes_as_markdown(summarized_sentences)
        all_notes.append(f"# Page {page_num + 1}\n\n{page_notes}")
    
    all_notes_markdown = "\n".join(all_notes)
    save_notes_to_file(all_notes_markdown, "notes.txt")
except ValueError as e:
    print(e)
