import cv2

image = cv2.imread("your image path")    

cv2.imshow("hori", image)

cv2.waitKey(0)

grey_pic = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Hori new", grey_pic)
cv2.waitKey(0)

inverted = 255 - grey_pic
cv2.imshow("Inverted", inverted)
cv2.waitKey()

blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
inverted_blur = 255 - blurred

pencil_sketch = cv2.divide(grey_pic, inverted_blur, scale=256.0)

cv2.imshow("Sketch", pencil_sketch)
cv2.waitKey(0)

cv2.imwrite('pencil_sketch.png', pencil_sketch)
cv2.waitKey(0)
