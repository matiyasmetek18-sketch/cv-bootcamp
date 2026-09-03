# 1. Import your classical load_image function
from image_enhancer.basic_image_ops import load_image, display_image

# 2. Import your real deep model functions
from image_enhancer.deep_models.dncnn import load_dncnn_model, denoise_image

# 3. Load your test image
img = load_image("src/image_enhancer/ex_photo.jpg")

# 4. Load the pretrained DnCNN model
model = load_dncnn_model()

# 5. Pass the image through the real model
out = denoise_image(model, img)

# 6. Display the output
display_image(out)
