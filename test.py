# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 19:02:15 2022

@author: Andrew
"""

import numpy as np
from matplotlib import image
from matplotlib import pyplot as plt


'''
# PIL version
from PIL import Image
# Import the world map image and display it
image = Image.open('Images/BaseMap.png')

print('Image size: {}'.format(image.size))

image.show() # displays the image in a seperate window
'''

# load the image in via pyplot
image = image.imread('Images/BaseMap.png') # this is an np array already
plt.imshow(image)
plt.show()

imdata = image[:,:,0:3]


# get all the unique colours from the image
uniqueColours = np.array([0, 0,0])
for y in imdata:
    colours_in_row = np.unique(y,axis=0)
    uniqueColours = np.unique(np.vstack((uniqueColours,colours_in_row)),axis=0)
    
print(uniqueColours)

# turn unique colours into image
dims = np.shape(uniqueColours)
newImg = np.ones((50,10*dims[0],4))

for i,c in enumerate(uniqueColours):
    for j in range(10):
        newImg[:,10*i + j,0:3] = c
        
newImg = np.float32(newImg)

plt.imshow(newImg)
plt.show()



image[0:50,0:110,0:4] = newImg
plt.imshow(imdata)
plt.show()



