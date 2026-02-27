import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt 
import os 
from os import listdir
from PIL import Image


def check_if_valid(img):
  '''
  This function checks if the image is a valid image
  
  :param img: image to be tested 
  '''
  if img is None:
    raise ValueError('This is not a valid image')
  
def is_gray(img):
  '''
  This function if the image is in grayscale
  
  :param img: image array to be tested
  '''
  return len(img.shape) == 2


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
  
  check_if_valid(img)
  
  if len(img.shape) == 2:
    raise ValueError('This image is already in grayscale')
  
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
  #this functions checks if the image is valid
  check_if_valid(img)
  
  RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
  
  plt.imshow(RGB_img)
  plt.axis('off')
  plt.show()
  pass

def resize_image(img, img_width, img_height):
  '''
  This function will take the image array and resize it to
  the new dimensions

  Args: img is the image array 
        img_width is the new image width
        img_height is the new image height
  '''
  
  check_if_valid(img)
  
  resized_img = cv.resize(img, (img_width, img_height))
  
  return resized_img 

def crop_image(img, x_start, y_start, x_end, y_end):
  '''
  This function extracts a rectangular region of interest (ROI)
  from the image
  Cropping is commonly used in preprocessing, object detection pipelines,
  and isolating specific regions for further analysis
  
  :param img: this is the image array 
  :param x_start: x-coordinate of the top left corner of the crop
  :param y_start: the y-coordinate of the top-left corner of the top
  :param x_end: x-end coordinates of the crop
  :param y_end: y-end coordinates of the crop
  '''
  
  check_if_valid(img)
  img_height, img_width = img.shape[:2]
  
  if x_start >= 0 and y_start >= 0:
    if x_start < x_end and y_start < y_end and x_end <= img_width and y_end <= img_height:
      cropped_img = img[y_start:y_end, x_start:x_end]
      return cropped_img
    else: 
      raise ValueError('Invalid coordinates')
  else:
    raise ValueError('Invalid coordinates')

def rotate_image(img, angle):
  '''
  This funciton rotates the image by a specific angle
  
  Rotation is useful for data augmentation, alignment, and geomertric
  transformations in computer vision tasks
  
  :param img: is the image array 
  :param angle: Rotation angles in degrees (postive = counterclockwise)
  '''
  check_if_valid(img)
  
  img_height, img_width = img.shape[:2]
  
  # calculate x,y coordinate of center
  cX = int(img_width / 2)
  cY = int(img_height / 2)
  
  
  rotate_matrix = cv.getRotationMatrix2D((cX, cY), angle, 1)
  
  rotated_image = cv.warpAffine(img, rotate_matrix, (img_width, img_height))
  
  return rotated_image

def flip_image(img, direction):
  '''
  Flips the image horizontally, vertically or both
  
  Flipping is usually used for data augmentation and creating
  oreintation-invariant training samples
  
  :param img: is the image array
  :param direction: 0 - vertical flip 
                    1 - horizontal flip
                    -1 - both
  '''
  check_if_valid(img)
  
  code_range = range(-1, 2)
  
  if direction in code_range:
    flipped_image = cv.flip(img, direction)
  else:
    raise ValueError('Invalid direction')
  
  return flipped_image
def batch_process_folder(folder_path, output_path, operation, *args):
  '''
  Applies a specified image operation to every image in a folder
  
  Batch proccessing is essential for automation, preprocessing pipelines,
  and preparing large data sets for machine learning workflows 
  
  :param folder_path: is the folder in which are all the images 
  :param output_path: is the folder in which proccessed images are saved
  :param operation: the operation that will be done on the images
  :param *args: extra arguments to make the function reusable for resize_image, flip_image, etc
  '''
  img_array = []
  img_proccessed = []
  if os.path.isdir(folder_path):
    
    if not os.path.exists(output_path):
      os.makedirs(output_path)
      
    for img in os.listdir(folder_path):
      if(img.endswith('.png') or img.endswith('.jpg') or img.endswith('.jpeg')):
        img_array.append(img)
    
    for img_name in img_array:
      #joining folder path and file name correctly 
      img_path = os.path.join(folder_path, img_name)
      img = load_image(img_path)
      img = operation(img, *args)
      # creating a new variable for joining folder path and file name to create a full path
      updated_image_path = os.path.join(output_path, img_name)
      save_image(img, updated_image_path)
      img_proccessed.append(updated_image_path)
      
  else:
    raise ValueError('Invalid path')
  
  # prints filepaths - img_proccessed
  return {'Image proccessed': len(img_proccessed), 'Images': img_proccessed}


def compute_histogram(img):
  '''
  This function takes an image array and returns a 256-bin histogram array
  Color images will be converted to grayscale unless the user passes a grayscale
  image
  
  :param img: color or grayscaled image
  '''
  
  check_if_valid(img)
  
  gray_img = img
  
  if not is_gray(img):
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  
  
  hist_array = [0 for _ in range(256)]
  
  # i is a row and j is the pixel intensity - the historgram bin to increment
  # There is 256 bins, one for each intensity value
  # The bin is incremented by 1 
  for i in gray_img:
    for j in i:
      hist_array[j] += 1 
    
  return hist_array
    
    

def compute_color_histogram(img):
  '''
  This function will return a dicontonary of 3 separate histograms arrays 
  in the order B G R
  
  :param img: color image
  '''
  rgb_img = img
  rgb_img = rgb_img.astype('uint8')
  
  if is_gray(img):
    rgb_img = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
  
  b, g, r = cv.split(rgb_img)
  
  b_hist_array = [0 for _ in range(256)]
  g_hist_array = [0 for _ in range(256)]
  r_hist_array = [0 for _ in range(256)]
  
  for i in b:
    for j in i:
      b_hist_array[j] += 1
  
  for i in g:
    for j in i:
      g_hist_array[j] += 1
  
  for i in r:
    for j in i:
      r_hist_array[j] += 1
      
  
  return r_hist_array, g_hist_array, b_hist_array

def plot_histogram(hist):
  '''
  This function will plot the histogram and visualized the intensity distribution 
  
  :param hist: histogram array 
  '''
  if not len(hist) == 256:
    raise ValueError('This histogram array is invalid')
  
  fig, ax = plt.subplots(figsize=(10,4))
  
  plt.plot(hist)
  plt.xlabel('Pixel values')
  plt.ylabel('Count of pixel values/ Histogram counts')
  plt.title('Histogram of a Grayscaled Image')
  
  plt.show()
  

def plot_color_histogram(hist_r, hist_g, hist_b):
  '''
  This function will plot the combined RGB (red, green, blue) histogram 
  Each histogram is plotted in its corresponding color
  
  :param hist_r: Red historgram to be displayed 
  :param hist_g: Green historgram to be displayed
  :param hist_b: Blue histogram to be displayed
  '''
  
  if not (len(hist_r) == 256 and len(hist_g) == 256 and len(hist_b) == 256):
    raise ValueError('Invalid color imgage')
  
  plt.plot(hist_r, color = 'red', label = 'Red histogram')
  plt.plot(hist_g, color = 'green', label = 'Green histogram')
  plt.plot(hist_b, color = 'blue', label = 'Blue histogram')
  plt.xlabel('Pixel values')
  plt.ylabel('Count of red, green, and blue pixel values/ Histogram counts')
  plt.title('Color Histogram')
  
  plt.show()

def adjust_brightness(img, value):
  '''
  Adjusts the brightness of the image by adding a constant value to every pixel 
  Positive values brighten the image; negative values darken it
  This function will work for grayscale and color images. Pixel values will be clipped 
  to 0-255
  
  :param img: input image (color or grayscale)
  :param value: value to be added or subtracted from each pixel
  '''
  
  check_if_valid(img)
  
  adj_img = img.copy()
  
  if is_gray(adj_img):
    row, column = img.shape
    
    for i in range(row):
      
      for j in range(column):
        adj_img[i, j] += value
        
        if adj_img[i, j] < 0:
          adj_img[i, j] = 0
        elif adj_img[i, j] > 255:
          adj_img[i, j] = 255
        
        
  else: 
    blue = adj_img[..., 0]
    green = adj_img[..., 1]
    red = adj_img[..., 2]
    
    row_b, column_b = blue.shape
    for i in range(row_b):
      
      for j in range(column_b):
        blue[i, j] += value
        
        if blue[i, j] < 0:
          blue[i, j] = 0
        elif blue[i, j] > 255:
          blue[i, j] = 255
    
    row_g, column_g = green.shape
    for i in range(row_g):
      
      for j in range(column_g):
        green[i, j] += value
        
        if green[i, j] < 0:
          green[i, j] = 0
        elif green[i, j] > 255:
          green[i, j] = 255
        
    row_r, column_r = red.shape
    for i in range(row_r):
      
      for j in range(column_r):
        red[i, j] += value
        if red[i, j] < 0:
          red[i, j] = 0
        elif red[i, j] > 255:
          red[i, j] = 255
  
  
  return adj_img

def adjust_contrast(img, factor):
  '''
  Adjusts the contrast of an image by multiplying all pixel values by a factor
  Factor > 1 will increase contrast while a factor b/n 0 and 1 will decrease it
  This function will work for grayscale and color image. Pixel values will be clipped 0-255
  
  :param img: input image (color or grayscale)
  :param factor: the factor that each pixel value will be multiplied with
  '''
  adj_img = img.copy()
  
  if is_gray(adj_img):
    row, column = img.shape
    
    for i in range(row):
      
      for j in range(column):
        adj_img[i, j] *= factor
        
        if adj_img[i, j] < 0:
          adj_img[i, j] = 0
        elif adj_img[i, j] > 255:
          adj_img[i, j] = 255
  
  else:
    blue = adj_img[..., 0]
    green = adj_img[..., 1]
    red = adj_img[..., 2]
    
    row_b, column_b = blue.shape
    for i in range(row_b):
      
      for j in range(column_b):
        blue[i, j] *= factor
        
        if blue[i, j] < 0:
          blue[i, j] = 0
        elif blue[i, j] > 255:
          blue[i, j] = 255
    
    row_g, column_g = green.shape
    for i in range(row_g):
      
      for j in range(column_g):
        green[i, j] *= factor
        
        if green[i, j] < 0:
          green[i, j] = 0
        elif green[i, j] > 255:
          green[i, j] = 255
        
    row_r, column_r = red.shape
    for i in range(row_r):
      
      for j in range(column_r):
        red[i, j] *= factor
        if red[i, j] < 0:
          red[i, j] = 0
        elif red[i, j] > 255:
          red[i, j] = 255
  
  
  return adj_img

def normalize_image(img):
  '''
  This funciton will perform intensity normalization.
  This means it will scale the pixel values so that the minimum be 0 and the 
  maximum be 255
  This function will work for grayscale and color images
  
  :param img: input image (color or grayscale)
  '''
  check_if_valid(img)
  
  img_copy = img.copy()
  
  row, column = img_copy.shape
  
  if is_gray(img_copy):
    max = 0 
    min = 255
    
    for i in range(row):
      
      for j in range(column):
        if max < img_copy[i, j]: 
          max = img_copy[i, j]
        if min > img_copy[i, j]: 
          min = img_copy[i, j]
    
    for i in range(row):
      
      for j in range(column):
        img_copy[i, j] -= min
        if not (max - min == 0):
          img_copy[i, j] /= (max - min)
        img_copy[i, j] *= 255
        
        if img_copy[i, j] < 0: 
          img_copy[i, j] = 0
        elif img_copy[i, j] > 255: 
          img_copy[i, j] = 255
  
  else:
    blue = img_copy[..., 0]
    green = img_copy[..., 1]
    red = img_copy[..., 2]
    
    max = 0
    min = 255
    
    row_b, column_b = blue.shape
    row_g, column_g = green.shape
    row_r, column_r = red.shape
    
    for i in range(row_b):
      for j in range(column_b):
        if max < blue[i, j]: 
          max = blue[i, j]
        if min > blue[i, j]: 
          min = blue[i, j]
        
    for i in range(row_b):
      for j in range(column_b):
        blue[i, j] -= min
        if not (max - min == 0):
          blue[i, j] /= (max - min)
        blue[i, j] *= 255
        
        if blue[i, j] < 0: 
          blue[i, j] = 0
        elif blue[i, j] > 255: 
          blue[i, j] = 255
    
    max = 0
    min = 255
          
    for i in range(row_g):
      for j in range(column_g):
        if max < green[i, j]: 
          max = green[i, j]
        if min > green[i, j]: 
          min = green[i, j]
        
    for i in range(row_g):
      for j in range(column_g):
        green[i, j] -= min
        if not (max - min == 0):
          green[i, j] /= (max - min)
        green[i, j] *= 255
        
        if green[i, j] < 0: 
          green[i, j] = 0
        elif green[i, j] > 255: 
          green[i, j] = 255

    max = 0
    min = 255
    
    for i in range(row_r):
      for j in range(column_r):
        if max < red[i, j]: 
          max = red[i, j]
        if min > red[i, j]: 
          min = red[i, j]
        
    for i in range(row_r):
      for j in range(column_r):
        red[i, j] -= min
        if not (max - min == 0):
          red[i, j] /= (max - min)
        red[i, j] *= 255
        
        if red[i, j] < 0: 
          red[i, j] = 0
        elif red[i, j] > 255: 
          red[i, j] = 255
  
  return img_copy
  

def contrast_stretch(img):
  '''
  This function will find the min and max pixel values 
  This funciton will linearly stretch intesities to fill 0-255
  This funciton will improve the contrast by streching the histogram
  
  :param img: input image (color or grayscale)
  '''
  img_copy = img.copy()
  
  max = 0
  min = 255
  
  if is_gray(img_copy):
    row, column = img.shape
    
    for i in range(row):
      for j in range(column):
        if max < img_copy[i, j]:
          max = img_copy[i, j]
        if min > img_copy[i, j]:
          min = img_copy[i, j]
    
    for i in range(row):
      for j in range(column):
        img_copy[i, j] -= min
        if not (max - min == 0):
          img_copy[i, j] /= (max - min)
        img_copy[i, j] *= 255
        
        if img_copy[i, j] < 0:
          img_copy[i, j] = 0
        elif img_copy[i, j] > 255:
          img_copy[i, j] = 255
  
  else:
    max = 0
    min = 255
    
    blue = img_copy[..., 0]
    green = img_copy[..., 1]
    red = img_copy[..., 2]
    
    row_b, column_b = blue.shape
    
    for i in range(row_b):
      for j in range(column_b):
        if max < blue[i, j]:
          max = blue[i, j]
        if min > blue[i, j]:
          min = blue[i, j]
    
    for i in range(row_b):
      for j in range(column_b):
        blue[i, j] -= min
        if not (max - min == 0):
          blue[i, j] /= (max - min)
        blue[i, j] *= 255
        
        if blue[i, j] < 0:
          blue[i, j] = 0
        elif blue[i, j] > 255:
          blue[i, j] = 255
          
    
    max = 0
    min = 255
    
    row_g, column_g = green.shape
    
    for i in range(row_g):
      for j in range(column_g):
        if max < green[i, j]:
          max = green[i, j]
        if min > green[i, j]:
          min = green[i, j]
    
    for i in range(row_g):
      for j in range(column_g):
        green[i, j] -= min
        if not (max - min == 0):
          green[i, j] /= (max - min)
        green[i, j] *= 255
        
        if green[i, j] < 0:
          green[i, j] = 0
        elif green[i, j] > 255:
          green[i, j] = 255
    
    max = 0
    min = 255
    
    row_r, column_r = red.shape
    
    for i in range(row_r):
      for j in range(column_r):
        if max < red[i, j]:
          max = red[i, j]
        if min > red[i, j]:
          min = red[i, j]
    
    for i in range(row_r):
      for j in range(column_r):
        red[i, j] -= min
        if not (max - min == 0):
          red[i, j] /= (max - min)
        red[i, j] *= 255
        
        if red[i, j] < 0:
          red[i, j] = 0
        elif red[i, j] > 255:
          red[i, j] = 255
    
  
  return img_copy

def histogram_equalization(img):
    '''
    This function applies histogram equalization to the whole image
    
    :param img: image to be proccessed
    '''
    
    new_img = img.copy()
    org_img = img.copy()
    
    if not is_gray(new_img):
        new_img = to_grayscale(img)
    
    gray_img = new_img.copy()
    
    gray_img = gray_img.astype('uint8')
    gray_img = cv.equalizeHist(gray_img)
    
    return gray_img

def histogram_equalization_clahe_grayscale(img, clip_limit = 10, grid_size=(8, 8)):
    '''
    Applies CACHE (Contrast Limited Adaptive Histogram Equalization) to an grayscale image
    or just a single channel
    
    
    :param img: uint8 numpy array of shape (heigth, width)
    :param clip_limit: maximum allowed value for each histogram bin
    :param grid_size: Tuple (n_rows, n_cols) indicating the number of regions the image is divided
    into
    '''
    
    new_img = img.copy()
    if not is_gray(img):
        new_img = to_grayscale(new_img)
    
    gray_img = new_img.copy()
    
    clahe = cv.createCLAHE(clip_limit, grid_size)
    cl1 = clahe.apply(gray_img)
    
    cv.imwrite('clahe_2.jpg', cl1)
    
    return cl1

def adjust_gamma(img, gamma):
    '''
    This fucntion will apply gamma correction for displaying images on the screen correctly 
    This will help to linearize the percieved brightness
    
    :param img: is the image to be proccessed 
    :param gamma: the scale in which the image brightness will be adjusted 
    '''
    if gamma <= 0:
        raise ValueError('Invalid gamma value')
    new_img = img.copy()
    
    gamma_corrected = np.array(255 * (new_img.astype(float) / 255.0) ** gamma, dtype = 'uint8')
    
    return gamma_corrected
        

def gray_world(img):
    '''
    This function will white balance the image using the gray-world algorithm
    
    :param img: image to be processed
    '''
    new_img = img.copy()
    img_LAB = cv.cvtColor(new_img, cv.COLOR_BGR2LAB)
    avg_a = np.average(img_LAB[:, :, 1])
    avg_b = np.average(img_LAB[:, :, 2])
    img_LAB[:, :, 1] = img_LAB[:, :, 1] - ((avg_a - 128) * (img_LAB[:, :, 0] / 255.0) * 1.2)
    img_LAB[:, :, 2] = img_LAB[:, :, 2] - ((avg_b - 128) * (img_LAB[:, :, 0] / 255.0) * 1.2)
    
    balanced_img = cv.cvtColor(img_LAB, cv.COLOR_LAB2BGR)
    
    return balanced_img

def plot_before_after(original, enhanced, title_before = 'Original', title_after = 'Enhanced'):
  '''
  This function will show the a side-by-side images of any combination. It could be grayscaled or 
  RGB images side by side. Gray -> Gray, RGB -> RGB, Gray -> RGB, etc
  
  :param original: is the original image
  :param enhanced: is the enhanced image
  :param title_before: the title of the original image
  :param title_after: the title of the enhanced image
  '''
  plt.figure(figsize = (10,6))
  
  plt.subplot(1, 2, 1)
  
  if is_gray(original):
    plt.imshow(original, cmap='gray')
  else:
    plt.imshow(original)
  
  plt.title(title_before)
  plt.axis('off')
  
  plt.subplot(1, 2, 2)
  
  if is_gray(enhanced):
    plt.imshow(enhanced, cmap='gray')
  else:
    plt.imshow(enhanced)
    
  plt.title(title_after)
  plt.axis('off')
  
  plt.tight_layout()
  plt.show()
  
def hist_before_after(original, enhanced, title_before = 'Original', title_after = 'Enhanced'):
  '''
  This function will show a side-by-side figure of a histogram before and after enhancement to show 
  how the pixel distribution changed 
  
  :param original: is the original image
  :param enhanced: is the enhanced enhanced with the changed pixel distribution 
  :param title_before: title of the original histogram
  :param title_after: title of the enhanced histogram
  '''
  plt.figure(figsize = (10,6))
  
  plt.subplot(1, 2, 1)
  
  if is_gray(original):
      hist = compute_histogram(original)
      plot_histogram(hist)
  else:
      hist_r, hist_g, hist_b = compute_color_histogram(original)
      plot_color_histogram(hist_r, hist_g, hist_b)
  
  plt.title(title_before)
  
  plt.subplot(1, 2, 2)
  
  if is_gray(enhanced):
      hist = compute_histogram(enhanced)
      plot_histogram(hist)
  else:
      hist_r, hist_g, hist_b = compute_color_histogram(enhanced)
      plot_color_histogram(hist_r, hist_g, hist_b)
  
  plt.title(title_after)
  
  plt.suptitle('Histogram comparision')
  
  plt.tight_layout()

def clahe_eqlz_before_after(img):
  '''
  This function will show a side-by-side figure of an orginal, equalized and clahe equalized image
  
  :param img: image to be shown and processed
  '''
  plt.figure(figsize = (10,6))
  
  gray_img = img.copy()
  
  plt.subplot(1, 3, 1)
  plt.imshow(gray_img)
  plt.title('Original image')
  plt.axis('off')
  
  if not is_gray(img):
    gray_img = to_grayscale(img)
  
  eqlz_img = histogram_equalization(gray_img)
  
  plt.subplot(1, 3, 2)
  plt.imshow(eqlz_img, cmap='gray')
  plt.title('Equalized image')
  plt.axis('off')
  
  clah_img = histogram_equalization_clahe_grayscale(gray_img)
  
  plt.subplot(1, 3, 3)
  plt.imshow(clah_img, cmap='gray')
  plt.title('Clahe equalized image')
  plt.axis('off')
  
  plt.suptitle('CLAHE‑vs‑Equalization comparison')
  