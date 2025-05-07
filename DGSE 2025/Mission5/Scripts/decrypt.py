import base64
import hashlib
import json
import re
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import requests

def getID(model, brand):
    raw = f"{model}:{brand}"
    hashed = hashlib.sha256(raw.encode("utf-8")).digest()
    device_id = base64.b64encode(hashed).decode()

    return device_id

def derive_key(device_id, salt):
    raw = f"{device_id}:{salt}"
    sha256 = hashlib.sha256(raw.encode("utf-8")).digest()
    return sha256

def getMessages(ID):
    response = requests.get(f"http://163.172.67.201:8000/messages?id={ID}")
    # Output example :
    # {"messages":[{"content":"M2geCVKOzPlyug9p9DvthxPip0oe9BPiT2sDfFhWy7iC3+JQI4SfO7+SLAlFSUmu8LoGj1hrUWil/uNXvc+5mKBMrRNFQT8ijBK14P0Z8qA=","isEncrypted":true,"sender":"Agent-02","timestamp":"2025-04-01 08:00:00"},{"content":"//5PBsYWhHlgqhVgG1omUyevzmlErLZVsTCLO78Rbb9qBMPnsKCS5/RZ4GEdWRBPiZ4BtO5h7j2PuIutfqf7ag==","isEncrypted":true,"sender":"Agent-1337","timestamp":"2025-04-01 10:00:00"},{"content":"2uNMSnJZa5JExhYgNA+V3RAiafhuLkj8Jnr4U+lSZOrrpMWjyA13w0Do3IIPcVBgK070rmweRKX/GkCAxat4i3JfWk1UvWNSmEZbHQlFznR7VFW6FKK84iJKhiDOp8Tk","isEncrypted":true,"sender":"Agent-01","timestamp":"2025-04-02 15:30:00"},{"content":"Swz/ycaTlv3JM9iKJHaY+f1SRyKvfQ5miG6I0/tUb8bvbOO+wyU5hi+bGsmcJD3141FrmrDcBQhtWpYimospymABi3bzvPPi01rPI8pNBq8=","isEncrypted":true,"sender":"Agent-02","timestamp":"2025-04-03 13:20:00"},{"content":"NAe44oieygG7xzLQT3j0vN+0NoPNUu0TAaid9Az3IlpcKwR0lSKaPT8F4y1zpbArWFIGpgzsPZtPAwL50qocTRMG/g5u+/wcc1nxmhBjCbg=","isEncrypted":true,"sender":"Agent-04","timestamp":"2025-04-04 08:30:00"},{"content":"dfeKlZP/gIntHySBYine2YUlNiX3LjlMOLu7y9tgprFyJIIcQpfghlQXut6cJUG2wtzGBVQUm7ITdpLNeVaZjamQHhPWEtNIJE/xtFg66Klui1qCKYKSrmZ4wm1CG/ZPy4csqbM28Ur8dts7XoV5FA==","isEncrypted":true,"sender":"Agent-04","timestamp":"2025-04-05 16:45:00"},{"content":"LjduJj9pfygHrVedwQIeXVBSMlT2wFe5tpavdDZN+kX61zI5qP4dl3jOljIReGyqR4dY8X7pSWm/ZHF0Tz3rM73COU6GTq9igI3m02s8H7LUKXRpVbyXATs5mei3DktV","isEncrypted":true,"sender":"Agent-03","timestamp":"2025-04-06 11:15:00"},{"content":"6mvFVrB3yEBGB4XD8dbFXOWGM4hErsA4j+B/NWM2nLOosWW/ECbmCqTTdlnZzQVq6hVYMIVoKwIDarF3DXCFid6Ng0uoC4UQF+l4xOnuUu4=","isEncrypted":true,"sender":"Agent-01","timestamp":"2025-04-06 14:20:00"},{"content":"OqKg5kGfvREPheoYGDUfWw42lSlwsviyXtiFrS1e878hWBGiJa1cdscvzo0FsDU+PHlnE1lkR5o4I5FhiOJ7OuPqjPSXWxKynrbgXIwZHZgDDq/HWJSxRFnhOU0Wi/n1","isEncrypted":true,"sender":"Agent-00","timestamp":"2025-04-07 09:00:00"}]}
    if response.status_code != 200:
        print("[-] Error while fetching.")
        exit(1)

    messages = response.json().get("messages", [])
    return [(msg["sender"], msg["content"], msg["timestamp"]) for msg in messages]

STATIC_IV = base64.b64decode("LJo+0sanl6E3cvCHCRwyIg==")
STATIC_SALT = "s3cr3t_s@lt"

# From https://github.com/androidtrackers/certified-android-devices
with open("google_model_brand.json", "r", encoding="utf-8") as f:
    devices = json.load(f)

messages = getMessages(getID("Pixel 9", "google"))
for device in devices:
    model, brand = device["model"], device["brand"]
    device_id = getID(model, brand)
    key = derive_key(device_id, STATIC_SALT)

    for sender, message, timestamp in messages:
        cipher = AES.new(key, AES.MODE_CBC, STATIC_IV)
        ciphertext = base64.b64decode(message)
        try:
            plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
            print(f"\033[0;32m[+] Message from {sender} at {timestamp} decrypt with {model} - {brand}: {plaintext.decode()}\033[0m")
        except Exception as e:
            continue
