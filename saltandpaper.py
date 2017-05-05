import PIL
from PIL import Image
import numpy as np
from numpy.random import normal
import matplotlib.pyplot as plt

im = Image.open("saltandpaper.tif")
im = im.convert('L')#converting to greyscale
pixels=np.asarray(im).copy()#numpy array for original image

print 'enter filter size'
filsize=input()#filter size
pad=int((filsize/2)+1)

copy=np.zeros(shape=((len(pixels)+pad),(len(pixels[0])+pad)))

filt=np.zeros(shape=(filsize,filsize))

for row in range(len(pixels)-pad):
   for col in range(len(pixels[row])-pad):
      summ=0
      for i in range(filsize):
         for j in range(filsize):
            filt[i][j] = pixels[row-((pad-1)-i)][col-((pad-1)-j)]
            pixxy=np.sort(filt,axis=None)
            
      copy[row][col] = pixxy[int(filsize*filsize)/2]#int((int(pixels[row-1][col-1])+int(pixels[row][col-1])+int(pixels[row+1][col-1])+int(pixels[row-1][col])+int(pixels[row][col])+int(pixels[row+1][col])+int(pixels[row-1][col+1])+int(pixels[row][col+1])+int(pixels[row+1][col+1]))/9)
      
im=PIL.Image.fromarray(np.uint8(copy))
im.save("chuss3.png")
im.show()
