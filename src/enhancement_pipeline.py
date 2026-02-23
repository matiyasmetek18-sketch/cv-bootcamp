from basic_image_ops import *

def enhance_image (img, config):
    img_copy = img.copy()
    
    bright_value = config["brightness"]
    contrast_value = config["contrast"]
    norm_value = config["normalize"]
    stretch_value = config["stretch"]
    plot_hist = config["plot_histogram"]
    
    if plot_hist:
        if is_gray(img_copy):
            hist = compute_histogram(img_copy)
            plot_histogram(hist)
        else:
            hist = compute_color_histogram(img_copy)
            plot_color_histogram(hist)
    
    
    img_copy = adjust_brightness(img_copy, bright_value)
    
    
    img_copy = adjust_contrast(img_copy, contrast_value)
    if norm_value:
        img_copy = normalize_image(img_copy)
    if stretch_value:
        img_copy = contrast_stretch(img_copy)
    if plot_hist:
        if is_gray(img_copy):
            hist = compute_histogram(img_copy)
            plot_histogram(hist)
        else:
            hist = compute_color_histogram(img_copy)
            plot_color_histogram(hist)
        

    return img_copy


def main():
    
    #Load image
    img = load_image("/Users/matiyasdawit/Downloads/my_photo.jpg")
    
    config = {
        "brightness": 30,
        "contrast": 1.2,
        "normalize": False,
        "stretch": True,
        "plot_histogram": True
    }
    
    new_image = enhance_image(img, config)
    
    save_image(new_image, "enhanced_new_photo.jpg")
    
    image_info(new_image)