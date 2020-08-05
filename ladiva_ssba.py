import time
import keyboard as kb


def press(button):
    kb.press(button)
    time.sleep(0.01)
    kb.release(button)


def spd():
    press("d")
    press("s")
    press("a")
    press("w+i")


def ssba():
    press("d")
    press("s")
    press("a")
    press("w")
    press("d")
    press("s")
    press("a")
    press("w+j")

time.sleep(2)
ssba()