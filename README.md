# lane-detection-openCV

```image = cv2.imread('test_image.jpg')``` </br>
#making a copy of image in array rep </br>
```lane_image = np.copy(image)```
# converting the image in to gray sclae for reducing the channels </br>
#gray scale images only has single channel, while RGB has three channesl </br>
```gray_image = cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)``` </br>

#we need to clear the noise in the image, because Image noise can create false noise </br>
#ultimately affects edge detection. </br>
#thats smooting the image. </br>
#filtering and smoothing the image can be done by guassian filter </br>

# To smooth the image </br>
#we can smooth by modifing the value of a pixel by average value of the </br>
#pixel intensities around the target pixel. </br>
#averaging out the pixels in the image to reduce noise is done by a kernal. </br>
```blur_image = cv2.GaussianBlur(gray_image, (5,5), 0)``` </br>
- But, when we apply a canny funtion we don't to apply GaussianBlur specially, </br>
- because cany funtion internally applies it. </br>

# applying Canny method to identify edges. </br>
- The change in brightness over a series of pixels is the GRADIENT. </br>
- A strong gradinent indicates a steep change and a small gradient indicates a shallow change </br> 
- To compute the gradient of a image one must recongnise, that we can represent an image in a two dimensional co-ordinate space [x,y]
- The X-axis represents the image's width and the y- axis go along the image's hight
- width represents the no.of columns and Hight represents the no.of rows, such that the product of width and the hight 
gives you the total number of pixels in the image.
 
```cv2.imshow('result',blur_image)``` </br>
#waits for any keyPress to close. </br>
```cv2.waitKey(0)``` </br>
