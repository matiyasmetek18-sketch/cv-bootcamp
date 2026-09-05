import numpy as np
from image_enhancer.basic_image_ops import resize_image, adjust_gamma, adjust_brightness

def test_resize_image():
    img = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    new_img = resize_image(img, 200, 200)
    
    heigth, width = new_img.shape[:2]
    
    assert heigth == 200
    assert width == 200
    
def test_adjust_gamma():
    img = np.zeros((350, 700, 3), dtype = np.uint8)
    new_img = adjust_gamma(img, 0.7)
    
    assert np.array_equal(img, new_img)
    
def test_adjust_brightness_normal():
    img = np.full((2, 2), 100, dtype=np.uint8)
    new_img = adjust_brightness(img, 20)

    assert np.all(new_img == 120)


def test_adjust_brightness_upper_clip():
    img = np.full((2, 2), 250, dtype=np.uint8)
    new_img = adjust_brightness(img, 20)

    assert np.all(new_img == 255)


def test_adjust_brightness_lower_clip():
    img = np.full((2, 2), 10, dtype=np.uint8)
    new_img = adjust_brightness(img, -20)

    assert np.all(new_img == 0)
