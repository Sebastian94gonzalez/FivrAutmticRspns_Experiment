import pyautogui

def windowsSec(key):
    # Type PIN
    pyautogui.typewrite(str(key))
    # Press enter
    pyautogui.press('enter')


pyautgui_Script.windowsSec(os.getenv('PASSKEY'))
    