from utils.GUI import *
from utils.requetes import *
from utils.operations import *

try:

    choix_cat = display_cat(requete_categ())
    choix_diff = display_diff(requete_diffic())

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
