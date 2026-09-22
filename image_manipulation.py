import cv2
import numpy as np

# Load the image
img = cv2.imread("sample.png")

if img is None:
    print("Error: Could not load image.")
    exit()

# Resize original image for easy viewing
img = cv2.resize(img, (500, 400))

print("=" * 55)
print("IMAGE PROPERTIES")
print("=" * 55)

height, width, channels = img.shape
print(f"Shape (H, W, C)     : {img.shape}")
print(f"Height              : {height}")
print(f"Width               : {width}")
print(f"Channels            : {channels}")
print(f"Total Pixels        : {img.size}")
print(f"Data Type           : {img.dtype}")
print(f"Mean Pixel Value    : {cv2.mean(img)}")

print("\n" + "=" * 55)
print("IMAGE MANIPULATION & CROPPING")
print("=" * 55)

# 1. Cropping (select a region)
# Format: img[y1:y2, x1:x2]
cropped = img[50:250, 100:350]      # Crop a portion of the image

# 2. Resizing
resized = cv2.resize(img, (300, 200))

# 3. Flipping
flip_horizontal = cv2.flip(img, 1)  # 1 = Horizontal flip
flip_vertical   = cv2.flip(img, 0)  # 0 = Vertical flip
flip_both       = cv2.flip(img, -1) # -1 = Both axes

# 4. Convert to grayscale (simple manipulation)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print("Cropping, Resizing and Flipping done successfully!")

# Display all results
cv2.imshow("1. Original Image", img)
cv2.imshow("2. Cropped Image", cropped)
cv2.imshow("3. Resized Image", resized)
cv2.imshow("4. Horizontal Flip", flip_horizontal)
cv2.imshow("5. Vertical Flip", flip_vertical)
cv2.imshow("6. Grayscale", gray)

print("\nAll manipulated images are displayed.")
print("Press any key to close the windows...")

cv2.waitKey(0)
cv2.destroyAllWindows()