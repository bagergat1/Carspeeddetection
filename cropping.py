from PIL import Image
def crop_image(input_image_path, output_image_path, crop_box):

    img = Image.open(input_image_path)
    

    cropped_img = img.crop(crop_box)
    

    cropped_img.save(output_image_path)