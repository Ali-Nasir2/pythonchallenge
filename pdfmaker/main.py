from PIL import Image
import os

def images_to_pdf(image_folder, output_pdf):
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('png', 'jpg', 'jpeg'))]
    
    image_files.sort()
    
    print(f"Found image files: {image_files}")
    
    images = [Image.open(os.path.join(image_folder, file)).convert('RGB') for file in image_files]
    
    if images:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"PDF saved successfully as {output_pdf}")
    else:
        print("No images found to convert.")


image_folder = # Path to the folder containing images
output_pdf = 'output.pdf'
images_to_pdf(image_folder, output_pdf)
