# 1. Import your classical load_image function
from image_enhancer.basic_image_ops import load_image, display_image

# 2. Import your placeholder deep model function
from image_enhancer.deep_models.dncnn import denoise_image

# 3. Load your test image
img = load_image("src/image_enhancer/ex_photo.jpg")

# 4. Pass it through the placeholder model
out = denoise_image(img)

# 5. Display or save the output
display_image(out)
