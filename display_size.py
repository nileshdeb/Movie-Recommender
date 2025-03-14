import cv2
import os

image_path = r"C:/Users/NILESH/Desktop/rakhi.jpg"
if not os.path.exists(image_path):
    print(f" Error: File not found at {image_path}")
else:
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    if image is None:
        print(" Error: Could not read the image. Check the file format or path.")
    else:
        height, width, channels = image.shape
        print(f" Image Size: Width = {width}, Height = {height}, Channels = {channels}")

        cv2.imshow("Color Image", image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
