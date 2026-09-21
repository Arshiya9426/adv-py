import cv2
import mediapipe as mp

# MediaPipe
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
RunningMode = mp.tasks.vision.RunningMode

# Hand detector settings
options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path="models/hand_landmarker.task"
    ),
    running_mode=RunningMode.VIDEO,
    num_hands=1
)

# Open webcam
cap = cv2.VideoCapture(0)

previous_point = None
timestamp = 0

with HandLandmarker.create_from_options(options) as landmarker:

    while True:

        success, frame = cap.read()

        if not success:
            print("Cannot open webcam")
            break

        # Mirror webcam
        frame = cv2.flip(frame, 1)

        # Convert to MediaPipe image
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        timestamp += 1

        # Detect hand
        result = landmarker.detect_for_video(
            mp_image,
            timestamp
        )

        # If hand detected
        if result.hand_landmarks:

            hand = result.hand_landmarks[0]

            # Index finger tip = landmark 8
            finger = hand[8]

            height, width, _ = frame.shape

            x = int(finger.x * width)
            y = int(finger.y * height)

            current_point = (x, y)

            # Draw line
            if previous_point is not None:

                cv2.line(
                    frame,
                    previous_point,
                    current_point,
                    (0, 255, 0),
                    5
                )

            previous_point = current_point

            # Draw fingertip
            cv2.circle(
                frame,
                current_point,
                8,
                (0, 0, 255),
                -1
            )

        else:
            previous_point = None

        cv2.putText(
            frame,
            "Move your index finger to draw",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.putText(
            frame,
            "Press Q to quit",
            (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        cv2.imshow("Finger Drawing", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()