import sqlite3

def display_cat():
    # Affiche les catégories
    for elem in affichage_categ:
        print(elem[1], ":", elem[0])
    choix_cat = input('Veuillez choisir la lettre de la catégorie qui vous intéresse :\n').upper()
    return choix_cat

def display_diff():
    #Affiche les difficultés
    for elem_diff in affichage_difficulty:
        print(elem_diff[1],":",elem_diff[0])
    choix_diff = input('Veuillez choisir la difficulté :\n')
    return choix_diff


try:

    connection = sqlite3.connect("data/projet.db")
    cursor = connection.cursor()

    print("Bienvenue sur notre projet quiz !")


    categ = 'SELECT * FROM tb_categories'
    affichage_categ = cursor.execute(categ)
    choix_cat = display_cat()


    difficulty = 'SELECT * FROM tb_difficulte'
    affichage_difficulty = cursor.execute(difficulty)
    choix_diff = display_diff()


    questions = 'SELECT quest_ID, quest_name FROM tb_questions WHERE cat_ID="'+choix_cat+'"AND diff_ID='+choix_diff
    affichage_qst = cursor.execute(questions)

    for qst in affichage_qst.fetchall():
        print(qst[1])
        affichage_rep = cursor.execute('SELECT rep_name FROM tb_reponses WHERE quest_ID = ?', (qst[0],))
        for rep in affichage_rep.fetchall():
            print(rep[0])

except Exception as msg:
    print("[Erreur]", msg)
    connection.rollback()

finally:
    connection.close()
