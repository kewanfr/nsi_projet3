films = [
  {
    "nom": "film d'intrigue à suspense",
    "duree": 114,
    "taille": 4.57,
  },
  {
    "nom": "film d'animation japonais",
    "duree": 80,
    "taille": 2.71,
  },
  {
    "nom": "court-métrage 1",
    "duree": 32,
    "taille": 0.63,
  },
  {
    "nom": "court-métrage 2",
    "duree": 20,
    "taille": 1.65,
  },
  {
    "nom": "court-métrage 3",
    "duree": 18,
    "taille": 2.15,
  },
  {
    "nom": "vlog 1",
    "duree": 4,
    "taille": 0.085,
  },
  {
    "nom": "vlog 2",
    "duree": 5,
    "taille": 0.320
  }
]

tailleMax = 5

def parties(str_bin, tab):
  """
  Selectionne des valeurs dans tab en fonction du nombre binaire str_bin, on prend chaque élément de tab qui correspond à un "1" dans le nombre binaire et on renvoie le tableau des éléments sélectionnés
  
  Arguments :
    - tab: tableau ayant autant de case que le nombre binaire a de bit
    - str_bin: chaine de caractère correspondant a un nombre binaire
  
  Retour:
    - retourne le tableau des valeurs sélectionnées
  
  Pré-condition :
    - str_bin doit être un nombre binaire au format str
    - tab doit avoir autant de case que le nombre de bit sur lequel le nombre binaire est définie
  """
  partie = []
  for i in range(len(str_bin)): # la valeur binaire est un str donc on peut la parcourir
    if str_bin[i] == '1':
      partie.append(tab[i])
  return partie
    
def calcul_solution(films, tailleMax):
  """
  Pour une liste de films, donne la meilleure duree (en minutes) de visionage pour un volume donné (en Go).
  Pour cela, on fait toutes les combinaisons de films possibles et on teste chacune d'entre elles pour trouver la meilleure solution.
  
  Arguments :
    - films: tableau de dictionnaires contenant les données des films: un entier pour la duree de visionage, un autre pour le volume du fichier et un str pour le nom du fichier
    - tailleMax: entier correspondant à l'espace disponible pour les films (en Go)
  
  Retour :
    - tuple: contenant un tableau des films sélectionnés, un entier de la duree de visionage optimale (en minutes) et un float du volume qu'occupent l'ensemble des films (en Go)
    
  """
  films = films
  nb_films = len(films)
  num_solution = (2**nb_films)-1
  
  duree_solution = 0
  taille_solution = 0
  meilleur_solution = []
  if films == []:
    return ([], 0, 0) # si la liste de films est vide on retourne des valeurs par défaut
  
  while num_solution > 0: # boucle tant que toutes les solutions n'ont pas été testés
    bi = bin(num_solution)[2:].zfill(nb_films) # donne la valeure binaire du numéro de la solution à testé
    solution_teste = parties(bi, films) # génère la solution de combinaisons de films à tester
    
    addition_taille = 0
    addition_duree = 0
    
    for film in solution_teste: 
      if addition_taille + film["taille"] <= tailleMax:
        fonctionne = True
        addition_taille += film["taille"]
        addition_duree += film["duree"]
      else: # si la solution nécessite plus que le volume maximum on arrete et on met les variables à 0 pour s'assurer que la solution ne soit pas choisie
        fonctionne = False
        break
    # On prend la solution testée comme nouvelle meilleure solution si la solution ne nécessite pas plus que le volume maximum
    if not fonctionne:
      pass
    # et que la duree de visionnage est supérieure a la meilleur solution actuel ou que les duree de visionages sont égale mais que le volume de la solution testé est plus faible
    elif duree_solution < addition_duree or (duree_solution == addition_duree and taille_solution > addition_taille): 
      duree_solution = addition_duree
      taille_solution = addition_taille
      meilleur_solution = solution_teste
    
    num_solution -= 1 # on passe à la solution suivante
      
  return (meilleur_solution, duree_solution, taille_solution)


def afficher_solution(solution):
  """
  Affiche une solution donnée du problème de duree de visionage optimale
  
  Arguments:
    - solution: correspond à un tuple contenant un tableau des films sélectionnées, un entier de la duree de visionage optimale en minutes et un float du volume que prennent l'ensemble des films en Go
  """
  films, duree_total, taille_total = solution
  print("La duree de visionnage optimale est de", duree_total, "minutes")
  print("Pour cela il faudrait prendre les films suivant :")
  for film in films:
    print(" - ", film["nom"])
  print("Cela occuperait un volume total de :", taille_total, "Go")



if __name__ == '__main__': # permet de ne pas executer le code si le fichier est importé
  print("\nSELON LA SOLUTION BRUTE : \n")
  afficher_solution(calcul_solution(films, tailleMax))
