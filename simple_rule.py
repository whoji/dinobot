# based on Ashwin Dhakai's script
# https://github.com/Ashwin-Dhakal/AI-for-Chrome-Dinosaur-Game

from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class coordinates:
    replay_btn = (425, 400) #(341,415)
    dino_head =  (175, 400) #162,423)


def restart():
    pyautogui.click(coordinates.replay_btn)
    pyautogui.keyDown('down')

def jump():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("       it jumped  hurray")
    time.sleep(0.18)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def Grab():
    im = ImageGrab.grab(bbox=(175+50+50,400,175+2 50,425))
    # im.show();time.sleep(2)
    # im = ImageOps.grayscale(im)
    imc = array(im.getcolors())
    a = get_avg_color(imc)
    print(a)
    return a

def get_avg_color(imc):
    sum_c = 0.0
    for c in imc:
        sum_c += c[0] * sum(c[1][:-1]) / 3
    return sum_c / sum([c[0] for c in imc])

def get_base_color():
    im = ImageGrab.grab(bbox=(175+50+50,400,175+250,425))
    imc = array(im.getcolors())
    base_color = get_avg_color(imc)
    return base_color

def main():
    time.sleep(3)
    restart()
    time.sleep(0.1)
    base_color_sum = get_base_color()
    while True:
        if Grab() < base_color_sum:
            jump()

main()

