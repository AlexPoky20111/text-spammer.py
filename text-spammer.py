import pyautogui
import time

a=int(input('how many message: '))

b=input('type your messsage: ')

time.sleep(5)

for i in range(a):
    pyautogui.write(b)
    pyautogui.press('enter')
print('Done')    