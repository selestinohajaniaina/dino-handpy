import cv2
import mediapipe as mp
import pyautogui

mp_draw = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
video = cv2.VideoCapture(0)

def toucher_space():
    pyautogui.keyDown('space')
    print("espace pressser")
    pyautogui.keyUp('space')
    print('espace lacher')

with mp_hand.Hands(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as hands:
    while True:
        ret, image = video.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if(results.multi_hand_landmarks):
            for hand_landmarks in results.multi_hand_landmarks:
                # mp_draw.draw_landmarks(image, hand_landmarks, mp_hand.HAND_CONNECTIONS)
                akimbe_x = hand_landmarks.landmark[4].x
                akimbe_y = hand_landmarks.landmark[4].y
                tondro_x = hand_landmarks.landmark[8].x
                tondro_y = hand_landmarks.landmark[8].y
                decalage = 0.1
                # if akimbe_x <= tondro_x + decalage and tondro_x <= akimbe_x + decalage and akimbe_y <= tondro_y + decalage and tondro_y <= akimbe_y - decalage :
                print('tondro_x=',tondro_x, 'akimbe_x=',akimbe_x)
                if akimbe_x <= tondro_x + decalage and tondro_x <= akimbe_x + decalage :
                    toucher_space()

        cv2.imshow('Frame', image)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break


video.release()
cv2.destroyAllWindow()