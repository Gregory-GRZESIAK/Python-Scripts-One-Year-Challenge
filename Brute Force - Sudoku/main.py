import os
import numpy as np
import time
class BruteForceSudoku():
    grid = []
    def __init__(self):
        file_path = os.path.join(os.path.dirname(__file__), 'grille.txt')
        with open(file_path) as f:
            lines = f.readlines()

        for l in lines:
            l = l[:-1]
            self.grid.append(l.split(' '))
            
        self.printSudoku()
        print("Le Brute force commence : ")
        time.sleep(1)
        coords = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == "0":
                    coords.append((i, j))
        
        self.BruteForce(coords, 0)
        
        
    def BruteForce(self, coords, icoord):
        time.sleep(0.01)
        if icoord >= len(coords):  # Condition d'arrêt : Si toutes les cases sont remplies
            print("Solution trouvée")
            self.printSudoku()
            return True

        if icoord < 0:  # Si on revient trop en arrière, on n'a pas de solution
            print("Pas de solution")
            return False

        # Coordonnées actuelles
        coord = coords[icoord]
        case = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        # Si la case est vide, on essaie les chiffres de 1 à 9
        if self.grid[coord[0]][coord[1]] == "0":
            for num in case:
                self.grid[coord[0]][coord[1]] = num
                if self.CheckValueInLine(coord) and self.CheckValueInColumn(coord) and self.CheckValueInBlock(coord):
                    self.printSudoku()
                    # Appel récursif pour la case suivante
                    if self.BruteForce(coords, icoord + 1):
                        return True
            # Si aucun chiffre ne convient, on réinitialise la case et on fait marche arrière
            self.grid[coord[0]][coord[1]] = "0"
            return False

        # Si la case n'est pas vide, on passe à la suivante
        return self.BruteForce(coords, icoord + 1)
    def CheckValueInLine(self, coord):
        t = np.array(self.grid[coord[0]])
        value = self.grid[coord[0]][coord[1]]
        
        unique, counts = np.unique(t, return_counts=True)
        if dict(zip(unique, counts))[f"{value}"] != 1:
            return False
        else : 
            return True
    def CheckValueInColumn(self, coord):
        col = []
        for i in self.grid:
            col.append(i[coord[1]])
        
        t = np.array(col)
        value = self.grid[coord[0]][coord[1]]
        
        unique, counts = np.unique(t, return_counts=True)
        if dict(zip(unique, counts))[f"{value}"] != 1:
            return False
        else : 
            return True
    def CheckValueInBlock(self, coord):
        a = [0, 1, 2]
        b = [3, 4, 5]
        c = [6, 7, 8]
        sections = [a, b, c]
        value = self.grid[coord[0]][coord[1]]
        grid_tempo = []

        # Extraire les sous-grilles 3x3
        for row_section in sections:
            for col_section in sections:
                bloc = []
                for i in row_section:
                    bloc.extend(self.grid[i][col_section[0]:col_section[2] + 1])
                grid_tempo.append(bloc)
                
        nbbloc = 3 * (coord[0] // 3) + (coord[1] // 3)
        t = np.array(grid_tempo[nbbloc])
        unique, counts = np.unique(t, return_counts=True)
        if dict(zip(unique, counts))[f"{value}"] != 1:
            return False
        else : 
            return True
               
    def printSudoku(self):
        a = [0, 1, 2]
        b = [3, 4, 5]
        c = [6, 7, 8]
        sections = [a, b, c]

        for section in sections:
            for i in section:
                for block in sections:
                    for j in block:
                        print(f" {self.grid[i][j]} ", end="")
                    print('|', end="")
                print('')
            print("-----------------------------")
                
a = BruteForceSudoku()        