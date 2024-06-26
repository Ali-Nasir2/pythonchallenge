from rembg import remove
from PIL import Image

image_path = "input_image_path"
processedImagePath = "output_image_path" 

display_image = input("Do you wanna see the final image (Y/n): ")

original_image = Image.open(image_path)
removed_image = remove(original_image)
removed_image.save(processedImagePath)
print("Background of the image has been removed successfully!")


if display_image.lower() == "y":
    Image.open(processedImagePath).show()
else:
    pass







