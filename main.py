import cv2
import mediapipe as mp
import pyautogui
import time

def eye_aspect_ratio(landmarks, eye_indices):
    # Calculate the euclidean distances between the vertical eye landmarks
    A = ((landmarks[eye_indices[1]].x - landmarks[eye_indices[5]].x) ** 2 + (landmarks[eye_indices[1]].y - landmarks[eye_indices[5]].y) ** 2) ** 0.5
    B = ((landmarks[eye_indices[2]].x - landmarks[eye_indices[4]].x) ** 2 + (landmarks[eye_indices[2]].y - landmarks[eye_indices[4]].y) ** 2) ** 0.5
    # Calculate the euclidean distance between the horizontal eye landmarks
    C = ((landmarks[eye_indices[0]].x - landmarks[eye_indices[3]].x) ** 2 + (landmarks[eye_indices[0]].y - landmarks[eye_indices[3]].y) ** 2) ** 0.5
    # Compute the eye aspect ratio
    ear = (A + B) / (2.0 * C)
    return ear

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Indices for left eye landmarks from mediapipe face mesh
LEFT_EYE_INDICES = [33, 160, 158, 133, 153, 144]

# Blink detection parameters
EAR_THRESHOLD = 0.25
BLINK_DEBOUNCE_TIME = 1.0  # seconds
last_blink_time = 0

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 1:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                pyautogui.moveTo(screen_x, screen_y)

        # Draw left eye landmarks
        for idx in LEFT_EYE_INDICES:
            x = int(landmarks[idx].x * frame_w)
            y = int(landmarks[idx].y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        # Calculate EAR for left eye
        ear = eye_aspect_ratio(landmarks, LEFT_EYE_INDICES)

        # Blink detection with debounce
        current_time = time.time()
        if ear < EAR_THRESHOLD and (current_time - last_blink_time) > BLINK_DEBOUNCE_TIME:
            pyautogui.click()
            last_blink_time = current_time

    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)
