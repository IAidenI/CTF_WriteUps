## Challenge “What Are You Doing In My Swamp” 209 résolutions :

**Ennoncé :**
>This challenge is like ogres, it has layers


Nous avons accès à un fichier `layers.jpg` mais il semble être corrompu. Avec une recherche internet, on tombe rapidement sur [recovery jpg](https://www.file-recovery.com/jpg-signature-format.htm). On suit donc les indications et on obtient cela :

<img src="./src/images/forensic_easy_1.jpg"/>

On y voit marquer Atbash Cipher mais à part cela rien de spécial. On va donc utiliser [stegseek](https://github.com/RickdeJager/stegseek) pour voir s'il ne contient pas de données cachées. On exécute donc cette commande :

<img src="./src/images/forensic_easy_2.png"/>


L'outil a bien trouver des données cachées que voici

<img src="./src/images/forensic_easy_3.png"/>

On y voit un semblant de flag. On se rappelle ce qui était marqué sur l'image, Atbash Cipher. On se rend donc sur ce site [decode](https://www.dcode.fr/chiffre-atbash) pour obtenir le flag.

<img src="./src/images/forensic_easy_4.png"/>
