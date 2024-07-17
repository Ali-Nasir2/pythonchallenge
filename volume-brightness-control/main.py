import mediapipe as mp
import screen_brightness_control as sbc
import cv2
import pyautogui

pyautogui.FAILSAFE = False

video_cam = cv2.VideoCapture(0)

signn = mp.solutions.hands
hands = signn.Hands(static_image_mode=False, max_num_hands=1,
                    min_detection_confidence=0.5, min_tracking_confidence=0.5)

result = mp.solutions.drawing_utils

while True:
    frameavail, currentframe = video_cam.read()
    if not frameavail:
        
        break

    frame_color = cv2.cvtColor(currentframe, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_color)

    if results.multi_hand_landmarks:

        for points in results.multi_hand_landmarks:

            result.draw_landmarks(currentframe, points, signn.HAND_CONNECTIONS)

            # Volume and brightness control logic
            fingerTipY = points.landmark[signn.HandLandmark.INDEX_FINGER_TIP].y
            indexFingerDipY = points.landmark[signn.HandLandmark.INDEX_FINGER_DIP].y
            middleFingerTipY = points.landmark[signn.HandLandmark.MIDDLE_FINGER_TIP].y
            middleFingerDipY = points.landmark[signn.HandLandmark.MIDDLE_FINGER_DIP].y

            if fingerTipY < indexFingerDipY:
                finger_point = 'up'
            else:
                finger_point = 'down'

            if middleFingerTipY < middleFingerDipY:
                middle_finger_point = 'up'
            else:
                middle_finger_point = 'down'

            if finger_point == 'up' and middle_finger_point != 'up':
                pyautogui.press('volumeup')
            elif finger_point == 'down' and middle_finger_point != 'down':
                pyautogui.press('volumedown')

            if finger_point == 'up' and middle_finger_point == 'up':
                sbc.set_brightness('+10')
            elif finger_point == 'down' and middle_finger_point == 'down':
                sbc.set_brightness('-10')

    cv2.imshow('Hand Gesture', currentframe)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_cam.release()
cv2.destroyAllWindows()

