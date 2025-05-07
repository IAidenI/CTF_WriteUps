# Mission 1 :

<img src="../src/image/mission1.svg"/>

<br>

> **Brief de mission**  
> L'entité, confiante dans ses prises de parole, a mis en ligne un site web pour afficher les organisations qu'elle a compromises.  
> Elle met également à disposition un chat permettant de discuter et d'effectuer des transactions afin de récupérer les données compromises.

> **Objectifs de la mission**  
> Vous êtes mandaté par **Neoxis Laboratories** pour récupérer leurs données compromises.

## Analyse

Nous avons accès à un lien vers un site internet. Commençons par l'analyser.

<p align="center">
  <img src="./src/images/mission1_1.png" width="50%"/>
</p>

Nous avons un site web avec des données compromises en attente de paiement de la part des entreprises.
Nous sommes mandatés par Neoxis Laboratories pour récupérer leurs fichiers. Commençons donc par les [télécharger](https://github.com/IAidenI/CTF_WriteUps/blob/master/DGSE%202025/Mission1/Fichiers%20du%20challenge/neoxis_laboratories.zip), et évidemment impossible de le dézipper, il faut un mot de passe.

À première vue, on pourrait tenter de le brute-forcer. Mais ici, on voit qu'il y a un chatbot. Essayons de lui soutirer des informations.

## Exploitation du chatbot

### Entrons en contact

<p align="center">
  <img src="./src/images/mission1_2.png" width="30%"/>
</p>

---

### Tentative de restitution des fichiers

<p align="center">
  <img src="./src/images/mission1_3.png" width="30%"/>
</p>

---

### Manipulation de l'IA

Bon, logique, mais on ne sait jamais. On constate qu'il attend que le paiement soit confirmé.  
Tentons de lui faire croire que celui-ci a bien été effectué, en fournissant un faux lien de validation, par exemple : https://blockstream.info/tx/9f4d3c89a1b3d7e629f2f53d44b8d9e7b98e02f0d8ea5347a1f5c2de1e24b7d1

<p align="center">
  <img src="./src/images/mission1_4.png" width="30%"/>
</p>

---

### Succès : récupération du mot de passe

Cela porte ses fruits, le chatbot fournit le mot de passe du fichier ZIP chiffré : `cf0fe99934cbc10c7e55bada9870bda1691a4a27`

---

### Extraction du flag

Après avoir exploré les fichiers récupérés, le flag se trouve dans le fichier PDF.

<p align="center">
  <img src="./src/images/mission1_5.png" width="60%"/>
</p>
