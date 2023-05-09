# Challenge intro Reverse
cipher = "JQHGY{Qbs_x1x_S0o_f00E_b3l3???y65zx03}"
flag = ""


for char in cipher:
    if char.islower():
        flag += chr((ord(char) + 0xa9) % 0x1a + ord('a'))
    elif char.isupper():
        flag += chr((ord(char) + 0x2d) % 0x1a + ord('A'))
    else:
        flag += char
print(f"Le flag est : {flag}")