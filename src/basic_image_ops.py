import numpy as np
import cv2 as cv
import matplotlib as plt 


def image_info(img):
  '''
  This function takes an image array and return basic information
  like image shape, min/max pix values, dtype, height and width, 
  and color format (BGR)

  Args: img is the image array 

  '''
  
  if img is not None:
    
    
    # the below will extract heigth, width, channels data from the image
    height, width, channel = img.shape
    
    print(f'The height, width and channel values respectively are: {img.shape}')
    
    #below is the data type of the array 
    print(f'The dtype of the image array is: {img.dtype}')
    
    #min and max pixel values are below
    min_blue = img[..., 0].min()
    min_green = img[..., 1].min()
    min_red = img[..., 2].min()
    
    print(f'Minimum pixel values in (B G R) is:  {min_blue}, {min_green}, {min_red}')
  
    max_blue = img[..., 0].max()
    max_green = img[..., 1].max()
    max_red = img[..., 2].max()
    
    print(f'Maximum pixel values in (B G R) is:  {max_blue}, {max_green}, {max_red}')
  
  

def load_image(img_path):
  '''
  This function takes an file path and loads an image from disk 
  It returns a NumPy array 
  It raises a value error if file does not exist
  

  Args: img_path is the image file on disk 
  '''
  img = cv.imread(img_path)
  
  if img is None:
    raise ValueError('The image is empty')
  
  return img

def to_grayscale(img):
  '''
  This function takes an image array and changes it to the 
  graysscale
  
  Args: img is the image array
  '''
  
  if img is None:
    raise ValueError('This is not a valid image')
  
  if len(img.size) == 2:
    raise Exception('This image is already in grayscale')
  
  gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  
  return gray_img


def save_image(img, img_path):
  '''
  This function will take a processed image and take it back to the 
  disk. This is important for dataset preprocessing, exporting augmented images,
  saving intermediate results, debugging transformations and batch processing


  Args: img is the image array 
        img_path is the path 
  '''
  if img is None:
    raise ValueError('This is not a valid image')
  
  return cv.imwrite(img_path, img)

def display_image(img):
  '''
  This function will display the image array to the screen
  using the matplotlib libaray of python  

  Args: img is the image array 
  '''
  plt.imshow(img)
  plt.waitforbuttonpress()
  plt.close('all')
  pass

def resize_image(img, img_width, img_height):
  '''
  This function will take the image array and resize it to
  the new dimensions

  Args: img is the iamge array 
        img_width is the new image width
        img_height is the new image height
  '''
  pass 

def crop_image(img, x_start, y_start, width, height):
  '''
  This function extracts a rectangular region of interest (ROI)
  from the image
  Cropping is commonly used in preprocessing, object detection pipelines,
  and isolating specific regions for further analysis
  
  :param img: this is the image array 
  :param x_start: x-coordinate of the top left corner of the crop
  :param y_end: the y-coordinate of the top-left corner of the top
  :param width: width of the cropped region
  :param height: height of the cropped region
  '''
  pass

def rotate_image(img, angle):
  '''
  This funciton rotates the image by a specific angle
  
  Rotation is useful for data augmentation, alignment, and geomertric
  transformations in computer vision tasks
  
  :param img: is the image array 
  :param angle: Rotation angles in degrees (postive = counterclockwise)
  '''
  pass

def flip_image(img, direction):
  '''
  Flips the image horizontally, vertically or both
  
  Flipping is usually used for data augmentation and creating
  oreintation-invariant training samples
  
  :param img: is the image array
  :param direction: is the direction which the image will face
  '''
  pass

def batch_process_folder(folder_path, output_path, operation):
  '''
  Applies a specified image operation to every shape in a folder
  
  Batch processing is essential for automation, preprocessing pipelines,
  and preparing large data sets for machine learning workflows 
  
  :param folder_path: Description
  :param output_path: Description
  :param operation: Description
  '''
  pass
  

