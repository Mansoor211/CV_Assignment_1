import numpy as np

def convolve2dimen(image, filter):    
  # For this function we assume that the filter is 3x3 hence we are just padding one zero on all sides.
  # tempInputImage is used for padding input image for performing convolution
  tempInputImage = np.zeros((image.shape[0] + 2, image.shape[1] + 2))  
  # setting image in center leaving one pixel on all sides. 
  tempInputImage[1:-1, 1:-1] = image

  # Flip filter 180 degrees for convolution through matrix multiplication 
  filter = np.flipud(np.fliplr(filter)) 
  # Result of convolution on input image (tempInputImage) will be saved in rImage
  rImage = np.zeros((image.shape[0],image.shape[1]))     

  for y in range(image.shape[1]):          
    for x in range(image.shape[0]):
      # Matrix multiplication order would be filter multiplied with 3x3 portion of 
      # image (tempInputImage) and result will be saved in corresponding pixel of resultant image (rImage) 
      rImage[x,y]=(filter*tempInputImage[x:x+3,y:y+3]).sum()
  return rImage