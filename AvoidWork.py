import pyautogui
import time
import random


def gen_points():
    x = random.randint(300, 1000)
    y = random.randint(300, 900)
    return x, y


if __name__ == '__main__':
    while True:
        time.sleep(300)
        x, y = gen_points()
        pyautogui.moveTo(x, y)
