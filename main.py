import cv2
import numpy as np

# Load the image
image = cv2.imread(r"C:\Users\NILESH\Pictures\rimon.jpg")

# Check if the image is loaded correctly
if image is None:
    print("Error: Could not read the image. Check the file path.")
else:
    # Convert image to HSV (Hue, Saturation, Value)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Split channels
    h, s, v = cv2.split(hsv)
    
    # Increase brightness by 30 (clip to keep values in [0,255])
    v = np.clip(v + 30, 0, 255)
    
    # Merge back the channels
    bright_hsv = cv2.merge((h, s, v))
    
    # Convert back to BGR color space
    bright_image_30 = cv2.cvtColor(bright_hsv, cv2.COLOR_HSV2BGR)

    # Display the original and brightened images
    cv2.imshow("Original Image", image)
    cv2.imshow("Brightened Image (+30)", bright_image_30)

    # Wait and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
