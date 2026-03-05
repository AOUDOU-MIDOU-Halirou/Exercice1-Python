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
'''nombrepremier = int(input("Veuillez entrer un nombre: "))
for i in range(1,nombrepremier+1):
    for x in range(1,i):
        if i % x == 0:
            print(i," n'est pas un nombre premier")
        else:
            print(i,("est un nombre premier")) '''
