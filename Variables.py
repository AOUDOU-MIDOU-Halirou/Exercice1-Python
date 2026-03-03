# echanger a,b sans utiliser c, a=12, b=5
a=12
b=5
a,b=b,a
print(a)
print(b)

# conversion et calcule
a= int(input("Enquel annee es-tu nee:"))
b = 2026 - a
print(f" En 2026, tu as {b} ans")

# conversion minutes en heures + minutes
m = int(input("Saisir un nombre de minutes:"))
c= m//60
d= m%60
print(f"{c} heures et {d} minutes")
# exercie 1 sur les variables
nom = "Salma"
age = 18
moyenne = 95
print("Je m'appelle " +nom+ ", j'ai " + str(age)+ " ans et ma moyenne est " +str(moyenne))

# exercices 2 sur les variables
'''un programme qui echange deux nombres, calcule leur somme et produit'''
e = 24
f = 45
e,f = f, e
print(f"L'echange de e et f donne: {e}, {f}")
print(f"la somme de e, e est: {e+f}")
print(f"le produit de e ef f donne: {e*f}")

# Exercice 3
# creation d'une liste
notes = [12,15,9,17,14]
print(f"La premiere note est: {notes[0]} ")
print(f"La derniere note est: {notes[-1]}")
print(f"La moyenne est : {sum(notes)/5}")

# Exercice 4
L= [10, 20, 30, 40, 50]
liste = [L[1],L[2],L[3]]
print("La liste original: ",L)
print("La nouvelle liste : ",liste)

# Exercice 5
#creer une liste vide, ajout 5 nombres puis afficher la somme
liste1 = []
liste1.append(25)
liste1.append(12)
liste1.append(21)
liste1.append(22)
liste1.append(16)
print(liste1)
print(f"La somme de la liste : {sum(liste1)}")
