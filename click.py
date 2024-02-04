from pynput import keyboard
import threading
import time
import pyautogui

class AutoClicker:
    def __init__(self):
        self.thread = None
        self.stop_flag = threading.Event()

    def auto_click(self):
        while not self.stop_flag.is_set():
            # Get the current mouse position
            x, y = pyautogui.position()

            # Perform a mouse click at the current position
            pyautogui.click(x, y)
            
            # Wait for 2 seconds before the next click
            time.sleep(2)

    def start_auto_click_thread(self):
        self.stop_flag.clear()
        self.thread = threading.Thread(target=self.auto_click)
        self.thread.start()

    def stop_auto_click_thread(self):
        self.stop_flag.set()
        self.thread.join()

auto_clicker = AutoClicker()

def on_press(key):
    try:
        if key.char == 'x':
            print('auto click started')
            auto_clicker.start_auto_click_thread()
    except AttributeError:
        if key == keyboard.Key.esc:
            print('auto click stopped')
            auto_clicker.stop_auto_click_thread()

def on_release(key):
    pass

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
