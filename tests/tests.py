import numpy as np
from image_enhancer.basic_image_ops import resize_image, adjust_gamma

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