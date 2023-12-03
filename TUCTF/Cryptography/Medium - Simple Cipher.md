## Challenge “Table Encryption” XXX résolutions :

**Ennoncé :**
>You can't crack my file! I am the exclusive owner of the encryption key!


Nous avons accès un fichier `table_encryption.xml.enc` et c'est à peu près tout. La seul information que l'on a est que le fichier de base est un fichier `.xml`. Avec une recherche internet on remarque que ce genre de fichier commencé très souvent avec cette entête : `<?xml version="1.0" encoding="UTF-8"?>`.
Mais cela ne nous avance pas sur la manière dont il a été chiffré. J'ai donc émis une hypothèse. Très souvant dans les challenges de cryptographie, les **XOR** est utilisé pour chiffrer des donnée et assez facilement retrouver le message en clair (car A XOR B = C <=> A XOR C = B).
Etant donné que nous connaisons le cipher text et une partie du plain text, j'ai fait un **XOR** entre cex deux valeur, dans un premier temps manuellement. Et j'ai pu observer que la clé commencais "Emoji ". Il i a donc de forte chances pour que mon hypothèse soit correcte. J'ai donc fait un algorithme pour trouver ma clé :

<img src="./src/images/table_encryption_easy_1.png"/>


Lorsqu'on l'exécute, on obtient :
`[*] Search the key...
[+] Key found : Emoji Moring Sta`

La clé utilisé est donc Emoji Moring Sta. J'ai donc juste à continuer mon code et qui va venir faire un **XOR** entre le fichier crypter et la clé.

<img src="./src/images/table_encryption_easy_2.png"/>

Nous avons donc à présent le fichier déchiffré qui contient le flag.

<img src="./src/images/table_encryption_easy_3.png"/>
