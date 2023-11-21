import pyautogui
from time import sleep


rows = int(input())
sleep(4)
for i in range(0, rows+1):
    pyautogui.write('#' * i)
    pyautogui.press('enter')