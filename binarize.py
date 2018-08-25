import cv2
import numpy as np
import PIL
from PIL import Image

img = Image.open('urdu.jpg')

img = img.convert('L')

pixels=np.asarray(img).copy()

sum=0
total=0
for row in range(len(pixels)):
   for col in range(len(pixels[row])):
      sum=sum+pixels[row][col]
      total+=1

threshold=135
for row in range(len(pixels)):
   for col in range(len(pixels[row])):
       if pixels[row][col]>threshold:
           pixels[row][col]=255
       else:
           pixels[row][col]=pixels[row][col]
img=PIL.Image.fromarray(np.uint8(pixels))

img.save("binaryx.png")
img.show()
