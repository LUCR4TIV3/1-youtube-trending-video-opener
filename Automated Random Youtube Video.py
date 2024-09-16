import pyautogui
import time

pyautogui.press("win")
time.sleep(1)
pyautogui.write("Microsoft Edge")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)

pyautogui.hotkey('alt', 'space')
time.sleep(1)
pyautogui.press('x')

pyautogui.hotkey('ctrl', 'l')
time.sleep(2)


pyautogui.write("https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl")
pyautogui.press("enter")


x = 658
y = 331

time.sleep(3)
pyautogui.click(x, y)