
# 🔢 Sudoku Brute Force Solver 🧩

## 📜 Description du Projet
Ce projet implémente un **solveur de Sudoku par brute force** en Python. L'algorithme prend en entrée une grille de Sudoku (formatée dans un fichier `grille.txt`) et tente de la résoudre en utilisant une approche par essais successifs. 

Le solveur teste chaque case vide de la grille en essayant les chiffres de 1 à 9 et vérifie si la solution est valide en respectant les règles du Sudoku :
- **Ligne** : un même chiffre ne peut apparaître qu'une seule fois.
- **Colonne** : un même chiffre ne peut apparaître qu'une seule fois.
- **Bloc 3x3** : un même chiffre ne peut apparaître qu'une seule fois.

## 📂 Structure du Projet
```
📂 Sudoku Brute Force Solver
├── main.py          # Script principal pour résoudre le Sudoku
├── grille.txt       # Fichier contenant la grille de Sudoku à résoudre
└── README.md        # Documentation du projet
```

## 📝 Format du Fichier `grille.txt`
Le fichier `grille.txt` contient la grille de Sudoku à résoudre, avec :
- **0** représentant les cases vides.
- Les chiffres **1-9** représentant les valeurs déjà remplies.

**Exemple de contenu :**
```
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

## 🚀 Comment Exécuter le Script
Assurez-vous d'avoir **Python 3.x** installé ainsi que le package `numpy`. Pour installer `numpy`, utilisez la commande suivante :

```bash
pip install numpy
```

### Lancer le solveur
Pour exécuter le script, placez-vous dans le répertoire du projet et lancez la commande suivante :

```bash
python main.py
```

Le programme lira le fichier `grille.txt`, affichera la grille initiale, et tentera de la résoudre en utilisant un algorithme de brute force. Si une solution est trouvée, la grille complète sera affichée.

## 🔍 Fonctionnement du Solveur
1. **Lecture de la grille** : Le programme lit le fichier `grille.txt` et initialise la grille.
2. **Recherche des cases vides** : Le solveur identifie toutes les cases vides de la grille.
3. **Brute Force** : Le solveur tente d'insérer les chiffres de 1 à 9 dans chaque case vide, en vérifiant si chaque tentative respecte les règles du Sudoku.
4. **Backtracking** : Si un chiffre ne convient pas, le solveur revient en arrière et essaie un autre chiffre.

### Exemple de Sortie
```
Grille initiale :
 5  3  -  -  7  -  -  -  - |
 6  -  -  1  9  5  -  -  - |
 -  9  8  -  -  -  -  6  - |
-----------------------------
 8  -  -  -  6  -  -  -  3 |
 4  -  -  8  -  3  -  -  1 |
 7  -  -  -  2  -  -  -  6 |
-----------------------------
 -  6  -  -  -  -  2  8  - |
 -  -  -  4  1  9  -  -  5 |
 -  -  -  -  8  -  -  7  9 |
-----------------------------

Le Brute force commence :
Solution trouvée :
 5  3  4  6  7  8  9  1  2 |
 6  7  2  1  9  5  3  4  8 |
 1  9  8  3  4  2  5  6  7 |
-----------------------------
 8  5  9  7  6  1  4  2  3 |
 4  2  6  8  5  3  7  9  1 |
 7  1  3  9  2  4  8  5  6 |
-----------------------------
 9  6  1  5  3  7  2  8  4 |
 2  8  7  4  1  9  6  3  5 |
 3  4  5  2  8  6  1  7  9 |
-----------------------------
```

## 🛠️ Personnalisation
Pour résoudre une autre grille, il suffit de modifier le fichier `grille.txt` en y insérant une nouvelle grille de Sudoku.

## 📜 Licence
Ce projet est sous licence **MIT**. Vous êtes libre d'utiliser, de modifier et de partager ce code, mais merci de me créditer si vous l'utilisez pour vos propres projets.

---

Merci d'explorer ce projet ! Si vous avez des idées d'amélioration ou des questions, n'hésitez pas à ouvrir une issue ou à me contacter.
