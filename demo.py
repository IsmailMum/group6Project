
import cv2
from gaze_tracking import GazeTracking
from pynput.keyboard import Key, Controller

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    keyboard = Controller()
    if gaze.is_blinking():
    	#key = "b"
    	#keyboard.press(key)
    	#keyboard.release(key)
    	text = "Blinking"
    elif gaze.is_right():
        key = "r"
        keyboard.press(key)
        keyboard.release(key)
        text = "Looking right"
    elif gaze.is_left():
        key = "l"
        keyboard.press(key)
        keyboard.release(key)
        text = "Looking left"
    elif gaze.is_center():
        #key = "c"
        #keyboard.press(key)
        #keyboard.release(key)
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
