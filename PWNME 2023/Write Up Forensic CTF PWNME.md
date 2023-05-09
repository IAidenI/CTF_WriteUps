<p align="center">
  <img src="./src/images/forensic/forensic.png"/>
</p>

## Challenge kNOCk kNOC 198 résolutions :


**Ennoncé :**
>Author: Braguette#0169
>
>We have to monitor our network every day to make sure our admins don't help players get out of the game. We are sending you a suspicious capture. Do your job !



### Analyse du fichier

On vient télécharger le fichier **“kNOCk kNOCk”** qui s'avère être un .pcapng. C’est donc un fichier contenant un scan réseau.

Pour pouvoir le lire, je l’ouvre avec **Wireshark** et j'obtiens énormément de données :

<img src="./src/images/forensic/forensic_Intro_1.png"/>

Comme à chaque fois, la première étape est l'application d’un filtre. Ici je commence avec un filtre **http**.

<img src="./src/images/forensic/forensic_Intro_2.png"/>

Les données sont nettement moins importantes à analyser. Je viens à présent suivre le **flux http** et j'obtiens ceci :

<img src="./src/images/forensic/forensic_Intro_3.png"/>



#### Extraction du document transmis

On y voit clairement qu’un client a envoyé une requête **HTTP GET** pour récupérer un fichier nommé, **“MalPack.deb”**. Le serveur est en “200 OK”, et envoie donc le fichier.
Afin de nous aussi récupérer ce fichier, je vais faire `Fichier → Exporter Objets → http`.
Je viens ensuite choisir la trame qui m'intéresse et l’exporter :

<img src="./src/images/forensic/forensic_Intro_4.png"/>

J’ai donc belle et bien le fichier **“MalPack.deb”** :

<img src="./src/images/forensic/forensic_Intro_5.png"/>

Ensuite, on va dans `/usr/local/bin` et on y trouve le fichier simplescript.sh que l’ion peux venir extraire pour l’exécuter ou bien juste l’ouvrir pour obtenir le flag :

<img src="./src/images/forensic/forensic_Intro_6.png"/>




## Challenge Silver 69 résolutions :

**Ennoncé :**
>Author: Mr.NOODLE#9112
>
>Hey,
>I received a flash drive in my mailbox. It appears that the person who sent me the package was aware that I was using Linux. However, the flash drive self-destructed before I was able to make an image of it. To get the flag, you have to go to the showcase site of the >c2 in question.
>
>This is real malware, so be careful when running it, use a vm for malware analysis
>
>Checksum Sha256 of usb_drive.img : 8947e34165792040d86915aea29df01f5e65f49ccfd624032522720ffb87c379



#### Récupération des fichiers

On vient télécharger le fichier `Silver` qui s'avère être un 7z.
On l’extrait et on obtient un fichier image nommé `usb_drive.img`.

La première chose à laquelle on pense, c'est de monter le fichier image dans un dossier nommé **usb-drive**.

<img src="./src/images/forensic/forensic_Easy_1.png"/>

Or si on se rend ensuite dans le fichier, on voit rapidement que celui-ci est vide.
Donc on va venir utiliser **Autopsy** qui est un logiciel qui va permettre de récupérer des documents qui ont été supprimés.

Il nous permet d’analyser l’image et d’obtenir d'intéressants fichiers.

<img src="./src/images/forensic/forensic_Easy_2.png"/>



#### Analyse des fichiers récupéré

On y voit notamment un fichier `.pdf.png` qui contient juste une image et le fichier `.Important.pdf.desktop` qui est un raccourcis :

<img src="./src/images/forensic/forensic_Easy_3.png"/>

On peut donc y voir que qui va executer un programme nommé `.a.sh` qui est un script bash :

<img src="./src/images/forensic/forensic_Easy_4.png"/>

Ici, le programme va venir ajouter une ligne de commande au programme `~/.bashrc` qui va exécuter à chaque fois qu’un nouveau terminal est ouvert le programme `~/fierfox`.
Ensuite, il vient copier le fichier `.firefox.elf` dans le dossier `~/.firefox`.
Il vient ensuite recharger `~/.bashrc` avec la commande source, puis vient ouvrir le fichier `.important.pdf`.
Il y a une dernière ligne en commentaire pour supprimer le fichier `Important.pdf.desktop`.
Le fichier Important.pdf n’est rien de plus qu’un pdf contenant “Hello, this is important” et ne va pas vraiment nous intéresser.

Et pour finir, le plus important, le fichier `.firefox.elf`. L'extension .elf est le format de fichier binaire standard pour les systèmes UNIX. Or on sait, par l’énoncé, que cet exécutable envoie des informations vers un serveur distant.



#### Interception du site malveillant

Par mesure de précaution, j’ai donc créé un VM pour exécuter ce programme.
Lors de son exécution, comme on peut s’en douter, il ne se passe rien visuellement, mais si on vient faire un scan du réseau avec **Wireshark**, on peut observer que lorsque l’on exécute le fichier, certaines trames apparaissent.

<img src="./src/images/forensic/forensic_Easy_5.png"/>

On y voit notamment 192.168.0.168 (qui est l’ip de ma VM) qui envoie des données au 178.62.67.181 sur le port 443.
Et si je rentre dans une barre de recherche, 178.62.67.181:443

On y voit une page web avec :

<img src="./src/images/forensic/forensic_Easy_6.png"/>