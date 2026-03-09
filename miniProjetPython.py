# Gestion des contacts
def ajouter_contact():
    nom = str(input("Veuillez saisir votre nom: "))
    tel = int(input("Saisir votre numero de telephone: "))
    email = str(input("Veuillez saisir votre email: "))
    with open("contacts.txt", "a") as fichier:
        fichier.write({"nom": nom, "telephone": tel,  "email": email} + "\n")
def afficher_contacts():
    with open("contacts.txt", "r") as fichier:
        contact = fichier.read()
        print(contact)
def rechercher_contact():
    pass
def supprimer_contact():
    pass
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