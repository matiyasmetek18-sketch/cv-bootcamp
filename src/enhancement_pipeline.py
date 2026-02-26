from basic_image_ops import *
import argparse

def enhance_image (img, config):
    img_copy = img.copy()
    
    bright_value = config["brightness"]
    contrast_value = config["contrast"]
    norm_value = config["normalize"]
    stretch_value = config["stretch"]
    plot_hist = config["plot_histogram"]
    equalize_value = config["equalize"]
    clahe_value = config["clahe"]
    gamma_value = config["gamma"]
    gamma_number = config["gamma_value"]
    white_balance_value = config["white_balance"]

    
    if plot_hist:
        if is_gray(img_copy):
            hist = compute_histogram(img_copy)
            plot_histogram(hist)
        else:
            hist_r, hist_g, hist_b = compute_color_histogram(img_copy)
            plot_color_histogram(hist_r, hist_g, hist_b)
    
    
    if white_balance_value:
        img_copy = gray_world(img_copy)
        
    if gamma_value:
        img_copy = adjust_gamma(img_copy, gamma_number)
        
    
    img_copy = adjust_brightness(img_copy, bright_value)

    img_copy = adjust_contrast(img_copy, contrast_value)
        
    
    if clahe_value or equalize_value:
        img_copy = to_grayscale(img_copy)
    
    if clahe_value:
        img_copy = histogram_equalization_clahe_grayscale(img_copy)
        
    elif equalize_value:
        img_copy = histogram_equalization(img_copy)
        
    if norm_value:
        img_copy = normalize_image(img_copy)
    if stretch_value:
        img_copy = contrast_stretch(img_copy)
    if plot_hist:
        if is_gray(img_copy):
            hist = compute_histogram(img_copy)
            plot_histogram(hist)
        else:
            hist_r, hist_g, hist_b = compute_color_histogram(img_copy)
            plot_color_histogram(hist_r, hist_g, hist_b)
        

    return img_copy


def main():
    
    #Load image
    img = load_image("/Users/matiyasdawit/Desktop/Computer_Vision_Project/cv-bootcamp/src/ex_photo.jpg")
    
    config = {
        "brightness": 120,
        "contrast": -1.2,
        "stretch": True,
        "plot_histogram": True,
        "normalize": False,
        "equalize": True,
        "clahe": False,
        "gamma": False,
        "gamma_value": 1.2,
        "white_balance": False,
    }
    
    new_image = enhance_image(img, config)
    
    save_image(new_image, "enhanced_new_photo.jpg")
    
    image_info(new_image)
    
    
if __name__ == "__main__":
    main()