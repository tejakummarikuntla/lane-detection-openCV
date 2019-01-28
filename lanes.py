import cv2
import numpy as np

#-----STEPS--------
# 1. Changing the image in to gray Scale
# 2. (Reduce Noise) applying guassian blue on the image
# 3. Apply canny method to identify edges in an image

image = cv2.imread('test_image.jpg')
#making a copy of image in array rep
lane_image = np.copy(image)
#converting the image in to gray sclae for reducing the channels
#gray scale images only has single channel, while RGB has three channesl
gray_image = cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)

#we need to clear the noise in the image, because Image noise can create false noise
# ultmately affects edge detection.
#thats smooting the image.
#filtering and smoothing the image can be done by guassian filter

#to smooth the image --------------
# we can smooth by modifing the value of a pixel by average value of the
#pixel intensities around the target pixel.
#averaging out the pixels in the image to reduce noise is done by a kernal.
blur_image = cv2.GaussianBlur(gray_image, (5,5), 0)
#But, when we apply a canny funtion we don't to apply GaussianBlur specially,
#because cany funtion internally applies it.

#applying Canny method to identify edges.
#The change in brightness over a series of pixels is the GRADIENT.
#A strong gradinent indicates a deep change and a small gradient indicates a slight change
canny_image = cv2.Canny(blur_image,50, 150)

cv2.imshow('result',canny_image)
#waits for any keyPress to close.
cv2.waitKey(0)
