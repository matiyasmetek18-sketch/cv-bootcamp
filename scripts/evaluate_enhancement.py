import cv2 as cv
import numpy as np


def create_degraded_image(img):
    # Reduce contrast and brightness
    degraded = img.astype(np.float32) * 0.45 - 20

    # Keep valid image intensity range
    degraded = np.clip(degraded, 0, 255)

    return degraded.astype(np.uint8)


clean = cv.imread("src/image_enhancer/logi.jpg")

if clean is None:
    raise ValueError("Could not load clean image")

degraded = create_degraded_image(clean)

cv.imwrite("degraded.jpg", degraded)