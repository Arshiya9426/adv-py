import cv2
import numpy as np

# Create a blank white image
image = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Draw a rectangle
# Parameters: image, top-left point, bottom-right point, color(BGR), thickness
cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), 3)

# Draw a filled rectangle
cv2.rectangle(image, (250, 50), (450, 200), (0, 255, 0), -1)

# Draw a circle
# Parameters: image, center, radius, color(BGR), thickness
cv2.circle(image, (125, 350), 60, (0, 0, 255), 3)

# Draw a filled circle
cv2.circle(image, (350, 350), 60, (255, 0, 255), -1)

# Display the image
cv2.imshow("Rectangles and Circles", image)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()