from basic_image_ops import (resize_image, to_grayscale, normalize_image, adjust_gamma, contrast_stretch,
                             compute_histogram, compute_color_histogram, plot_before_after, 
                             clahe_eqlz_before_after, hist_before_after)

OPERATION_REGISTRY = {
    "resize_image": resize_image,
    "to_grayscale": to_grayscale,
    "normalize": normalize_image,
    "adjust_gamma": adjust_gamma,
    "contrast_stretch": contrast_stretch,
    "compute_histogram": compute_histogram,
    "compute_color_histogram": compute_color_histogram,
    "clahe": clahe_eqlz_before_after,
    "hist_plot": hist_before_after
}