from Crypto.Cipher import AES

k = bytes.fromhex("e8f93d68b1c2d4e9f7a36b5c8d0f1e2a")
v = bytes.fromhex("1f2d3c4b5a69788766554433221100ff")
d = bytes.fromhex("37e0f8f92c71f1c3f047f43c13725ef1")

def unpad(x): return x[:-x[-1]]

c = AES.new(k, AES.MODE_CBC, v)
print(unpad(c.decrypt(d)).decode())