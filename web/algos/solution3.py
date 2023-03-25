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

def selectionne_min(tab, i, cle):
  """
  Renvoie l'indice du plus petit élément du tableau d'objets tab, à partir de l'indice i et de la clé d'objets.

  Arguments:
  - tab: tableau d'objets à trier
  - i: indice minimum
  - cle: clé selon laquelle trier le tableau d'objets
  """
  res = i
  minimum = tab[i][cle]
  for j in range(i + 1, len(tab)):
    if tab[j][cle] < minimum:
      minimum = tab[j][cle]
      res = j
  return res

def tri_selection(tab, cle):
  """
  Trie un tableau d'objets par l'algorithme du tri sélection selon la clé précisée en argument.
  Arguments:
  - tab: tableau d'objets à trier
  - cle: clé selon laquelle trier le tableau d'objets
  """
  for i in range(len(tab)):
    # i est le nombre d'éléments bien triés, et aussi l'indice où placer
    # le prochain élément (le début de la partie non-triée).
    ind_min = selectionne_min(tab, i, cle)
    tab[i], tab[ind_min] = tab[ind_min], tab[i]


def rapport(films):
  """
  Fait le rapport entre la duree et la taille pour chaque éléments
  Arguments:
  - films: Tableau de dictionnaire
  Prérequis:
  Tableau de dictionnaire avec les clés : "taille", "duree" et "rapport"
  """
  for i in range(len(films)):
        rapport = films[i]["duree"] / films[i]["taille"]
        films[i]["rapport"] = rapport
        
def solution_rapport(films):
    """
    Affiche les films avec la taille totale et le temps total pour avoir le plus de durée de contenu possible dans le stockage
    Arguments:
    - films: tableau de dictionnaire
    Prérequis:
    Tableau de dictionnaire contenant les clés ""nom", "taille", "duree" et "rapport"
    """
    films_gardes = []
    taille_films = 0
    duree_films = 0
    rapport(films)
    tri_selection(films, "rapport")
    films = list(reversed(films))
    for i in range(len(films)):
        valeur_taille = taille_films + films[i]["taille"]
        if valeur_taille < 5:
            taille_films += films[i]["taille"]
            films_gardes.append(films[i]["nom"])           
            duree_films += films[i]["duree"]
        else:
            pass

          
        
    print("Les films sont :")
    for i in range(len(films_gardes)):
        print("- ", films_gardes[i])
    print("La taille totale est de", round(taille_films, 2), "Go.")
    print("La durée totale est de", duree_films, "minutes.")    


solution_rapport(films)
