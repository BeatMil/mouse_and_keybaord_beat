import pyautogui as pg
import time

"""
This code will open Paint and draw a square
only works on window 555
"""

x = 100
y = 20

time.sleep(1)
pg.click(20,1200)
pg.typewrite("paint")
pg.hotkey("return")
pg.moveTo(220,500,1)
# pg.click()
# pg.time.sleep(0.5)
# pg.click()
pg.dragRel(200,000,1)
pg.dragRel(0,-200,1)
pg.dragRel(-200,000,1)
pg.dragRel(0,200,1)
# pg.scroll(1000)
# print(pg.position())
# pg.moveRel(500,0,0.5)
# print(pg.position())
# # pg.moveTo(x,y,0.5)
# pg.click(x,y)
# print(pg.position())