# Exercice 8
A={1,2,3,4}
B={3,4,5,6}

'''print(A.isdisjoint(B))
print(A.update(B))
print(B.difference(A))
print(A.intersection(B))'''
print("Union: ", A|B)
print("Intersection: ", A & B)
print("La difference: ", A-B)

# Autre méthodes
print("Union 2: ", A.union(B))
print("Intersection 2: ", A.intersection(B))
print("Difference 2:", A.difference(B))

# Exercice 9
# Supprimer les doublons en utilisant un ensemble
L= [1,2,2,3,4,4,5]
k= L.remove(2)
i = L.remove(4)
print("La liste mise a jour:",L)

# Exercice 10
# Afficher le nom de l'etudiant
etudiant = {"nom": "Ali", "age":20, "note":83}
print("le nom de l'etudiant: ", etudiant.get("nom"))
print("La note de l'etudiant: ", etudiant.get("note"))

# Exercice 11
# Stocker des informations dans le dictionnaire
utilisateur = {}
a= input("Veuiller saisir votre nom: " )
b = input("Donner votre age: ")
c = input("Veuiller saisir la ville: " )
utilisateur["nom"] = a
utilisateur["age"] = b
utilisateur["ville"] = c 
print("Les informations du dictionnaire : ", utilisateur)

# Exercice 12
# Calculer la moyenne des notes
P = {"Math": 80, "Python":90, "Reseau":70}
print("Calculer la moyenne des matieres: ",(P.get("Math")+P.get("Python")+ P.get("Reseau"))/3)

# Exercice 13
# Afficher les element d'un tuple
thistuple = ("cyber", "python", "reseau")
print("le premier element du tuple: ", thistuple[0])
print(" Le nombre d'element du tuple ", len(thistuple)) 

# Exercice 14
# Creer un tuple avec 3 nombres
tuple3 = (1,4,6)
print("La somme des element du tuple: ",sum(tuple3))

# Exercice 15
# Creer une pile vide, empilr 3 nombres et depiler le dernier puis affiche la pile
maPile = []
maPile.append(23)
maPile.append(18)
maPile.append(45)
maPile.pop()
print("La pile final: ", maPile)

# Exercice 16
# creer une file vide et ajouter 3 elements, retire le premier puis afficher la file
maFile = []
maFile.append(90)
maFile.append(67)
maFile.append(56)
maFile.pop(0)
print("La file finale: ", maFile)

# Exercice des vaeriable
# creation d'une liste de 5 etudiants
listeEtudiant = []
etudiant1 = {"nom":"Salma", "moyenne":90}
etudiant2 = {"nom":"Minal", "moyenne":95}
etudiant3 = {"nom":"Abdoul Hamid", "moyenne":89}
etudiant4 = {"nom":"Hanane", "moyenne":70}
etudiant5 = {"nom":"Abdoul Raheem", "moyenne":81}
listeEtudiant.append(etudiant1)
listeEtudiant.append(etudiant2)
listeEtudiant.append(etudiant3)
listeEtudiant.append(etudiant4)
listeEtudiant.append(etudiant5)
print("L'etudiant ayant la meilleure moyenne: ", listeEtudiant)