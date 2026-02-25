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
    white_balance_value = config["white_balance"]
    
    
    histogram_equalization(img_copy)
    
    if plot_hist:
        if is_gray(img_copy):
            hist = compute_histogram(img_copy)
            plot_histogram(hist)
        else:
            hist_r, hist_g, hist_b = compute_color_histogram(img_copy)
            plot_color_histogram(hist_r, hist_g, hist_b)
    
    
    if clahe_value:
        img_copy = histogram_equalization_clache_grayscale(img_copy)
    
    if equalize_value:
        img_copy = histogram_equalization(img_copy)
    
    if white_balance_value:
        img_copy = gray_world(img_copy)
        
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
        "white_balance": False,
    }
    
    new_image = enhance_image(img, config)
    
    save_image(new_image, "enhanced_new_photo.jpg")
    
    image_info(new_image)
    

def histogram_equalization(img):
    '''
    This function applies histogram equalization to the whole image
    
    :param img: image to be proccessed
    '''
    
    new_img = img.copy()
    org_img = img.copy()
    
    if not is_gray(new_img):
        new_img = to_grayscale(img)
    
    gray_img = new_img.copy()
    
    gray_img = gray_img.astype('uint8')
    gray_img = cv.equalizeHist(gray_img)
    
    return gray_img

def histogram_equalization_clache_grayscale(img, clip_limit = 10, grid_size=(8, 8)):
    '''
    Applies CACHE (Contrast Limited Adaptive Histogram Equalization) to an grayscale image
    or just a single channel
    
    
    :param img: uint8 numpy array of shape (heigth, width)
    :param clip_limit: maximum allowed value for each histogram bin
    :param grid_size: Tuple (n_rows, n_cols) indicating the number of regions the image is divided
    into
    '''
    
    new_img = img.copy()
    if not is_gray(img):
        new_img = to_grayscale(new_img)
    
    gray_img = new_img.copy()
    
    clahe = cv.createCLAHE(clip_limit, grid_size)
    cl1 = clahe.apply(gray_img)
    
    cv.imwrite('clahe_2.jpg', cl1)
    
    return cl1

def adjust_gamma(img, gamma):
    '''
    This fucntion will apply gamma correction for displaying images on the screen correctly 
    This will help to linearize the percieved brightness
    
    :param img: is the image to be proccessed 
    :param gamma: the scale in which the image brightness will be adjusted 
    '''
    if gamma <= 0:
        raise ValueError('Invalid gamma value')
    new_img = img.copy()
    
    gamma_corrected = np.array(255 * (new_img.astype(float) / 255.0) ** gamma, dtype = 'uint8')
    
    return gamma_corrected
        

def gray_world(img):
    '''
    This function will white balance the image using the gray-world algorithm
    
    :param img: image to be processed
    '''
    new_img = img.copy()
    img_LAB = cv.cvtColor(new_img, cv.COLOR_BGR2LAB)
    avg_a = np.average(img_LAB[:, :, 1])
    avg_b = np.average(img_LAB[:, :, 2])
    img_LAB[:, :, 1] = img_LAB[:, :, 1] - ((avg_a - 128) * (img_LAB[:, :, 0] / 255.0) * 1.2)
    img_LAB[:, :, 2] = img_LAB[:, :, 2] - ((avg_b - 128) * (img_LAB[:, :, 0] / 255.0) * 1.2)
    
    balanced_img = cv.cvtColor(img_LAB, cv.COLOR_LAB2BGR)
    
    return balanced_img
    
if __name__ == "__main__":
    main()