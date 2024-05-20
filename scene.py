import cv2 as cv
import numpy as np
from font_setup import *
import color_setup as color
import about_game as about
import audio_setup as audio

def exit_from_app():
    cv.destroyAllWindows()
    exit()

def main_menu(frame):
    cv.putText(frame, about.app_title, (100, 200), header_txt["face"], header_txt["scale"], color.white, header_txt["thickness"], header_txt['line_type'])
    cv.putText(frame, "By Mrcl", (230, 230), normal_txt["face"], normal_txt["scale"], color.white, normal_txt["thickness"], normal_txt['line_type'])
    cv.putText(frame, "Type (e) to continue...", (160, 300), normal_txt["face"], normal_txt["scale"], color.white, normal_txt["thickness"], normal_txt['line_type'])
    cv.imshow(about.app_title, frame)
    while True:
        key = cv.waitKey(0)
        if key == -1:
            exit_from_app()
        if key == ord('e') or key == ord('E'):
            break

def select_working_time(frame):
    message = "Type in minute..."
    input = ""
    while True:
        background = frame.copy()
        cv.putText(background, "Set your working time", (20, 200), header_txt["face"], header_txt["scale"], color.white, header_txt["thickness"], header_txt['line_type'])
        cv.putText(background, message, (200, 230), normal_txt["face"], normal_txt["scale"], color.white, normal_txt["thickness"], normal_txt['line_type'])
        cv.putText(background, input, (160, 300), normal_txt["face"], normal_txt["scale"], color.white, normal_txt["thickness"], normal_txt['line_type'])
        cv.imshow(about.app_title, background)
        typed = cv.waitKey(0)
        try:    
            if typed == ord('\r') and input != "0" and input != "": # Enter
                break
            elif typed == 8:
                input = input[:-1]
                print(input)
            elif (int(chr(typed)) == 0) and input == "":
                pass
            elif int(chr(typed)) < 10 and int(chr(typed)) >= 0:
                input = input + str(chr(typed))
            
        except:
            pass
    return int(input)

def select_breaking_time(frame):
    message = "Type in minute..."
    input = ""
    while True:
        cv.putText(frame, "Set your breaking time", (20, 200), header_txt["face"], 1.4, color.white, header_txt["thickness"], header_txt['line_type'])
        cv.putText(frame, message, (200, 230), normal_txt["face"], normal_txt["scale"], color.white, normal_txt["thickness"], normal_txt['line_type'])
        cv.putText(frame, input, (160, 300), normal_txt["face"], normal_txt["scale"], color.white, normal_txt["thickness"], normal_txt['line_type'])
        cv.imshow(about.app_title, frame)
        typed = cv.waitKey(0)
        try:    
            if typed == ord('\r') and input != "0" and input != "": # Enter
                break
            elif typed == 8:
                input = input[:-1]
                print(input)
            elif (int(chr(typed)) == 0) and input == "":
                pass
            elif int(chr(typed)) < 10 and int(chr(typed)) >= 0:
                input = input + str(chr(typed))
            
        except:
            pass
    return int(input)

def working_time(frame, working_time, time_is_running):
    minute, working_time = working_time, working_time * 60
    second = 0
    while True:
        background = frame.copy()
        cv.putText(background, "Working Time", (125, 200), header_txt["face"], header_txt['scale'], color.white, header_txt["thickness"], header_txt['line_type'])
        cv.putText(background, str(minute) + " : " + str(second), (220, 260), header_txt["face"], header_txt['scale'], color.white, header_txt["thickness"], header_txt['line_type'])
        cv.imshow(about.app_title, background)

        if minute == 0 and second == 0:
            time_is_running = True
            break

        second -= 1
        if second < 0:
            minute -= 1
            second = 59

        # EVENT ---------------
        key = cv.waitKey(1000)
        if key == ord('q') or key == ord('Q'):
            time_is_running = False
            cv.destroyWindow(about.app_title)
            break
        elif key == ord('n'):
            break
    return time_is_running

def break_time(frame, break_time, time_is_running):
    minute, break_time = break_time, break_time * 60
    second = 0
    while True:
        background = frame.copy()
        cv.putText(background, "Breaking Time", (115, 200), header_txt["face"], header_txt['scale'], color.white, header_txt["thickness"], header_txt['line_type'])
        cv.putText(background, str(minute) + " : " + str(second), (220, 260), header_txt["face"], header_txt['scale'], color.white, header_txt["thickness"], header_txt['line_type'])
        cv.imshow(about.app_title, background)

        if minute == 0 and second == 0:
            time_is_running = True
            break

        second -= 1
        if second < 0:
            minute -= 1
            second = 59

        # EVENT ---------------
        key = cv.waitKey(1000)
        if key == ord('q') or key == ord('Q'):
            time_is_running = False
            cv.destroyWindow(about.app_title)
            break
        elif key == ord('n'):
            break

    return time_is_running

def alarm(frame):
    audio.alarm.play(-1)
    cv.putText(frame, "Alarm on!", (165, 200), header_txt["face"], header_txt['scale'], color.white, header_txt["thickness"], header_txt['line_type'])
    cv.putText(frame, "Click (N) to start...", (175, 260), normal_txt["face"], normal_txt["scale"], color.white, normal_txt["thickness"], normal_txt['line_type'])
    cv.imshow(about.app_title, frame)
    while True:
        key = cv.waitKey(0)
        if key == ord('q') or key == ord('Q'):
            time_is_running = False
            cv.destroyWindow(about.app_title)
            break
        elif key == ord('n') or key == ord('N'):
            audio.alarm.stop()
            break