from scapy.all import rdpcap, ICMP, IP
from Crypto.Cipher import AES

__key = bytes.fromhex("e8f93d68b1c2d4e9f7a36b5c8d0f1e2a")
__iv = bytes.fromhex("1f2d3c4b5a69788766554433221100ff")

def pkcs7_unpad(x):
    return x[:-x[-1]]

def decrypt_hex_string(hex_str, chunk=16):
    cipher = AES.new(__key, AES.MODE_CBC, __iv)
    data = bytes.fromhex(hex_str)[:chunk]
    decrypted = cipher.decrypt(data)
    return pkcs7_unpad(decrypted).decode()

packets = rdpcap("capture_victim.pcap")

for pkt in packets:
    if IP in pkt and ICMP in pkt:
        if pkt[ICMP].type == 8:
            payload = bytes(pkt[ICMP].payload)[16:]
            print(f"{decrypt_hex_string(payload.hex())}")
