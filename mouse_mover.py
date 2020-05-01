import pyautogui as pgui
import msvcrt

while True:
  pgui.moveRel(1000, 0, duration=1)
  pgui.moveRel(-1000, 0, duration=1)
  if msvcrt.kbhit():
    break
