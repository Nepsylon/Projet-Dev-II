# dictionnaire test servant pour le hardcoding

questions = {
    "Que signifie les initiales de RAM ?\n": {"1:Random Access Memory": True,
                                              "2:Repetitive Access Memory": False,
                                              "3:Render Acceleration Material": False},
    "SSD est l'abréviation de :\n": {"1:Solid Snake Drive": False,
                                     "2:Solid State Drive": True,
                                     "3:Strong State Drive": False,
                                     "4:Strong Snake Drive": False},
    "Quel langage de programmation est le plus récent ?\n": {"1:Java": True,
                                                             "2:C": False,
                                                             "3:Python": False,
                                                             "4:PHP": False}
}

if __name__ == "__main__":
    def example():
        """" Fait par Christopher Fauconnier """
        qst_actuelle = 1  # variable qui va afficher dans la console le n° de qst
        result = 0  # variable conservant le "score" de l'user

        # boucle parcourant le dictionnaire questions
        for i in questions:
            qst = questions[i].keys()  # variable contenant les clés du dictionnaire imbriqué
            qst2 = list(questions[i].values())  # liste qui contient des booléens et va les comparer avec le choix user
            print(qst_actuelle, ")", i)  # affiche la question en console

            # boucle pour afficher les différentes réponses
            for j in qst:
                print(j)

            """ Fait par Simon Kinet"""
            choix = int(input('Choisissez le numéro de la réponse: '))  # variable stockant un entier décidé par l'utilisateur
            while choix > len(questions[i]) or choix <= 0:
                print("Nombre invalide")
                choix = int(input(
                    'Choisissez le numéro de la réponse: '))  # variable stockant un entier décidé par l'utilisateur
            else:
                choix -= 1  # on transforme en indice pour se déplacer dans la liste "qst2"

                # test du choix avec la valeur dans la liste "qst2"
                if qst2[choix] == True:
                    result += 1
                else:
                    print("Mauvaise Réponse !")
            qst_actuelle += 1

        print("Vous avez réussi", result, "questions !")

example()

'''
class Qst_user:
    def __init__(self, question, réponse1, valeur1, réponse2, valeur2, réponse3, valeur3, réponse4, valeur4):

        self.reponses = {réponse1: valeur1, réponse2: valeur2, réponse3: valeur3, réponse4: valeur4}
        self.question = {question: self.reponses}

    def __str__(self):
        return str(self.question)


test = Qst_user("je m'appelle :", "Chris", True, "Simon", False, "David", False, "Georges", False)
print(test.question["je m'appelle :"])
'''