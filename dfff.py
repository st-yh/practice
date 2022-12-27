from datetime import datetime
import pyautogui
now = datetime.now()

pyautogui.mouseInfo()
print(pyautogui.getActiveWindow())
print(now.time())
print(now.hour)
print(type(now.minute))

pyautogui.click(980, 430)

while True:
    pyautogui.press('enter')
    now = datetime.now()
    if 23 == now.hour and 59==now.minute:
        print('dfff')


        break