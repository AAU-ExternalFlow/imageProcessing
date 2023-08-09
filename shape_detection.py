import os
from PIL import Image

def image_rotate(image_path, degrees):

    image=Image.open(image_path)
    rotated_image = image.rotate(degrees, expand=True)
    rotated_image.save("uploads/blurred_image.png")
    rotated_image.show()
    return image_path_rotated

# def image_canny(image_path, canny_value):

#     return image_path_canny


# def show_image(image_path):
#     pass