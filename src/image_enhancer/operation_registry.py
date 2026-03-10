from image_enhancer.basic_image_ops import resize_image, to_grayscale, normalize_image, adjust_gamma, contrast_stretch

OPERATION_REGISTRY = {
    "resize_image": resize_image,
    "to_grayscale": to_grayscale,
    "adjust_gamma": adjust_gamma,
    "normalize": normalize_image,
    "contrast_stretch": contrast_stretch
}