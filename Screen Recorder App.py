import time

import cv2          # helps save the captured images in a video format.
import numpy as np  # helps convert images captured into an array and pass it onto openCV.
import pyautogui    # to capture images on the screen
import time

''' note: a codec is the language in which the computer should make a file into an output video.
    fourcc is a 4 character code used to compress the frames (i.e. the language) such as XVID, MJPEG, WMV1, WMV2, etc.
    function VideoWriter takes parameters (filename,fourcc,fps,frame_size) '''

def minimize():
    import win32gui
    import win32con
    from os import mkdir    # imports directory so we can save recording

    window = win32gui.FindWindow(None,"Screen recorder")
    win32gui.ShowWindow(window,win32con.SW_MINIMIZE)

minimized = False    # this means it's currently not minimized
#=========================================================
# set the screen resolution, get it from your OS settings
#=========================================================
SCREEN_SIZE = (pyautogui.size())
#=========================================================
# creating the VideoWriter object
#=========================================================
# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# create the video write object
t = time.strftime("%d-%m-%y %H-%M-%S")
# note 20 is our fps value that we set.
output = cv2.VideoWriter("C://Users\Aimee\Documents//C - 2nd Year Uni//PERSONAL CODING PROJECTS//Python Projects//Project 2 - Screen Recorder App//recordings//rec "+t+".avi",fourcc,20,(SCREEN_SIZE))
# activate the webcam and capture from it.
webcam = cv2.VideoCapture(0)
print("Recording started.\nwindow is minimized in taskbar\nPress z to exit.")
#=========================================================
# a while loop to keep capturing the screen and writing it to the file until letter z is pressed on the keyboard.
#=========================================================
while True:
    # make a screenshot
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array so it can work with OpenCV
    img = np.array(img)
    # convert colours from BGR to RGB
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # show the frame
    cv2.imshow("Screen recorder",frame) # Screen recorder is my window's name

    if minimized != True:
        minimized = True
        minimize()          # this will only minimize the window once.

    # write the frame
    output.write(frame)
    # if the user presses z, it exits
    if cv2.waitKey(1) == ord("z"):
        print("\rRecording finished.")
        break

# making sure everything is closed when exited
output.release()
cv2.destroyAllWindows()