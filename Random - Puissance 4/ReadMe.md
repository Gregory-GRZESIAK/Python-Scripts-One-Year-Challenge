# 🎮 Puissance 4 - Simulation Aléatoire 🟡🔴

## 📜 Description du Projet
Ce projet simule des parties de **Puissance 4** où deux joueurs jouent de manière entièrement aléatoire. Le but est de **faire jouer deux joueurs aléatoires un grand nombre de fois** et de **collecter des statistiques** sur les résultats des parties. Cela permet d'analyser la fréquence des victoires pour chaque joueur ainsi que les types d'alignements gagnants.

## 🔍 Fonctionnalités
- **Deux joueurs aléatoires** jouent tour à tour en plaçant leurs jetons de manière aléatoire dans la grille.
- La partie se termine lorsqu'un joueur aligne **4 jetons horizontalement, verticalement ou en diagonale**, ou lorsque la grille est complètement remplie.
- Le programme répète cette simulation sur un grand nombre de parties (par défaut, 1 500 000 essais) pour collecter des statistiques :
  - Nombre de victoires pour chaque joueur.
  - Type d'alignement gagnant (horizontal, vertical, diagonale).
  - Nombre de parties nulles (aucun gagnant).

## 📊 Statistiques Générées
À la fin de la simulation, le programme affiche :
- **Nombre total d'essais** effectués.
- **Victoires par joueur** (`player1` et `player2`).
- **Alignements gagnants** :
  - `horizontal`
  - `vertical`
  - `diag_down` (diagonale descendante)
  - `diag_up` (diagonale montante)
- Distribution du nombre d'alignements nécessaires pour gagner (`win1` à `win7`).
- **Winrate** pour chaque joueur et le pourcentage de parties nulles.

## 🛠️ Instructions pour Exécuter le Script
Assurez-vous d'avoir **Python 3.x** installé sur votre machine ainsi que le package `numpy`. Pour installer `numpy`, utilisez la commande suivante :

```bash
pip install numpy
```

Exécution
Pour exécuter le script, utilisez la commande suivante dans le terminal :
```bash
python main.py
```

Exemple de Résultats
Voici un exemple de sortie générée après avoir exécuté le programme avec 1 500 000 essais :
```yaml
Nb essaie : 1500000
 -> null: 3829
 -> player1: 833469
 -> player2: 662702
 -> horizontal: 704617
 -> vertical: 529720
 -> diag_down: 221864
 -> diag_up: 221111
 -> win1: 1340608
 -> win2: 133551
 -> win3: 18859
 -> win4: 2785
 -> win5: 327
 -> win6: 37
 -> win7: 4
Winrate 1 : 0.555646
Winrate 2 : 0.4418013333333333
Null : 0.0025526666666666666
Temps d'exécution : 980.49 secondes
```

## 📁 Structure du Dossier
Le projet est organisé comme suit :

```bash
📂 Random - Puissance 4
├── main.py         # Script principal
└── README.md       # Documentation
```

⚙️ Personnalisation des Paramètres
Vous pouvez modifier la variable essaie_nombre dans le fichier main.py pour ajuster le nombre de parties simulées :
```python
essaie_nombre = 1500000
```