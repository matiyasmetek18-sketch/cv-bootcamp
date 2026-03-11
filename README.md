#  Computer Vision — Image Operations Toolkit
*This project was completed across multiple real days. Each “Milestone” below represents a learning phase, not a single calendar day.*

---

## Summary 
- A modular, config-driven image enhancment pipeline with a CLI, dynmaic operation registry, visulaization suite and full test coverage

## High level Overview 
- This project is a professional-grade image enhacement pipeline built as part of a self-directed computer vision bootcamp. It includes a dynmaic operation registry, a modular pipleine exectuor, a visulaization suite, and a fully pakcaged CLI tool. Every component was designed with real engineering practices: clean architecture, reproducible configs, test coverage and `src/` layout. 

## Features 
### Core Features
- Modular enhacmement pipeline
- Dynamic operation registry
- Visulaization registry
- Config-driven architecture
- CLI tool (enhance-image)
- Full test suite with pytest

### Enhacement Operations
- Brightness
- Contrast
- Gamma corrrection
- Normlization
- Contrast stretching
- White balance (LAB)
- Histogram equalization
- CLAHE

### Geometric Operations
- Resize
- Crop
- Rotate
- Flip

### Visualization Tools
- Before / After visualization tools
- Histogram comparison
- CLAHE vs Equalization comparison

## Project Structure 
```python
src/
  image_enhancer/
    __init__.py
    basic_image_ops.py
    cli.py
    enhancment_pipeline.py
    ex_photo.jpg
    operation_registry.py
    pipleine_executor.py
    visualization_registry.py
```

## Installation instructions
```python
git clone
cd cv-bootcamp
pip install -e .
```

## Example CLI Usage
```python
enhance-image --config configs/basic.yaml --input input.jpg --output output.jpg
```

## Example Config snipeet
```Yaml
operations:
  - resize:
    img_width: 170
    img_heigth: 170
  - to_grayscale
  - adjust_gamma:
    gamma: 0.9
```

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

##  Milestone 6 — Advanced Enahcement operations
*Completed over several real days*

###  Overview   
This milestone introduced the most advanced enhacement operations in the entire project. I implemented gamma co-relation, LAB-based white balance, and CLAHE (adaptive histogram equalization). These functions required deeper conceptual understanding and careful ordering inside the pipeline

###  Features Completed 
- Implemented:
  - `adjust_gamma`
  - `gray_world`
  - `histogram_equalization_clache_grayscale`

- Added:
  - Safe float-based gamma transformation
  - Per channel LAB chromaticity correction
  - Tile-based adaptive contrast enhacement
  - Explicit grayscale conversion before local contrast operations

###  Learned 
- How gamma affects mid-tones and percieved brightness
- Why white balance must happen before grayscale conversion
- How LAB color space separates luminance from chromaticity
- Why CLAHE avoids noise amplification compared to global equalization
- How to design mutually exclusive enhacement paths (CLAHE vs Equalization)

###  Reflection 
- This was one of the most conceptually challenging milestones
- Understanding LAB space felt like a big leap in my CV knowledge
- CLAHE made me appreciate how real imaging systems enhance low-light photos

##  Milestone 7 — Full Enahcement Pipeline Integration
*Completed over several real days*

###  Overview   
This milestone brought everything together into a single, professional-grade enahcement pipeline. I designed ```enhance_image()``` to apply operations in the correct order, handle color vs grayscale transitions, and support a flexible configuration system

###  Features Completed 
- Implemented the full enhacement pipeline:
  - White balance
  - Gamma correction
  - Brightness adjustement
  - Contrast adjustment
  - Grayscale conversion (when needed)
  - CLAHE or Histogram equalization
  - Normalization
  - Contrast stretching

- Added:
  - Before/After histogram equalization
  - Clean config-driven architecture
  - Mutually exclusive CLAHE/equalization logic
  - Intentional ordering to avoid destructive interactions

###  Learned 
- How to design a real CV pipeline with intentional ordering
- How to avoid conflicts between color and grayscale operations
- How to build a modular, readable, and maintainable enahcement engine
- How to think about image processing as a sequence of transformations, not isolated functions

###  Reflection 
- This was a smooth milestone for me, I enjoyed lookign for solutions online
- The pipeline felt like a real tool, not just a collection of functions
- I now understand how professinal CV systems structure enhacnement workflows
- This milestone made the project "portfolio-ready"

##  Milestone 8 — Visualization and comparison tools
*Completed in a day*

###  Overview   
This milestone focused on building a complete visualization suite to help me understand, debug, and communicate the effects of each enhacement operation in my pipeline. These tools are now part of the project and will also be used in the final README examples

###  Features Completed 
- Implemented:
  - Before and After Image comparision
  - Before and After Histogram comparision
  - CLAHE vs Equalization Comparison

###  Learned 
- How to design visualzation utilites that work for both grayscale and RGB images
- How to use histograms to intepret enhancement behavior
- How global equalization differs from CLAHE in practice
- How to structure Matplotlib figures cleanly using subplots, titles, and layout management
- How visualization helps validate the correctness of each enhancement step 

###  Reflection 
- This pipeline felt more "real" and more developed
- This milestone is like showing the summary of what I have worked on so far visually


