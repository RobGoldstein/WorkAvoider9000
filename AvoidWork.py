import pyautogui
import time
import random


def gen_points():
    x = random.randint(300, 1000)
    y = random.randint(300, 900)
    z = random.randint(10, 120)
    return x, y, z


if __name__ == '__main__':
    while True:
        x, y, z = gen_points()
        time.sleep(z)
        pyautogui.moveTo(x, y)
