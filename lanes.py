import cv2
import numpy as np

def canny(image):
    gray_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur_image = cv2.GaussianBlur(gray_image, (5,5), 0)
    canny_image = cv2.Canny(blur_image,50, 150)
    return canny_image

def region_of_intrest(image): 
    height = image.shape[0]
    polygons = np.array([
    [(200, height), (1100, height), (550, 250)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    return mask


image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny = canny(lane_image)

# cv2.imshow('result',canny)
cv2.imshow("result",region_of_intrest(canny))
cv2.waitKey(0)
