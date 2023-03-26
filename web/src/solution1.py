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

def selectionne_max(tab, i, cle):
  """
  Renvoie l'indice du plus grand élément du tableau de dictionnaires tab, à partir de l'indice i, à partir duquel chercher et de la clé du dictionnaire dans laquelle chercher.

  Arguments:
  - tab: tableau de dictionnaire dans lequel chercher la valeur
  - i: indice minimum, à partir duquel on commence à chercher dans le tableau
  - cle: clé selon laquelle chercher la plus grande valeure

  Retour :
  - res : correspond à un entier de l'indice où se trouve la plus grande valeur
  
  Pre-condition:
  - cle doit etre une clé des dictionnaires du tableau tab et doit correspondre à des valeurs int ou float
  - i ne doit pas etre plus grand que le nombre d'élément de tab
  """
  res = i
  maximum = tab[i][cle]
  for j in range(i + 1, len(tab)):
    if tab[j][cle] > maximum:
      maximum = tab[j][cle]
      res = j
  return res


def tri_decroissant_selection(tab, cle):
  """
  Trie un tableau de dictionnaire avec l'algorithme du tri par sélection selon la valeur des dictionnaires pour la clé précisée en argument.
  
  Arguments:
  - tab: tableau de dictionnaire à trier
  - cle: clé selon laquelle trier le tableau 
  """
  for i in range(len(tab)):
    ind_max = selectionne_max(tab, i, cle) # récupère l'indice ou se trouve la plus grande valeur pas encore trié
    tab[i], tab[ind_max] = tab[ind_max], tab[i] # échange la plus grande valeur restant à trié avec la première valeur parmis celle qui ne sont pas encore trié


def rapport(films):
  """     
  Ajoute la clé rapport qui fait le rapport entre la duree et la taille pour chaque dictionnaire du tableau de films
  
  Arguments:
    - films: Tableau de dictionnaires conteant les informations sur chaque film
  
  Pré-condition:
    - Tableau de dictionnaire avec les clés : "volume", "duree"
  """
  for elt in films:
    elt["rapport"] = elt["duree"] / elt["taille"]

    
def calcul_solution(films, tailleMax):
  """
  Pour un liste de films, optimise la duree de visionage (en minutes) pour un volume donné (en Go).
  Pour cela, on trie les films par ordre décroissant, par rapport à leur rapport entre la duree et la taille, et on les ajoute à la solution tant que la taille de la solution est inférieur à tailleMax.
  
  Arguments :
    - films: tableau de dictionnaires contenant les données des films: un entier pour la duree de visionage, un autre pour le volume du fichier et un str pour le nom du fichier
    - tailleMax: entier correspondant à l'espace disponible pour les films (en Go)
  
  Retour :
    - tuple: contenant un tableau des films sélectionnés, un entier de la duree de visionage optimale (en minutes) et un float du volume qu'occupent l'ensemble des films (en Go)
  
  """
  taille_solution = 0
  duree_solution = 0
  solution = []
  
  rapport(films)
  tri_decroissant_selection(films, "rapport")
  
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
  print("\n\nSELON LA SOLUTION GLOUTON RATIO : \n")          
  afficher_solution(calcul_solution(films, tailleMax))