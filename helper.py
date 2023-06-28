import pyautogui
import keyboard

while True:
    # keyboard.wait('h')
    # print(pyautogui.position())
    print(pyautogui.locateOnScreen('imgs/regiao.png', confidence=0.8))
