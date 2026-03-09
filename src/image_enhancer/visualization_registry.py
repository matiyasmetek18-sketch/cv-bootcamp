from basic_image_ops import (compute_histogram, compute_color_histogram, plot_histogram, 
                             plot_color_histogram, plot_before_after, hist_before_after, clahe_eqlz_before_after)

VISUALIZATION_REGISTRY = {
    "compute_histogram": compute_histogram,
    "compute_color_histogram": compute_color_histogram,
    "plot_histogram": plot_histogram,
    "plot_color_histogram": plot_color_histogram,
    "plot_before_after": plot_before_after,
    "hist_before_after": hist_before_after,
    "clahe_eqlz_before_after": clahe_eqlz_before_after,
}