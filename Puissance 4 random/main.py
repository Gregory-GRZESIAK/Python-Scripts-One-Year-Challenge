import random
import numpy as np
import time

class Puissance4Aleatoire():
    nb_colonne = 7
    nb_ligne = 6
    win = False
    
    form = {1:"X", 2:"O"}
    def __init__(self):
        self.grid = np.full([self.nb_ligne, self.nb_colonne], "-", dtype=str)
        self.winCondition = []
        self.winCount = 0
        self.winPlayer = 0
        i = 1
        while not self.win:
            if self.win:  # Ajout de cette condition pour arrêter la boucle si quelqu'un gagne
                break
            if i % 2 != 0:
                self.tour(1)
            else:
                self.tour(2)
            
            if i == int(self.nb_ligne*self.nb_colonne):
                self.win = True    
                print("No win")
            i += 1
    
    def tour(self, joueur):
        possible_columns = [i for i in range(self.nb_colonne) if self.grid[0][i] == "-"]
        column = self.chose_colum(possible_columns)

        coord = (self.send_to_bottom(column), column)
        self.grid[coord[0]][coord[1]] = self.form[joueur]
        self.check_win(coord, joueur)
        return
    def check_win(self, coord, joueur):
        # Check horizontal
        possible = [[1,2], [2,1], [3,0], [0,3]]
        directions = {
            "horizontal": (0, 1),
            "vertical": (1, 0),
            "diag_down": (1, 1),
            "diag_up": (1, -1)
        }
        for direction, (d_row, d_col) in directions.items():
            for p in possible:
                res = []
                for i in range(-p[0], p[1] + 1):
                    row = coord[0] + i * d_row
                    col = coord[1] + i * d_col
                    if 0 <= row < self.nb_ligne and 0 <= col < self.nb_colonne:
                        res.append(self.grid[row][col])
                # Condition de victoire : quatre jetons alignés du même joueur
                if len(res) == 4 and all(cell == self.form[joueur] for cell in res):
                    self.win = True
                    self.winCondition.append(direction)
                    self.winCount += 1
                    self.winPlayer = joueur
                    ## print(coord)
                    ## print(self.grid)
                    ## print(f"win! {direction.capitalize()} {joueur}")
                    ## print("-------")
        return


    def send_to_bottom(self, colonne):
        i = 0
        while i < self.nb_ligne and self.grid[i][colonne] == "-":
            i += 1
        return i - 1 if i > 0 else i

    
    def chose_colum(self, colonne_possible: list):
        return random.choice(colonne_possible)


# Mesurer le temps de début
start_time = time.time()

res = {"null": 0, "player1": 0, "player2": 0, "horizontal": 0, "vertical": 0, 
       "diag_down": 0, "diag_up": 0, "win1": 0, "win2": 0, "win3": 0, 
       "win4": 0, "win5": 0, "win6": 0, "win7": 0}

essaie_nombre = 100

for i in range(essaie_nombre):
    print(f"Essaie : {i+1}")
    a = Puissance4Aleatoire()
    if a.winCount == 0:
        res["null"] += 1
    else:
        res["player1"] += int(a.winPlayer == 1)
        res["player2"] += int(a.winPlayer == 2)
        res["horizontal"] += a.winCondition.count("horizontal")
        res["vertical"] += a.winCondition.count("vertical")
        res["diag_down"] += a.winCondition.count("diag_down")
        res["diag_up"] += a.winCondition.count("diag_up")

        res["win1"] += int(a.winCount == 1)
        res["win2"] += int(a.winCount == 2)
        res["win3"] += int(a.winCount == 3)
        res["win4"] += int(a.winCount == 4)
        res["win5"] += int(a.winCount == 5)
        res["win6"] += int(a.winCount == 6)
        res["win7"] += int(a.winCount == 7)

# Mesurer le temps de fin
end_time = time.time()

# Affichage des statistiques finales
print("\n\n\n\n")
print("---------------------------")
print(f"Nb essaie : {essaie_nombre}")
for key, value in res.items():
    print(f" -> {key}: {value}")

print(f"Winrate 1 : {res['player1']/essaie_nombre}")
print(f"Winrate 2 : {res['player2']/essaie_nombre}")
print(f"Null : {res['null']/essaie_nombre}")

# Afficher le temps d'exécution total
print(f"Temps d'exécution : {end_time - start_time:.2f} secondes")
