import cv2

image = cv2.imread(r"C:/Users/NILESH/Desktop/rakhi.jpg", cv2.IMREAD_COLOR)

cv2.imshow("Color Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
