import os
import cv2 as cv
import numpy as np
import scene

path = os.getcwd()

def refreshFrame(color = (0,0,0)):
    global frame
    frame = background.copy()

    # set color
    frame[:, :, 0] = color[0]
    frame[:, :, 0] = color[1]
    frame[:, :, 0] = color[2]

# initialize frame
background = np.ones((550, 550, 3)).astype(np.uint8)
frame = background.copy()
refreshFrame()

# Screen Resolution
HEIGHT, WIDTH = background.shape[:2]

# Main Menu
scene.main_menu(frame)
refreshFrame()

# set working time
working_time = scene.select_working_time(frame)
refreshFrame()


# set break time
break_time = scene.select_breaking_time(frame)
refreshFrame()

# Time is running now!
time_is_running = True
while time_is_running:
    time_is_running = scene.working_time(frame, working_time, time_is_running)
    refreshFrame()

    if not time_is_running: break

    scene.alarm(frame)
    refreshFrame()

    if not time_is_running: break
    
    time_is_running = scene.break_time(frame, break_time, time_is_running)
    refreshFrame()

    if not time_is_running: break

    scene.alarm(frame)
    refreshFrame()

    if not time_is_running: break

"""
RENCANA
BuaT agar setelah periode kerja tertentu, jeda istirahat dibuat lebih lama
"""

cv.destroyAllWindows()