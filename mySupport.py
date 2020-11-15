def rgbExclusion(image, color):
  if color == 'r':
    image[:,:,2] = 0 #empty red channel
  elif color == 'g':
    image[:,:,1] = 0 #empty green channel
  elif color == 'b':
    image[:,:,0] = 0 #empty blue channel
  return image