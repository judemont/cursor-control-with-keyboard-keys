from pynput import keyboard
import pyautogui
import threading
import sys

if len(sys.argv) > 2:
    if(sys.argv[1] == "--help" or sys.argv[1] == "-h"):
        print("Usage: python3 main.py [SENSIBILITY] \n Default sensitivity is 30")
    else:
        SENSIBILITY = int(sys.argv[1])

else:
    SENSIBILITY = 30


def move_cursor(key):
    if key == keyboard.Key.up:
        pyautogui.moveRel(0, -SENSIBILITY)
    elif key == keyboard.Key.down:
        pyautogui.moveRel(0, SENSIBILITY)
    elif key == keyboard.Key.left:
        pyautogui.moveRel(-SENSIBILITY, 0)
    elif key == keyboard.Key.right:
        pyautogui.moveRel(SENSIBILITY, 0)
    elif key == keyboard.Key.space:
        pyautogui.click()
        print("space")

def on_press(key):
    t = threading.Thread(target=move_cursor, args=(key,))
    t.start()



with keyboard.Listener(on_press=on_press) as listener:
     listener.join()
