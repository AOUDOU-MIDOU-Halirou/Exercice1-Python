# Exercice 1
# Nombres positifs ou negatifs
a = int(input("Veuillez entrer un nombre: "))
if a > 0:
    print("Nombre positif")
elif a < 0:
    print("Nombre negatif")
else:
    print("Zero")

# Exercice 2
# Nombre paire ou impaire
b = int(input("Veuillez saisir un nombre: "))
if b % 2 ==0:
    print(f"Ce nombre {b} est paire")
else:
    print(f"Ce nombre {b} est impaire")

# Exercice4
age = int(input(" Saisir un age quelqu'un: "))
if age < 13:
    print("cette personne est enfant")
elif age >= 13 and age < 18:
    print("cette personne est adolescent")
else:
    print("cette personne est adulte.") 

# Exercice 5
# creation d'un mot de passe
mot_de_passe = "python123"
motUtilisateur = str(input(" Veuillez entrer votre mot de passe: "))
if mot_de_passe == motUtilisateur:
    print("Acces autorisé")
else:
    print("Accès refusé.")

# Exercice 6
# Admission a l'universite
noteExamen = float(input("Veuillez saisir votre note: "))
noteProjet = float(input("Veuillez entrervla note du projet: "))

if noteExamen >= 50 and noteProjet >= 50:
    print("l'etudiant est accepté")
else:
    print("La demande de l'etudiant esst refusé.")

# Exercice 7
# Demander a l'utilisateur 3 nombres et affiche le plus grand nombre
a=float(input("Veuillez entrer un nombre : "))
b=float(input("Veuillez entrer un nombre : "))
c=float(input("Veuillez entrer un nombre : "))
if a > b:
    if a > c:
        print(f"le nombre le plus grand est. : {a}")
    else:
        print(f"le nombre le plus grand est : {c}")
else:
    if b > c:
        print(f"le plus grand nombre est: {b}")
    else:
        print(f"le plus grand nombre est: {c}")

# Exercice 8
# Annee bissextile
annee = int(input("Veuillez donner une une année: "))
if (annee % 4 ==0 and annee % 100 != 0) or annee % 400 ==0:
    print(f"Cette année {annee} est bissextile") 
else:
    print(f"Cette année {annee} n'est pas bissextile")

# Exercice 10
# Reduction magasin selon le montant achete
montantClient = float(input('Veuillez saisir le montant de  votre achat: '))
if montantClient >= 100:
    prix = (montantClient * 20) / 100
    prixFinal = montantClient - prix
    print(f"Le prix d'achat est {prixFinal}")
elif montantClient >= 50:
    prix = (montantClient * 10) /100
    prixFinal = montantClient - prix
    print(f"Le prix d'achat est {prixFinal}")
else:
    print("le d'achat sans reduction ", montantClient)

# Plus en profondeur
# Exercice 1
utilisateur = "admin"
mot_dePasse= "python1234"
nom = input("Veuillez saisir votre nom d'utilisateur: ").strip()
motDepasse = input("Veuillez saisir votre mot de passe: ").strip()
if utilisateur == nom and mot_dePasse == motDepasse:
    print("Connexion reussie.")
elif utilisateur == nom and mot_dePasse != motDepasse:
    print("le mot de passe incorrect")
elif utilisateur != nom and mot_dePasse == motDepasse:
    print("Utilisateur incorrect")
else:
    print("Utilisateur incorrect et mot de passe incorrect. ")

# Exercice 5
# Mini distributeur bancaire
solde = 1000
montantRetirer = int(input("Veuillez saisir le montant a retiré: "))
if montantRetirer > solde:
    print("Fonds insuffisants")
elif montantRetirer <= 0:
    print("Montant invalide")
else:
    solde -= montantRetirer
    print("Retrait accepté.")
    print("Le nouveau solde est ", solde)

