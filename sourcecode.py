import pyautogui
import time
import keyboard

print('importing done')


hotkey = input("Which key should be set as a hotkey? : ")
delay = float(input('enter the delay you want to be in between clicks  70Milliseconds minimum 3+ recomended : '))
print('to stop this program you can just press control+c when in focus')

while True:
    if keyboard.is_pressed(hotkey) == True:
        print('Reset operation initiated')
        pyautogui.press('Esc')
        pyautogui.click(pyautogui.locateCenterOnScreen('quit.jpg'))
        time.sleep(delay)
        pyautogui.click(pyautogui.locateCenterOnScreen('singleplayer.jpg'))
        time.sleep(delay)
        pyautogui.click(pyautogui.locateCenterOnScreen('create1.png'))
        time.sleep(delay)
        pyautogui.click(pyautogui.locateCenterOnScreen('create2.jpg'))




