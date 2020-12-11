from utils.operations import *
import sqlite3

try:
    connection = sqlite3.connect("data/projet.db")
    cursor = connection.cursor()

    print("Bienvenue sur notre projet quiz !")

    categ = 'SELECT * FROM tb_categories'
    table_cat = cursor.execute(categ)
    choix_cat = display_cat(table_cat)

    difficulty = 'SELECT * FROM tb_difficulte'
    table_difficulty = cursor.execute(difficulty)
    choix_diff = display_diff(table_difficulty)

    questions = 'SELECT quest_ID, quest_name FROM tb_questions WHERE cat_ID="' + choix_cat + '"AND diff_ID=' + choix_diff
    affichage_qst = cursor.execute(questions)

    utilisateur = quiz(affichage_qst)
    print("Vous avez eu " + str(utilisateur) + " bonnes réponses.")
    save_score(utilisateur)

except Exception as msg:
    print("[Erreur]", msg)
    connection.rollback()

finally:
    connection.close()
