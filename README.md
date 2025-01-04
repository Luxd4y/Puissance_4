# **Puissance 4**

## **Description du projet**
Puissance 4 est un jeu de société classique où deux joueurs s'affrontent en plaçant des jetons dans une grille. Le but est d'aligner quatre jetons de sa couleur (horizontalement, verticalement ou diagonalement). Ce projet implémente ce jeu en utilisant le langage Python et la bibliothèque `tkinter` pour la création de l'interface graphique. Un mode contre l'ordinateur est également inclus, où un bot joue de manière automatisée.

## **Prérequis**
Pour faire fonctionner ce projet, vous devez avoir installé Python et les modules suivants :
- `tkinter` : pour l'interface graphique.
- `math` : pour les calculs nécessaires au bot.
- `random` : pour les choix aléatoires dans le jeu (par exemple, le bot choisit un coup aléatoire parmi les possibilités).
- `time` : pour créer des pauses entre les actions du jeu, en particulier pour le bot.

### **Installation**
1. Téléchargez et installez Python sur [python.org](https://www.python.org/downloads/).
2. Assurez-vous d'avoir `tkinter` installé. Si ce n'est pas le cas, installez-le via votre gestionnaire de paquets ou en utilisant `pip` :
   ```bash
   pip install tk

## Comment jouer

### 1. Interface de jeu
Le jeu se joue sur une grille de **7 colonnes** et **6 lignes**.  
Les joueurs prennent des tours pour ajouter un jeton dans la colonne de leur choix.  
Le premier joueur à aligner **4 jetons** horizontalement, verticalement ou diagonalement gagne la partie.

### 2. Contrôles
- **Déplacement du jeton** :  
  Utilisez les flèches **gauche (←)** et **droite (→)** pour déplacer votre jeton dans la grille.
  
- **Placement du jeton** :  
  Appuyez sur la flèche **bas (↓)** pour déposer le jeton dans la colonne actuelle.
  
- **Quitter le jeu** :  
  Si vous souhaitez quitter le jeu, cliquez sur le bouton **"Quitter"** situé en haut à droite.

### 3. Mode Joueur contre l'ordinateur
- **Joueur 1** prend le **premier tour** et joue avec des **jetons rouges**.
- L'**ordinateur** joue ensuite avec des **jetons jaunes**.
- Le bot utilise une **logique simplifiée d'intelligence artificielle** pour choisir ses coups. L'algorithme **minimax** analyse les différentes possibilités sur la grille pour prendre la meilleure décision.
