import sqlite3

connection = sqlite3.connect("data/projet.db")
cursor = connection.cursor()


def display_cat(requete_cat):
    # Affiche les catégories

    liste_cat = []
    for elem in requete_cat:
        print(elem[1], ":", elem[0])
        liste_cat.append(elem[0])
    choix_user = input('Veuillez choisir la lettre de la catégorie qui vous intéresse :\n').upper()

    while choix_user not in liste_cat and not None:
        print('Ce n\' est pas une catégorie valable.')
        choix_user = input('Veuillez choisir la lettre de la catégorie qui vous intéresse :\n').upper()

    return choix_user


def display_diff(requete_diff):
    # Affiche les difficultés

    liste_diff = []
    for elem_diff in requete_diff:
        print(elem_diff[1], ":", elem_diff[0])
        liste_diff.append(str(elem_diff[0]))
    choix_diff = input('Veuillez choisir la difficulté :\n')

    while choix_diff not in liste_diff and not None:
        print('Ce n\'est pas une difficulté existante.')
        choix_diff = input('Veuillez choisir le numéro de la difficulté correspondante :\n')

    return choix_diff


def quiz(qcm):
    points = 0
    numero_qst = 1
    for qst in qcm.fetchall():
        print(str(numero_qst) + ') '+ qst[1] + "\n")
        affichage_rep = cursor.execute('SELECT rep_name, value FROM tb_reponses WHERE quest_ID = ?', (qst[0],))
        numero_rep = 1  # sert à afficher le numéro de question dans la console
        liste_reponses = []  # indique les numéros de réponses possibles (min 3: [1,2,3])
        valeurs_qst = []  # va sauvegarder les valeurs dans l'ordre des réponses. Exemple: [0,1,0]
        numero_qst += 1

        for rep in affichage_rep.fetchall():
            print(str(numero_rep) + ") " + rep[0])
            liste_reponses.append(numero_rep)
            valeurs_qst.append(int(rep[1]))
            numero_rep += 1

        while True:
            choix_reponse = input("Sélectionnez le numéro de la solution :\n")
            try:
                choix_reponse = int(choix_reponse)
            except ValueError:
                print("Erreur : Vous n'avez pas entré un nombre valide")
                continue
            if choix_reponse in liste_reponses:
                break
            else:
                print("Erreur : Vous n'avez pas entré un nombre valide.")

        points += valeurs_qst[choix_reponse - 1]

    return points


def save_score(points):
    decision = input("Désirez-vous sauvegarder votre score?\nTapez oui si vous êtes intéressé:\n")
    decision.lower()
    if decision == "oui":
        user_pseudo = input("Choisissez votre pseudo:\n")
        cursor.executescript(
            "INSERT INTO tb_scores (pseudo, score) VALUES ('" + user_pseudo + "\', \'" + str(points) + "');")
