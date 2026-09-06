import cv2 as cv
import numpy as np


def create_degraded_image(img):
    # Reduce contrast and brightness
    degraded = img.astype(np.float32) * 0.45 - 20

    # Keep valid image intensity range
    degraded = np.clip(degraded, 0, 255)

    return degraded.astype(np.uint8)