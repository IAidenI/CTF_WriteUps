## Challenge “L'Académie du détail” 360 résolutions :

**Ennoncé :**
>Author: seaweedbrain#1321
>
>Le nez plongé dans votre café noir, vous parcourez d'un rapide coup d'œil la une du journal fraichement paru. L'un des titres vous interpelle :
>
>Mars 1980 : L'opaque secret du nouveau membre de l'Académie Française.
>Vous parcourez alors le journal à la recherche de l'article en question. Il énonce :
>
>Après des heures de délibération, les Académiciens ont enfin voté pour le nouveau membre de la grande Académie Française. Mais pour des raisons que tout le monde ignore, son nom demeure secret depuis ce jour. Malgré tous leurs efforts, aucun journaliste n'a réussi a obtenir le moindre indice ou la moindre image.
>Interloqué, vous vous rendez compte que l'Académie Française possède un site web. Peut être que la réponse est finalement à portée de tous, voir même plus ... !
>
>Toutes les informations nécéssaires à la résolution de ce challenge sont présentes dans l'énoncé ci-dessus.
>Le flag est au format classique 404CTF{}. Vous devez le trouver, il ne peut pas être deviné.
>
>Connection au challenge : https://academie.challenges.404ctf.fr/


### Analyse du site

Tout d'abord, accédons au site internet.

<img src="./src/images/web_easy_1.png"/>
<img src="./src/images/web_easy_2.png"/>

Une chose attire tout de suite l'oeil. Le boutton s'identifier.

<img src="./src/images/web_easy_3.png"/>

Tout d'abord on essaie `admin` & `admin` (on sait jamais), mais non concluant. On peut aussi rapidement essaye quelques **injection sql** du genre `admin' --`, mais rien de productif non plus.
Bon essayons de mettre `test` & `test`.

<img src="./src/images/web_easy_4.png"/>

Nous sommes bien connecté en tant que `test`. On peut voir à présent un autre boutton intéressant. Liste des membres. Car petit rappel, on cherche ici le nom du nouveau membre qui n'est pas accesible au publique. Si on se rend sur cette page, on obtient rien de concluant.

<img src="./src/images/web_easy_5.png"/>

### Test de vulnérabilité

Si on va faire un tour du coté des **cookies**, on voit que nous avons un cookie de session. Allons décortiquer ce token sur https://jwt.io

<img src="./src/images/web_easy_6.png"/>

On a donc plusieurs parties sur ce token. Le Header, le Payload, et la vérification de la signature. Un Json Token doit être chiffré par un algorithme, ici HS256, pour être sécurisé. Nous pouvons donc essayer un **brute force** avec un dictionnaire pour retrouver le secret utiliser et donc crafter un token.
Personelement je vais utiliser `hashcat` mais on peut très bien le faire avec `jtr`. Je rentre donc la commande suivante : `hashcat token.txt -m 16500 -a 0 /usr/share/wordlists/rockyou.txt`

<img src="./src/images/web_easy_7.png"/>

Malheureusement, il n'as rien trouver. Avant d'essayer plein de wordlist différente en espérant trouver le bon secret essayons autre chose.

### Exploitation de la faille

En effet, il existe une vulnérabilité assez connue sur des **JWT**. Elle est généralement dû à une mauvaise configuration. Parfois, si l'en-tête indique que l'algorithme est défini sur "none", certains serveurs peuvent ignorer cette information et considérer le JWT comme valide, sans vérifier la signature.
Très bien, on se rend sur https://www.base64encode.org/ pour changer {"alg":"HS256","typ":"JWT"} par {"alg":"none","typ":"JWT"}.
Nous obtenons alors eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0. On vient le remplacer dans le token, on obtient donc eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjg2MDc3MDgyfQ.oI4koW9o0t1XftXnVZRnNVIEw6WOfBO4WWoVtztRyNM (en ayant pris soin de changer `test` par `admin` bien évidament).
On viens juste changer notre token par celui ci et on recharge la page.

<img src="./src/images/web_easy_8.png"/>