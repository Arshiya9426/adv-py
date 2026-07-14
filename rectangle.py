import cv2
import numpy as np

drawing = False
ix, iy = -1, -1

# Create a white image
img = np.ones((500, 500, 3), np.uint8) * 255

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp = img.copy()
            # Blue rectangle
            cv2.rectangle(temp, (ix, iy), (x, y), (255, 0, 0), 2)
            cv2.imshow("Rectangle", temp)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # Final blue rectangle
        cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 2)

# Create window
cv2.namedWindow("Rectangle")
cv2.setMouseCallback("Rectangle", draw_rectangle)

while True:
    cv2.imshow("Rectangle", img)

    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cv2.destroyAllWindows()