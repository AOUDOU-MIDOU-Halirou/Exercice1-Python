# creation d'un mot de passe
mot_de_passe = ""

while mot_de_passe != "python123":
    mot_de_passe = input("Entrez le mot de passe :")

print("Accès autorisé")

# Afficher les 1 a 10 avec un boucle for
for i in range(1,11):
    print(i)

# Affiche des nombres paire entre 1 a 20
for i in range(1,21):
    if i % 2 ==0:
        print(i) 

# la table de multiplication de 7
for i in range(1,11):
    print("7 x", i ,"=", 7*i )

# demander un nombre a l'utilisateur et affiche 
# le carre de tous les nombre jusqu'a ce nombre
nombre = int(input("Veuillez entrer un nombre: "))
for i in range(1,nombre):
    print(i,"^2=",pow(i,2))

# Exercie 5
# Calculer la somme des nombres 1 à 100 avec une boucle
somme = 0
for i in range(1,101):
    somme = somme + i
    print(somme)

# Exercice 6
# Demander à l'utilisateur d'entrer un nombre
nombreFactoriel = int(input("Veuillez entrer un nombre: "))
factorielle = 1
for i in range(1,nombreFactoriel+1):
    factorielle = factorielle * i
    print(i,"! =  ", factorielle)

# exercice 7
# nombre premier
nombrepremier = int(input("Veuillez entrer un nombre: "))
est_premier = True
for i in range(2,nombrepremier):
    if nombrepremier % i ==0:
        est_premier=False
        break
if est_premier == True:
    print(f"Le nombre {nombrepremier} est premier.")
else:
    print(f"Le nombre {nombrepremier} n'est pas premier.")
    
# Exercice 8
# Afficher tout les nombres premiers entre 1 et 50
for i in range(2,51):
    for x in range(2,i):
        if i % x == 0:
            print(f"Le nombre {i} n'est pas remier.")
            break       
    else:
        print(f"le nombre {i} est premier")
        
# Exercice 9
# ce programme demande un nombre a l'utilisateur 
# jusqu'a ce que ce dernier entre 0
utili = 4
somme = 0
while utili != 0:
    utili = int(input("Veuillez donner un nombre: "))
    somme = somme + utili
print(f"La somme = {somme}")
