import pyautogui
import time
pyautogui.size()

width, height = pyautogui.size()

pyautogui.position()
print(pyautogui.position())
i = 0
while i < 100:
    #Klik na mape
    pyautogui.click((85, 399))
    pyautogui.hotkey('ctrl',"a")

    pyautogui.hotkey('ctrl',"v")
    pyautogui.click((85, 350))
    #Klik na Find
    pyautogui.click((423, 406))
    time.sleep(1)
    #Klik na Lat
    pyautogui.click((123, 524))
    pyautogui.hotkey('ctrl',"a")
    pyautogui.hotkey('ctrl',"c")
    #Klik na Excel
    pyautogui.click((1433, 21))

    #Pole Lat
    pyautogui.press('right')
    pyautogui.hotkey('ctrl',"v")

    #Klik na long
    pyautogui.click((439, 520))
    pyautogui.hotkey('ctrl',"a")
    pyautogui.hotkey('ctrl',"c")
    #Klik na Excel
    pyautogui.click((1433, 21))

    #Pole Lat
    pyautogui.press('right')
    pyautogui.hotkey('ctrl',"v")

    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.press('down')

    pyautogui.hotkey('ctrl',"c")

    i+=1