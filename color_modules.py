import cv2
import numpy as np

# Load the image
img = cv2.imread("motorsport.jpg")

if img is None:
    print("Error: Could not load image. Check the file path.")
    exit()

print("=" * 55)
print("COLOR MODELS DEMONSTRATION")
print("=" * 55)

# Resize image to smaller size (width = 400 pixels)
scale_width = 400
ratio = scale_width / img.shape[1]
dim = (scale_width, int(img.shape[0] * ratio))
img = cv2.resize(img, dim)

# Convert to different color models
rgb  = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv  = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab  = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

print(f"Original Image Shape (BGR): {img.shape}")
print(f"RGB Image Shape           : {rgb.shape}")
print(f"Grayscale Image Shape     : {gray.shape}")
print(f"HSV Image Shape           : {hsv.shape}")
print(f"LAB Image Shape           : {lab.shape}")

# Display all color models (now smaller)
cv2.imshow("1. Original (BGR)", img)
cv2.imshow("2. RGB", rgb)
cv2.imshow("3. Grayscale", gray)
cv2.imshow("4. HSV", hsv)
cv2.imshow("5. LAB", lab)

print("\nAll images are resized to smaller size.")
print("Press any key to close all windows...")

cv2.waitKey(0)
cv2.destroyAllWindows()