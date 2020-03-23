import keyboard as kb
import time

# time.sleep(1)
# kb.wait("esc") # holy damn!! This is like a real macro!!
# kb.write("hearing of a telescope built by a Dutch eyeglass maker, Italian scientist Galileo Galilei put together his own version,")
# Record events until 'esc' is pressed.
recorded = kb.record(until='esc')
# Then replay back at three times the speed.
kb.play(recorded, speed_factor=3)