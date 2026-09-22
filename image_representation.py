import cv2
import numpy as np

# 1. Read the image
img = cv2.imread("sample.png")   # Replace with your image path

# Check if image is loaded successfully
if img is None:
    print("Error: Could not load image. Check the file path.")
    exit()

# 2. Image Representation & Resolution
print("=" * 50)
print("IMAGE REPRESENTATION & RESOLUTION")
print("=" * 50)

height, width, channels = img.shape
total_pixels = height * width

print(f"Image Shape (H, W, C)     : {img.shape}")
print(f"Height (rows)             : {height} pixels")
print(f"Width  (columns)          : {width} pixels")
print(f"Number of Channels        : {channels}")
print(f"Resolution                : {width} × {height}")
print(f"Total Pixels              : {total_pixels:,}")
print(f"Data Type                 : {img.dtype}")
print(f"Memory size (approx)      : {img.nbytes / 1024:.2f} KB")

# 3. Accessing Individual Pixel Values
print("\n" + "=" * 50)
print("PIXEL VALUES")
print("=" * 50)

# Access a specific pixel (row, column)
y, x = 100, 150   # Example coordinates
pixel = img[y, x]

print(f"Pixel at location ({x}, {y}):")
print(f"  BGR values → Blue: {pixel[0]}, Green: {pixel[1]}, Red: {pixel[2]}")

# Access only Blue channel value of that pixel
print(f"  Blue channel only     : {img[y, x, 0]}")

# 4. Convert to Grayscale to show 2D representation
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(f"\nGrayscale Image Shape   : {gray.shape}  (only Height × Width)")
print(f"Pixel value at ({x},{y}) : {gray[y, x]}  (single intensity value)")

# 5. Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)

print("\nPress any key to close the windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

