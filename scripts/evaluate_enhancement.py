import cv2 as cv
import numpy as np
from skimage.metrics import structural_similarity


def create_degraded_image(img):
    degraded = img.astype(np.float32) * 0.45 - 20
    degraded = np.clip(degraded, 0, 255)

    return degraded.astype(np.uint8)


clean = cv.imread("src/image_enhancer/logi.jpg")

if clean is None:
    raise ValueError("Could not load clean image")

degraded = create_degraded_image(clean)
cv.imwrite("degraded.jpg", degraded)

clean_gray = cv.cvtColor(clean, cv.COLOR_BGR2GRAY)
degraded_gray = cv.cvtColor(degraded, cv.COLOR_BGR2GRAY)

degraded_ssim = structural_similarity(
    clean_gray,
    degraded_gray,
    data_range=255
)

print(f"Degraded SSIM: {degraded_ssim:.4f}")