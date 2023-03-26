from solution1 import calcul_solution
import unittest

films1 = [
  {
    "nom": "f1",
    "duree": 50,
    "taille": 2.5,
  },
  {
    "nom": "f2",
    "duree": 50,
    "taille": 2.5,
  },
  {
    "nom": "f3",
    "duree": 50,
    "taille": 2.7,
  }
]
films2 = []

films3 = [
  {
    "nom": "f1",
    "duree": 20,
    "taille": 20,
  },
  {
    "nom": "f2",
    "duree": 20,
    "taille": 15,
  }
]
films4 = [
  {
    "nom": "f1",
    "duree": 20,
    "taille": 20,
  },
  {
    "nom": "f2",
    "duree": 6,
    "taille": 6,
  },
  {
    "nom": "f3",
    "duree": 20,
    "taille": 15,
  }
]

def recup_nom(tab):
  """
  Récupère la valeur stockée dans la clé "nom" pour tous les dictionnaires du tableau tab
  
  Argument :
    - tab : tableau de dictionnaire ayant une clé "nom"

  Retour :
    - retourne un tableau de la valeur de la clé "nom" pour chaque dictionnaire de tab

  Pré-condition :
    - les dictionnaires dans tab doivent avoir une clé "nom"
  """
  tab_nom = []
  for elt in tab:
    tab_nom.append(elt["nom"])
  return tab_nom

class test_solution1(unittest.TestCase):
  def test1(self):
    """
    intérêt du test : test basic vérifiant si la fonction retourne des résultats cohérent
    """
    self.assertEqual(recup_nom(calcul_solution(films1, 5)[0]), ["f1", "f2"])
      
  def test2(self):
    """
    intérêt du test : test le bon fonctionnement de la fonction lorsqu'on lui donne un tableau vide
    """
    self.assertEqual(recup_nom(calcul_solution(films2, 5)[0]), [])
      
      
  def test3(self):
    """
    intérêt du test : Vérifie que la fonction choisit bien f2 qui a le meilleur rapport entre f1 et f2
    """
    self.assertEqual(recup_nom(calcul_solution(films3, 20)[0]), ["f2"])


def test4():
  """
  Test sans unitest
  intérêt du test : vérifier que la fonction fonctionne correctement en lui donnant une liste de films ou tous sont trop volumineux
  """
  try:
    val = []
    assert(recup_nom(calcul_solution(films4, 5)[0]) == val)
    print("Test 4 : OK")
  except AssertionError:
    print("Test 4 : Assert error : ", calcul_solution(films4, 2)[0], " != ", val)
    return

test4()
unittest.main()