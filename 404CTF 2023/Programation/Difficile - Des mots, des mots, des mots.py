import socket
import base64
import math
import re

url = "challenges.404ctf.fr"
port = 30980

def connection():
    #connexion au chall
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((url, port))
        print("[+] Connexion établie\n")
    except:
        print("[-] Connexion non établie")
        sys.exit(0)
    return client

def recup_ennonce(client):
    reception = client.recv(4096)
    recup = reception.decode()
    return recup

def envoie_reponse(data, client):
    data += "\n"
    client.send(data.encode())

def find_sentence(ennonce):
    debut = ennonce.find('{') + 1
    fin = ennonce.find('}', debut)
    return ennonce[debut:fin].strip()

def empty(val):
    return val

def regle_1(val_r1):
    return ''.join(reversed([val_r1[i:i + 1] for i in range(0, len(val_r1), 1)]))

def regle_2(val):
    val_r2 = regle_1(val)

    if len(val_r2) % 2 == 0:
        indice = int(len(val_r2) / 2)
        part_1 = val_r2[0:indice]
        part_2 = val_r2[indice:len(val_r2)]
        val_r2 = part_2 + part_1
        return val_r2
    else:
        indice = math.floor(len(val_r2) / 2)
        char = val_r2[indice]
        return val_r2.replace(char, "")

def regle_3(val_r3):
    if len(val_r3) >= 3:
        if val_r3[2] not in voyelle:
            val_voyelle = ""
            for i in range(len(val_r3)):
                if val_r3[i] not in voyelle:
                    continue
                val_voyelle += val_r3[i]
                indice = val_r3.find(val_r3[i])
                val_r3 = val_r3[:indice] + "$" + val_r3[indice + 1:]

            val_voyelle = val_voyelle[1:] + val_voyelle[:1]
            for char in val_voyelle:
                indice = val_r3.find('$')
                val_r3 = val_r3[:indice] + char + val_r3[indice + 1:]

            return regle_2(val_r3)
        else:
            val_voyelle = ""
            for i in range(len(val_r3)):
                if val_r3[i] not in voyelle:
                    continue
                val_voyelle += val_r3[i]
                indice = val_r3.find(val_r3[i])
                val_r3 = val_r3[:indice] + "$" + val_r3[indice + 1:]

            val_voyelle = val_voyelle[-1:] + val_voyelle[:-1]
            for char in val_voyelle:
                indice = val_r3.find('$')
                val_r3 = val_r3[:indice] + char + val_r3[indice + 1:]

            return regle_2(val_r3)
    else:
        return val_r3

def regle_4(val):
    val_r4 = regle_3(val)

    i = 0
    while i < len(val_r4):
        if val_r4[i].lower() not in voyelle and ord(val_r4[i].lower()) >= 97 and ord(val_r4[i].lower()) <= 122:
            if i != 0:
                vp = last_voy(val_r4[i])
                s = Somme(val_r4, i)
                a = chr(((ord(vp) + int(s)) % 95) + 32)
                val_r4 = val_r4[:i + 1] + a + val_r4[i + 1:]
                i += 1
                continue
            i += 1
            continue
        i += 1
    return tri_occurrences(val_r4)


def tri_occurrences(val):
    occurrences = {}
    for c in val:
        if c in occurrences:
            occurrences[c] += 1
        else:
            occurrences[c] = 1

    sorted_chars = sorted(occurrences.keys(), key=lambda c: (-occurrences[c], ord(c)))

    sorted_val = ""
    for c in sorted_chars:
        sorted_val += c * occurrences[c]

    return sorted_val

def last_voy(lettre):
    if lettre.islower():
        for i in range(ord(lettre), ord('a') - 1, -1):
            if chr(i) in voyelle:
                return chr(i)
    else:
        for i in range(ord(lettre), ord('A') - 1, -1):
            if chr(i).lower() in voyelle:
                return chr(i)

def Somme(val, n):
    s = 0
    for i in range(n - 1, -1, -1):
        s += ord(val[i]) * pow(2, (n - i)) * Id(val[i])
    return s

def Id(ieme_lettre):
    if ieme_lettre.lower() in voyelle:
        return 1
    else:
        return 0

voyelle = ['a', 'e', 'i', 'o', 'u', 'y']
client = connection()
recup_1 = recup_ennonce(client)

val = empty(find_sentence(recup_1))
envoie_reponse(val, client)
val = recup_ennonce(client)

val = regle_1(find_sentence(val))
envoie_reponse(val, client)
val = recup_ennonce(client)

val = regle_2(find_sentence(val))
envoie_reponse(val, client)
val = recup_ennonce(client)

val = regle_3(find_sentence(val))
envoie_reponse(val, client)
val = recup_ennonce(client)

val = regle_4("cosette")
envoie_reponse(val, client)
val = recup_ennonce(client)
print(val)

val_to_decode = find_sentence(val).split()
payload = ""

for decode in val_to_decode:
    payload += regle_4(decode) + " "
print(payload)
envoie_reponse(payload[:-1], client)
flag = recup_ennonce(client)
print(flag)