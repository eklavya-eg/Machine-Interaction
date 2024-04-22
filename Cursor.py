import cv2
import mediapipe as mp
import pyautogui
import math


class Cursor:
    def start():
        frame_width = 1920
        frame_height = 1080

        cap = cv2.VideoCapture(0)
        mpHands = mp.solutions.hands
        hands = mpHands.Hands()
        mpDraw = mp.solutions.drawing_utils

        screen_width, screen_height = pyautogui.size()
        pyautogui.moveTo(screen_width // 2, screen_height // 2)

        prev_thumb_pos = None
        cursor_pos = pyautogui.position()
        smoothing_factor = 2
        click_threshold = 40

        left_click_pressed = False
        right_click_pressed = False

        while True:
            ret, img = cap.read()
            if not ret: continue
            img = cv2.resize(img, (frame_width, frame_height))
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(imgRGB)

            if results.multi_hand_landmarks:
                for handlms in results.multi_hand_landmarks:
                    thumb = None
                    index = None
                    middle = None
                    for id, lm in enumerate(handlms.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)

                        if id == 4:  # Thumb
                            thumb = (cx, cy)
                            cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
                        elif id == 8:  # Index finger
                            index = (cx, cy)
                            cv2.circle(img, (cx, cy), 15, (0, 255, 255), cv2.FILLED)
                        elif id == 12:  # Middle finger
                            middle = (cx, cy)
                            cv2.circle(img, (cx, cy), 15, (255, 0, 0), cv2.FILLED)

                    if thumb and prev_thumb_pos:
                        thumb_diff = (thumb[0] - prev_thumb_pos[0], thumb[1] - prev_thumb_pos[1])
                        thumb_diff = (-thumb_diff[0], thumb_diff[1])
                        cursor_pos = (cursor_pos[0] + int(thumb_diff[0] * smoothing_factor),
                                    cursor_pos[1] + int(thumb_diff[1] * smoothing_factor))
                        pyautogui.moveTo(cursor_pos[0], cursor_pos[1])

                    prev_thumb_pos = thumb

                    if thumb and index:
                        distance = math.sqrt((thumb[0] - index[0])**2 + (thumb[1] - index[1])**2)
                        if distance < click_threshold:
                            if not left_click_pressed:
                                pyautogui.mouseDown(button='left')
                                left_click_pressed = True
                        else:
                            if left_click_pressed:
                                pyautogui.mouseUp(button='left')
                                left_click_pressed = False

                    if thumb and middle:
                        distance = math.sqrt((thumb[0] - middle[0])**2 + (thumb[1] - middle[1])**2)
                        if distance < click_threshold:
                            if not right_click_pressed:
                                pyautogui.mouseDown(button='right')
                                right_click_pressed = True
                        else:
                            if right_click_pressed:
                                pyautogui.mouseUp(button='right')
                                right_click_pressed = False

            cv2.imshow("Hand Tracking", img)
            if cv2.waitKey(1) & 0xFF==27:
                break

        cap.release()
        cv2.destroyAllWindows()
