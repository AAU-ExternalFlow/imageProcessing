import os
import cv2
from PIL import Image

def gaussian_blur(image, value):
    return cv2.GaussianBlur(image, (value, value), 0)

def canny(image, min_value, max_value):
    return cv2.Canny(image, min_value, max_value)

# def bitwise_not(image):
#     return cv2.bitwise_not(image)

def image_rotate(image_path, degrees):
    # # Get a list of files in the directory
    # files = os.listdir(image_path)

    # # Filter the list to include only image files (you can modify the condition as per your file extensions)
    # image_files = [file for file in files if file.endswith((".png", ".jpg", ".jpeg"))]

    # if not image_files:
    #     print("No image files found in the directory.")
    #     return

    # # Sort the image files based on their creation time (most recent first)
    # sorted_files = sorted(image_files, key=lambda file: os.path.getmtime(os.path.join(image_path, file)), reverse=True)

    # # Select the newest image file
    # newest_image_path = os.path.join(image_path, sorted_files[0])

    # Rotate the newest image
    # image = Image.open(newest_image_path)
    image=Image.open(image_path)
    rotated_image = image.rotate(degrees, expand=True)
    rotated_image.save("uploads/blurred_image.png")
    rotated_image.show()
#     return image_path_rotated


# def image_canny(image_path, canny_value):

#     return image_path_canny


# def show_image(image_path):
#     pass