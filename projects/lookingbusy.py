import pyautogui, time

try:
    while True:
        pyautogui.move(123,11, 0.75)
        pyautogui.move(-123, 0, 0.75)
        time.sleep(10)
except KeyboardInterrupt:
    print("Quit!")