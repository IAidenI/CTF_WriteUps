import hashlib
import base64

def getID(model, brand):
    raw = f"{model}:{brand}"
    hashed = hashlib.sha256(raw.encode("utf-8")).digest()
    device_id = base64.b64encode(hashed).decode()

    return device_id

model="Pixel 9"
brand="Google"
print(f"{brand} - {model} a pour id : {getID(model, brand)}")
