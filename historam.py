import numpy as np
import matplotlib.pyplot as plt

def histogramEqualiser(imageEq):
  hist,bins = np.histogram(imageEq.flatten(),256,[0,256])

  cdf = hist.cumsum()
  cdf_normalized = cdf * hist.max()/ cdf.max()

  fig = plt.figure()
  fig.add_subplot(3, 4, 1)
  plt.imshow(imageEq,cmap='gray')

  fig.add_subplot(3, 4, 2)
  plt.hist(imageEq.flatten(),256,[0,256], color = 'r')
  plt.xlim([0,256])

  cdf_m = np.ma.masked_equal(cdf,0)
  cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
  cdf = np.ma.filled(cdf_m,0).astype('uint8')
  img2 = cdf[imageEq]

  fig.add_subplot(3, 4, 3)
  plt.imshow(img2,cmap='gray')

  fig.add_subplot(3, 4, 4)
  plt.hist(img2.flatten(),256,[0,256], color = 'b')
  plt.xlim([0,256])