# Gestion des contacts
import json
def ajouter_contact():
    nom = str(input("Veuillez saisir votre nom:"))
    telephone = int(input("Saisir votre numero de telephone: "))
    email = str(input("Veuillez saisir votre email:"))
    dic = {"Nom": nom, "Telephone": telephone, "Email": email}
    with open("contacts.txt", "a") as fichier:
        fichier.write(json.dumps(dic) + "\n")
def afficher_contacts():
    with open("contacts.txt", "r") as fichier:
        for ligne in fichier:
            contact = json.loads(ligne)
            print("Nom:", contact["Nom"])
            print("Telephone:", contact["Telephone"])
            print("Email:", contact["Email"])
            print("-------------------------------------")
def rechercher_contact():
    nom = str(input("Veuillez saisir votre nom:")).strip()
    with open("contacts.txt", "r") as fichier:
        contact = fichier.read()
        if nom in contact:
            #print("Nom:", contact["Nom"])
            #print("Telephone:", contact["Telephone"])
            #print("Email:", contact["Email"])
            print("Ce nom est sur la liste.")
            print("-------------------------------------")
        else:
            print("Contact introuvable.")


def supprimer_contact():
    nom = str(input("Veuillez saisir votre nom:")).strip()
    with open("contacts.txt", "r") as fichier:
        contact = fichier.read()
        if nom in contact:
            del contact[nom]
            print("L'element supprimer.")
            afficher_contacts()
        else:
            print("Ce nom ne figure pas sur la liste.")
        
def menu():
    print("=== Gestionnaire de Contacts ===")
    print("1. Ajouter un contact ")
    print("2. Voir les contacts")
    print("3. Rechercher un contact")
    print("4. Supprimer un contact")
    print("5. Quitter")
while True:
    menu()
    choix = int(input("Choisissez une option: "))
    if choix == 1:
        ajouter_contact()
    elif choix == 2:
        afficher_contacts()
    elif choix == 3:
        rechercher_contact()
    elif choix == 4:
        supprimer_contact()
    elif choix == 5:
        print("Merci de visiter notre site. Au revoir !!!")
        break
    else:
        print("Votre choix est invalide, veuillez choisir à nouveau.")