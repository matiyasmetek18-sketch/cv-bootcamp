#  Computer Vision Bootcamp — Image Operations Toolkit Organzied by copilot 
*This project was completed across multiple real days. Each “Milestone” below represents a learning phase, not a single calendar day.*
*t hello _
---

##  Milestone 1 — Project Setup & Functionality Scaffolding   
*Completed over several real days*

###  Overview   
Set up the project structure and created scaffolds for all core image‑processing functions. Focused on writing clean docstrings, planning the API surface, and establishing a professional workflow using VS Code + GitHub.

###  Features Completed 
- Created project folder structure (`src/`, `notebooks/`, `assets/`)
- Initialized `basic_image_ops.py`
- Added scaffolds for core image operations:
  - `load_image`
  - `image_info`
  - `to_grayscale`
  - `save_image`
  - `display_image`
  - `resize_image`
  - `crop_image`
  - `rotate_image`
  - `flip_image`
  - `batch_process_folder`
- Wrote clean docstrings and planned the function interfaces

###  Reflection 
- This phase focused on scaffolding, not implementation  
- I felt excited to move into real functionality afterward  
- The structure suggested by AI helped me stay organized  
- This work felt more practical and relevant than school assignments  

---

##  Milestone 2 — Core Image Operations Implemented   
*Completed over multiple real days*

###  Overview   
Implemented the actual logic for the scaffolds created earlier and validated them using test images. Focused on correctness, clarity, and error handling.

###  Features Completed 
- Implemented and validated:
  - `load_image`
  - `image_info`
  - `to_grayscale`
  - `save_image`
  - `display_image`

###  Learned 
- BGR vs RGB color spaces  
- How to use Matplotlib for image visualization  
- How to turn axes off for clean display  
- Consistent input‑validation patterns  
- Clean, return‑only utility design  

###  Reflection 
- This milestone felt straightforward  
- Matplotlib was the most challenging part, but I solved issues by Googling and checking with Copilot  
- I learned how to display and close images properly  
- I felt more confident working with OpenCV and Matplotlib  

---

##  Milestone 3 — Geometric Transformations   
*Completed across several real days*

###  Overview   
Expanded the toolkit with geometric image operations and built the first automation pipeline using batch processing. Focused on writing reusable, flexible functions.

###  Features Completed 
- Implemented:
  - `resize_image`
  - `crop_image`
  - `rotate_image`
  - `flip_image`
  - `batch_process_folder` (first automation pipeline)

###  Learned 
- Spatial slicing and coordinate validation  
- Image geometry (width, height, center)  
- Rotation matrices and affine transforms  
- Flip codes and orientation handling  
- How to design a reusable batch‑processing function using:
  - path handling  
  - flexible `*args` for operations  
  - clean separation of load → transform → save  
  - returning structured results  

###  Reflection 
- Learned how to resize images using OpenCV  
- Finding the image center was the hardest part  
- Rotation challenged me the most — Copilot guided my thinking without giving code  
- `batch_process_folder` was the hardest function so far  
  - It required systematic thinking  
  - Searching online  
  - Using AI guidance  
  - Handling paths, iteration, flexible operations, and clean output  
- This was the first time my toolkit felt like a real tool  

---

###  Example: Batch resize images to (200, 150) 

```python
batch_process_folder(
    folder_path = "input_images",
    output_path = "output_images"
    operation = resize_image
    *args = (200, 140)
```

###  Example: Flip image horizontally (direction = 1) 

```python
batch_process_folder(
    folder_path="input_images",
    output_path="output_images",
    operation=flip_image,
    *args=(1,)
)
```

---

##  Milestone 4 — Histogram Analysis Toolkit   
*Completed over several real days*

###  Overview   
Implemented a complete histogram analysis module from scratch for both grayscale and RGB images. This included computing pixel‑intensity distributions and visualizing them using Matplotlib.

###  Features Completed 
- Implemented:
  - `compute_histogram`
  - `compute_color_histogram`
  - `plot_histogram`
  - `plot_color_histogram`

###  Learned 
- How to plot grayscaled image 
- How to plot RGB images
- How to access pixel intensity values
- How to manually computer historgrams at the pixel level
- How to design modular reliable CV utilites

###  Reflection 
- This phase focused on implementation
- I felt excited to move into real analsysis   
- The structure suggested by AI helped me stay organized  
- This work felt actually felt practical and relevant than school assignments

---

##  Milestone 5 — Intesity Transformations
*Completed over several real days*

###  Overview   
Implemeneted a full suite of intensity transformations. These functions adjust pixel values directly, enabling brightness control, contrast manipulation, normalization, and contrast stretching for both grayscale and RGB images. All operations were built manually using nested loops, careful min/max scanning, and explicit clipping to maintain valid 0-255 ranges

###  Features Completed 
- Implemented:
  - `adjust_brightness`
  - `adjust_contrast`
  - `normalize_image`
  - `contrast_stretch`

###  Learned 
- How to plot manipulate pixel intensitites at the per-pixel level
- How to safely compute and use min/max values for scaling
- How to avoid divide-by-zero error in normalization
- How to design two-pass algorithms (scan -> transform)
- How to handle grayscale and RGB images consistently
- How to build reliable, modular CV utilities that mirror real engineering practice  

###  Reflection 
- This required the most intense logic so far
- It was the second most challenging part of the project so far
- It was easier since I did similar logic prior to this Milestone in Milestone 4
- I felt myself thinking more like an engineer more than a student
- The repetition across channels helped me internalize the structure 
