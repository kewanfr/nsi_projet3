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

def recupDuree(film):
  """
  Retourne la duree d'un film. Cette fonction est utilisée pour le tri des films par ordre décroissant de duree.

  Arguments:
    - film: dictionnaire du film dont on veut la duree
    
  Pré-condition:
    - film doit être un dictionnaire contenant la clé "duree"

  Retour:
    - int: duree du film
  """
  return film["duree"]


def calcul_solution(films, tailleMax):
  """
  Pour un liste de films, optimise la duree de visionage (en minutes) pour un volume donné (en Go).
  Trie par ordre décroissant la liste de films en fonction de la durée du film. Itère sur tous les films pour prendre les films un par un jusqu'à arriver à la tailleMax.
  
  Arguments :
    - films: tableau de dictionnaires contenant les données des films: un entier pour la duree de visionage, un autre pour le volume du fichier et un str pour le nom du fichier
    - tailleMax: entier correspondant à l'espace disponible pour les films (en Go)
  
  Retour :
    - tuple: contenant un tableau des films sélectionnés, un entier de la duree de visionage optimale (en minutes) et un float du volume qu'occupent l'ensemble des films (en Go)
  
  """
  taille_solution = 0
  duree_solution = 0
  solution = []
  
  films = sorted(films, key=recupDuree, reverse=True) # Tri décroissant selon la durée du film
  
  for elt in films:
    if taille_solution + elt["taille"] <= tailleMax:
      taille_solution += elt["taille"]
      duree_solution += elt["duree"]
      solution.append(elt)
          
  return(solution, duree_solution, taille_solution)


def afficher_solution(solution):
  """
  Affiche une solution donnée du problème de duree de visionage optimale
  
  Arguments:
    - solution: correspond à un tuple contenant un tableau des films sélectionnées, un entier de la duree de visionage optimale en minutes et un float du volume que prennent l'ensemble des films en Go
  """
  films, duree_total, taille_totale = solution
  print("La duree de visionnage optimale est de", duree_total, "minutes")
  print("Pour cela il faudrait prendre les films suivant :")
  for film in films:
    print(" - ", film["nom"])
  print("Cela occuperait un volume total de :", taille_totale, "Go")


if __name__ == '__main__': # permet de ne pas executer le code si le fichier est importé
  print("\n\nSELON LA SOLUTION GLOUTON : \n")          
  afficher_solution(calcul_solution(films, tailleMax))