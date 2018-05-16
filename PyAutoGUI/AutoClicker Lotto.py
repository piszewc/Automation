import pyautogui
import time

pyautogui.size()

width, height = pyautogui.size()

pyautogui.position()
print(pyautogui.position())
i = 0
while i < 10:
    # Take Copy
    pyautogui.click((1419, 17))
    pyautogui.hotkey('ctrl', "c")
    pyautogui.click((385, 66))
    pyautogui.dragTo(459, 66, 0.2, button='left')
    pyautogui.press('delete')
    pyautogui.hotkey('ctrl', "v")
    pyautogui.press('enter')
    time.sleep(1)

    # Ilosc
    pyautogui.click((203, 899))
    pyautogui.dragTo(268, 898, 0.2, button='left')
    pyautogui.hotkey('ctrl', "c")
    pyautogui.click((1419, 17))
    pyautogui.press('right')
    pyautogui.hotkey('ctrl', "v")

    pyautogui.click((203, 922))
    pyautogui.dragTo(268, 922, 0.2, button='left')
    pyautogui.hotkey('ctrl', "c")
    pyautogui.click((1419, 17))
    pyautogui.press('right')
    pyautogui.hotkey('ctrl', "v")

    pyautogui.click((203, 947))
    pyautogui.dragTo(268, 947, 0.2, button='left')
    pyautogui.hotkey('ctrl', "c")
    pyautogui.click((1419, 17))
    pyautogui.press('right')
    pyautogui.hotkey('ctrl', "v")

    pyautogui.click((203, 972))
    pyautogui.dragTo(268, 972, 0.2, button='left')
    pyautogui.hotkey('ctrl', "c")
    pyautogui.click((1419, 17))
    pyautogui.press('right')
    pyautogui.hotkey('ctrl', "v")

    # Kwota


    pyautogui.click((284, 899))
    pyautogui.dragTo(373, 898, 0.2, button='left')
    pyautogui.hotkey('ctrl', "c")
    pyautogui.click((1419, 17))
    pyautogui.press('right')
    pyautogui.hotkey('ctrl', "v")

    pyautogui.click((284, 922))
    pyautogui.dragTo(373, 922, 0.2, button='left')
    pyautogui.hotkey('ctrl', "c")
    pyautogui.click((1419, 17))
    pyautogui.press('right')
    pyautogui.hotkey('ctrl', "v")

    pyautogui.click((284, 947))
    pyautogui.dragTo(373, 947, 0.2, button='left')
    pyautogui.hotkey('ctrl', "c")
    pyautogui.click((1419, 17))
    pyautogui.press('right')
    pyautogui.hotkey('ctrl', "v")

    pyautogui.click((284, 972))
    pyautogui.dragTo(373, 972, 0.2, button='left')
    pyautogui.hotkey('ctrl', "c")
    pyautogui.click((1419, 17))
    pyautogui.press('right')
    pyautogui.hotkey('ctrl', "v")

    pyautogui.hotkey('ctrl', 'left')
    pyautogui.press('down')

    i += 1