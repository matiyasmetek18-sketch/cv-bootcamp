import cv2 as cv


def image_info(img):
  '''
  This function takes an image array and return basic information
  like the min/max pix values, dtype and shape

  Args: img is the image array 

  '''
  pass

def load_image(img_path):
  '''
  This function takes an file path and will display it in the 
  NumPy array 

  Args: img is the image array
  '''
  pass

def to_grayscale(img):
  '''
  This function takes an image array and changes it to the 
  graysscale
  
  Args: img is the image array
  '''
  pass


def save_image(img, img_path):
  '''
  This function will save the image array the file path to 
  where it will be saved  
  This will help in debugging and reproducing results


  Args: img is the image array 
        img_path is the path 
  '''
  pass 

def display_image(img):
  '''
  This function will display the image array to a screen 
  usign Google colab friendly libraries 

  Args: img is the image array 
  '''
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

def crop_image(img, x_start, y_end, img_width, img_height):
  '''
  This function will crop the image array into the given dimensions
  
  :param img: this is the image array 
  :param x_start: Description
  :param y_end: Description
  :param img_width: Description
  :param img_height: Description
  '''
  pass

def rotate_image(img, angle):
  '''
  This funciton rotates the image with a specific angle
  This is useful for debugging and visualization
  
  :param img: is the image array 
  :param angle: is the angle which the image is tilted
  '''
  pass

def flip_image(img, direction):
  '''
  This functions will flip the image in the specified direction
  This is useful for visualization and debugging
  
  :param img: is the image array
  :param direction: is the direction which the image will face
  '''
  pass

def batch_process_folder(folder_path, output_path, operation):
  '''
  This is important for batch processing, for automation and operation
  
  :param folder_path: Description
  :param output_path: Description
  :param operation: Description
  '''
  

