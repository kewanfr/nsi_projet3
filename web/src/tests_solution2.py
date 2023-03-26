from solution2 import calcul_solution

films1 = []
films2 = [
  {
    "nom": "f1",
    "duree": 51,
    "taille": 2.5,
  },
  {
    "nom": "f2",
    "duree": 51,
    "taille": 2.5,
  },
  {
    "nom": "f3",
    "duree": 50,
    "taille": 2.4,
  }
]
films3 = [
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
films4 = [
  {
    "nom": "f1",
    "duree": 20,
    "taille": 1,
  },
  {
    "nom": "f2",
    "duree": 30,
    "taille": 1,
  },
  {
    "nom": "f3",
    "duree": 120,
    "taille": 2,
  }
]
films5 = [
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

def test1():
  """
  Verifie le bon fonctionnement de la fonction avec un tableau vide
  """
  try:
    assert(calcul_solution(films1, 5)[0] == [])
    print("Test 1 : OK")
  except AssertionError:
    print("Test 1 : Assert error : ", calcul_solution(films1, 5)[0], " != ", val)
    
def test2():
  """
  Intérêt du test : test basique vérifiant que la fonction retourne des résultats cohérent
  """
  val = ["f1", "f2"]
  try:
    assert(recup_nom(calcul_solution(films2, 5)[0]) == val)
    print("Test 2 : OK")
  except AssertionError:
    print("Test 2 : Assert error : ", recup_nom(calcul_solution(films2, 5)[0]), " != ", val)
    
def test3():
  """
  Verifier que les résultats sont ceux attendus
  """
  val = ["film d'intrigue à suspense", "vlog 2", "vlog 1"]
  try:
    assert(recup_nom(calcul_solution(films3, 5)[0]) == val)
    print("Test 3 : OK")
  except AssertionError:
    print("Test 3 : Assert error : ", recup_nom(calcul_solution(films3, 5)[0]), " != ", val)

def test4():
  """
  intérêt du test : vérifier que la fonction fonctionne correctement en lui donnant une liste de films où le total est inférieur à 5Go
  """
  try:
    val = ["f3", "f2", "f1"]
    assert(recup_nom(calcul_solution(films4, 5)[0]) == val)
    print("Test 4 : OK")
  except AssertionError:
    print("Test 4 : Assert error : ", recup_nom(calcul_solution(films4, 5)[0]), " != ", val)

def test5():
  """
  intérêt du test : vérifier que la fonction fonctionne correctement en lui donnant une liste de films tous trop volumineux
  """
  try:
    val = []
    assert(calcul_solution(films5, 5)[0] == val)
    print("Test 5 : OK")
  except AssertionError:
    print("Test 5 : Assert error : ", calcul_solution(films5, 5)[0], " != ", val)

test1()
test2()
test3()
test4()
test5()
    
