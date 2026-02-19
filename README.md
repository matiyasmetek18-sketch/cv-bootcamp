# Computer Vision bootcamp - image operations toolkit
## Day 1 - Project setup and functionality scafolding 
- Created the project structure and initialized the 'basic_image_ops.py' module
- Added Scaffolds for core image operations:
    - Load image
    - image_info
    - to_grayscale
    - save_image
    - display_image
    - resize_image
    - crop_image
    - rotate_image
    - flip_image
    - batch_process folder
- Focused on writing clean docstrings and planning for API surface
- Reflection
  - Today was not implementation but just scaffolding
  - I was excited to finish day 1 and go to day 2. I feel like I am more relevant material than in school
  - I followed this structure as it was the one suggested by AI
## Day 2 - Core Image Operations Implemented 
- Implemented and validated
  - load_image
  - image_info
  - to-grayscale
  - save_image
  - display_image
- Learned:
  - BGR vs RGB color spaces
  - Using matplotlib for visualization
  - Consistent input validation patterns
  - Clean return-only utility design
- Reflection
  - This day was straight-forward, just the using matplot lib was challenging for me. I was able to find the right answer by looking googling it and seeing what other wrote while checking this answer using co-pilot
  - I learned some functions of matplotlib and how to use it for image display and to turn the axis off
  - I understand how to display and image and close the image page as well
## Day 3 - Geometric Transformations
- Implemented:
  - resize_image
  - crop_image
  - rotate_image
  - flip_image
  - batch_process_folder (first automation pipeline)
- Learned:
  - Spatial slicing and coordinate validation
  - Image geometry (width, height, center)
  - Rotation matrices and affine transforms
  - Flip codes and orientation handling
  - How to design a reusable batch-processing function using:
    - path handling
    - flexible *args for operations
    - clean separation of load -> transform -> save
    - returning structured results
- Reflection:
  - I learend how to use openCV to re-size an image
  - I learned how to find the center of an image using the width and height of the image.
  - Finding the center was the hardest part for this day
  - I was very much challenged with how to rotate the image. I had to be corrected with co-pilot as it guided me (without it providing me the code) on how to think about in solving it.
  - Building batch_process_folder was by far the hardest I have done so far. It taught me to think systematically, look for solutions online and use AI (copilot) to guide me in solving the issue. This function combined file iteration, path management, flexible operations, and clean output handling. This was the first time my toolkit felt like an actual tool .
# Example batch resize images to (200, 150)
batch_process_folder(
    folder_path = "input_images"
    output_path = "output_images"
    operation = resize_image
    *args = (200, 150)
)
# Example flip image by a direction of 1 - horizontal flip 
batch_process_folder(
folder_path = "input_images"
output_path = "output_images"
operation = flip_image
*args = 1
)

