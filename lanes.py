import cv2
import numpy as np

def canny(image):
    gray_image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur_image = cv2.GaussianBlur(gray_image, (5,5), 0)
    canny_image = cv2.Canny(blur_image,50, 150)
    return canny_image

def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1,y1), (x2,y2), (255, 0, 0), 10)
    return line_image

def region_of_intrest(image):
    height = image.shape[0]
    polygons = np.array([
    [(200, height), (1100, height), (550, 250)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
canny = canny(lane_image)
cropped_image = region_of_intrest(canny)
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5 )
line_image = display_lines(lane_image, lines)
combo_imge = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)
# cv2.imshow('result',canny)
cv2.imshow("result",combo_imge)

cv2.waitKey(0)
