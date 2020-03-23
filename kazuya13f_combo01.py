import time
import keyboard as kb

def press(button):
    kb.press(button)
    time.sleep(0.03)
    kb.release(button)

def pewgf():
    press('d')   # already release itself 
    time.sleep(0.03)
    kb.press('s+d+i')
    time.sleep(0.03)
    kb.release('s,d,i')
#0.712 & 0.713
#0.717
#0.713!!
#!!---0.714---!!
time.sleep(1.5)
press('s+d+i') #hook punch
time.sleep(0.714)
pewgf()
