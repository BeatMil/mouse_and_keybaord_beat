import keyboard as kb
from time import sleep
text_array = []
text = input("TYPE_FAST: ")
sleep(1)
text_split = text.split()
for i in text_split:
	kb.write("%s "%i)
	sleep(0.01)
