# Exercice
# Creer un programme qui demande à une personne de son nom et 
# age pour l'enregistrer dans un fichier
'''nom = input("Veuillez ecrire votre nom:").strip()
age = input("Veuillez ecrire votre age:").strip()

# Enregistrer le nom et age de la personne dans le fichier
with open("personnes.txt", "a") as fichier:
    fichier.write("Nom: " +nom + ",")
    fichier.write("Age: " + age + ";\n")

# Afficher les information de la liste : Exercice 2
with open("personnes.txt", "r") as fichier:
    contenuFichier = fichier.read()
    print("Les informations enregistrées:")
    print(f"La liste des gens sur le fichier: {contenuFichier} ")'''

# Exercice 3
nombre = 0
while nombre != 3:
    nomEtudiants = input("Donner votre nom: ").strip()
    with open("etudiant.txt", "a") as fichier:
        fichier.write(nomEtudiants + "\n")
        fichier.close()
    nombre += 1

# Afficher les elements dans un fichier
with open("etudiant.txt", "r") as fichier:
    contenu = fichier.read()
    print("Les informations du fichier: ", contenu)
    print(f"le nombre d'etudiant: {len(contenu)}")
 