import socket
import base64
import re

url = "challenges.404ctf.fr"
port = 31420

def connection():
    try:
        # Cration du socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connection au serveur
        client.connect((url, port))
        print("[+] Connexion établie\n")
    except:
        # Connection échoué
        print("[-] Connexion non établie")
        sys.exit(0)
    return client

def recup_ennonce(client):
    # Recupere la réponse du serveur
    reception = client.recv(4096)
    return reception

def envoie_reponse(data, client):
    # Ajoute le caractères
    data += "\n"
    client.send(data.encode())

# Main

# Connection au challenge
print("[*] Connection en cours...")
client = connection()

i = 0
while True:
    # Recuperation de l'ennoncé
    recup_1 = recup_ennonce(client)
    recup_2 = recup_ennonce(client)
    recup_1 = recup_1.replace(b'\n', b'')
    recup_2 = recup_2.replace(b'\n', b'')
    recup = recup_1 + recup_2
    print(recup)

    # Comptage du nombre de rinocéros
    nombre_rino = str(recup.count(bytes('~c`°^)', 'utf-8')))
    print(nombre_rino)
    envoie_reponse(nombre_rino, client)
    i += 1