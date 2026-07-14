import cv2
import numpy as np

# Create a blank image
height = 400
width = 600

img = np.zeros((height, width, 3), dtype=np.uint8)

# Create horizontal gradient
for x in range(width):
    blue = 255 - int((255 * x) / width)
    red = int((255 * x) / width)
    img[:, x] = (blue, 0, red)

# Display the image
cv2.imshow("Color Gradient", img)

cv2.waitKey(0)
cv2.destroyAllWindows()