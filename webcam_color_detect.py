import cv2
import numpy as np

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Blue color range in HSV
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])

    # Create mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Remove noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)

        # Ignore small objects
        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)

            # Draw rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display label
            cv2.putText(frame, "Blue Color",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (255, 0, 0),
                        2)

    # Show original frame
    cv2.imshow("Blue Color Detection", frame)

    # Show mask
    cv2.imshow("Mask", mask)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
cap.release()
cv2.destroyAllWindows()