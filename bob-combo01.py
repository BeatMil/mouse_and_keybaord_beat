import time
import keyboard as kb

def flash_punch():
    kb.press("u")
    time.sleep(0.1)
    kb.release("u")
    kb.press("i")
    time.sleep(0.4)
    kb.press("u")   
    time.sleep(0.1)
    kb.release("u,i")

def hopkick():
    # kb.press("w+d+j")
    # kb.release("w+d+j")
    kb.press('w+d+j')
    time.sleep(0.03)
    kb.release('w,d,j')

def dash_attack():
    kb.press('d')
    time.sleep(0.03)
    kb.release('d')

    time.sleep(0.1)

    kb.press('d')
    time.sleep(0.03)

    time.sleep(0.1)

    kb.press('i')
    time.sleep(0.03)
    kb.release('d')
    kb.release('i')

time.sleep(5)
hopkick()
time.sleep(0.9)
flash_punch()
time.sleep(0.7)
dash_attack()


