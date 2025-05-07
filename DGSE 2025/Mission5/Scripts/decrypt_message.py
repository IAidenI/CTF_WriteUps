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
    if response.status_code != 200:
        print("[-] Error while fetching.")
        exit(1)

    messages = response.json().get("messages", [])
    return [(msg["sender"], msg["content"], msg["timestamp"]) for msg in messages]

STATIC_IV = base64.b64decode("LJo+0sanl6E3cvCHCRwyIg==")
STATIC_SALT = "s3cr3t_s@lt"

model = "Pixel 9"
brand = "Google"

device_id = getID(model, brand)
key = derive_key(device_id, STATIC_SALT)

messages = getMessages(device_id)

for sender, message, timestamp in messages:
    cipher = AES.new(key, AES.MODE_CBC, STATIC_IV)
    ciphertext = base64.b64decode(message)
    try:
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
        print(f"\033[0;32m[+] Message from {sender} at {timestamp} decrypt with {model} - {brand}: {plaintext.decode()}\033[0m")
    except Exception as e:
        continue


