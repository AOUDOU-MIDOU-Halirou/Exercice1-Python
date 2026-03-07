# Exercice1
def bonjour():
    print("Bonjour et bienvenue en python.")
bonjour()

# Exercice 2
# Creation d'un methode qui clacule le carre d'un nombre
def carre(nombre):
    print(f"Le carre de {nombre} est: ", pow(nombre,2))
carre(4)
carre(20)

# Exercice 3
# retourne la somme de a et b
def addition(a,b):
    return a+b
resultat = addition(3,7)
print("le resultat de la somme est: ",resultat)

# Exercice 4
# La methode retourne plusieur valeurs
def calcule(a,b):
    return (a+b, a*b)
somme, produit = calcule(5,8)
print(f"La somme du calcule est: {somme}")
print(f"Le produit du calcule est: {produit}")

# Exercice 5
# Verifie si un nombre est premier ou pas
def est_pair(nombre):
    if nombre % 2 == 0:
        return True
    return False
print(est_pair(6))

# Exercice 6
# Faire la somme des elements d'une liste
def somme_liste(liste):
    sommes = 0
    for i in liste:
        sommes = sommes + i
    return sommes
print(f"La somme des elements de la liste est: {somme_liste([1,2,3,4,5])}")

# Exercice 7
# une fonction retourne tous les nombres premiers jusqu'a n
def nombres_premiers(n):
    liste_nombre = []
    for i in range(2,n):
        for x in range(2,i):
            if i % x == 0:
                break
        else:
            liste_nombre.append(i)
    return liste_nombre

print(nombres_premiers(20))