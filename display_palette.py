import cv2
import numpy as np

image_path = r"C:/Users/NILESH/Desktop/rakhi.jpg"
image = cv2.imread(image_path, cv2.IMREAD_COLOR)

if image is None:
    print("Error: Could not read the image.")
else:
    blue, green, red = cv2.split(image)

    blank = np.zeros_like(blue)

    blue_img = cv2.merge([blue, blank, blank])  
    green_img = cv2.merge([blank, green, blank])
    red_img = cv2.merge([blank, blank, red])

    cv2.imshow("Original Image", image)
    cv2.imshow("Blue Channel", blue_img)
    cv2.imshow("Green Channel", green_img)
    cv2.imshow("Red Channel", red_img)

    height, width, channels = image.shape
    print(f"Image Size: Width = {width}, Height = {height}, Channels = {channels}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
