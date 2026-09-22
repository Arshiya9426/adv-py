import cv2

# 1. Reading an Image
img = cv2.imread("sample.png")

if img is None:
    print("Error: Could not load image.")
    exit()

print("Image read successfully!")
print(f"Image Shape: {img.shape}")

# Resize for better viewing
img = cv2.resize(img, (400, 300))

# 2. Displaying the Image
cv2.imshow("Original Image", img)

print("Image is displayed. Press any key to continue...")
cv2.waitKey(0)          # Wait until a key is pressed
cv2.destroyAllWindows() # Close the window

# 3. Writing (Saving) the Image
# Save as JPG
cv2.imwrite("saved_image.jpg", img)

# Save as PNG
cv2.imwrite("saved_image.png", img)

print("Image saved successfully as:")
print(" → saved_image.jpg")
print(" → saved_image.png")