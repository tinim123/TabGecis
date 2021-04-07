import pyautogui
import time
import msvcrt


time.sleep(1);
pyautogui.hotkey('alt','tab');
time.sleep(2);

while 1:
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(2)


