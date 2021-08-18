import tkinter
from tkinter import *
from tkinter import messagebox as mb
import sqlite3

connection = sqlite3.connect("data/projet.db")
cursor = connection.cursor()

try:
    fenetre = tkinter.Tk()
    categories = dict()
    difficultes = dict()
    questions = []
    reponses = []
    num_reponses = []
    valeur_cat = ''
    valeur_diff = ''

    class Quiz:
        def __init__(self):
            self.question_number = 0
            self.reponse_selected = IntVar()
            self.reponses = self.radiobouton()
            self.ques = self.question(self.question_number)
            self.display_reponses(self.question_number)
            self.boutons()
            self.correct = 0

        def question(self, question_number):  # fonction qui initialise la question
            requete_donnees()
            t = Label(fenetre, text="Question pour un champion",
                      width=90, bg="orange", fg="white", font=(25))
            t.place(x=0, y=0)
            question_number = Label(
                fenetre, text=questions[question_number], bg="grey", font=(10))
            question_number.place(x=70, y=100)
            return question_number

        def radiobouton(self):  # Fonction qui initialise les boutons radios des réponses
            val = 0
            b = []
            taille = 150
            while val < 3:
                btn = Radiobutton(fenetre, text=" ", variable=self.reponse_selected,
                                  command=self.suivant, value=val + 1, bg="grey", font=(8))
                b.append(btn)
                btn.place(x=100, y=taille)
                val += 1
                taille += 40
            return b

        # Fonction qui met les réponses associé aux boutons radios
        def display_reponses(self, question_number):
            val = 0
            self.reponse_selected.set(0)
            self.ques['text'] = questions[question_number]
            for op in reponses[question_number]:
                self.reponses[val]['text'] = op
                val += 1

        def boutons(self):  # Fonction pour les boutons existants
            bouton_accueil = Button(fenetre, text="Accueil", command=accueil,
                                    width=10, bg="orange", fg="white", font=(16))
            bouton_accueil.place(x=100, y=380)
            bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy,
                                    width=10, bg="orange", fg="white", font=(16))
            bouton_quitter.place(x=750, y=380)

        # Fonction qui récupère la valeur cochée et vérifié avec num_reponses
        def verif_reponse(self, question_number):
            if self.reponse_selected.get() == num_reponses[question_number]:
                return True

        def suivant(self):  # Fonction qui permet de passer à la suite
            if self.verif_reponse(self.question_number):
                self.correct += 1
            self.question_number += 1
            if self.question_number == len(questions):
                self.resultat()
            else:
                self.display_reponses(self.question_number)

        def resultat(self):  # Fonction qui calcule les points et affiche le résultat
            destroy()
            score = int(self.correct / len(questions) * 100)
            correct = "Vous avez obtenu le score de " + \
                str(self.correct) + "/10\nFélicitations!"
            Label(fenetre, text=correct, bg="grey", font=(10)).place(x=350, y=150)


    def requete_donnees():  # Fonction qui permet de récupérer les données de la db
        requete_questions = 'SELECT quest_ID, quest_name FROM tb_questions WHERE cat_ID="' + \
            valeur_cat + '"AND diff_ID=' + str(valeur_diff)
        qcm = cursor.execute(requete_questions)
        temporaire = dict()

        for qst in qcm.fetchall():
            requete_donnees = cursor.execute(
                'SELECT rep_name FROM tb_reponses WHERE quest_ID = ?', (qst[0],))
            questions.append(qst[1])
            for i in requete_donnees.fetchall():
                if qst[1] in temporaire:
                    temporaire[qst[1]] += list(i)
                else:
                    temporaire[qst[1]] = list(i)

            requete_valeurs = cursor.execute(
                'SELECT value, rep_ID FROM tb_reponses WHERE quest_ID = ?', (qst[0],))
            indice = 1
            for val, id in requete_valeurs.fetchall():
                if val == 1:
                    num_reponses.append(indice)
                else:
                    indice += 1

        for valeur in temporaire.values():
            reponses.append(valeur)


    def requete_categ():  # Fonction qui permet de récupérer les données de la db et les met dans un dictionnaire categories
        global categories
        categ = 'SELECT * FROM tb_categories'
        cursor.execute(categ)
        table_cat = cursor.fetchall()
        for elem in table_cat:
            categories[elem[0]] = elem[1]


    def requete_diff():  # Fonction qui permet de récupérer les données de la db et les met dans un dictionnaire difficultes
        global difficultes
        diff = 'SELECT * FROM tb_difficulte'
        cursor.execute(diff)
        table_diff = cursor.fetchall()
        for elem in table_diff:
            difficultes[elem[0]] = elem[1]


    def select_cat():  # Fonction qui récupère la valeur de la catégorie séléctionnée et passer à la suite
        global valeur_cat
        valeur_cat = var_cat.get()
        destroy()
        affiche_difficultes()


    def select_diff():  # Fonction qui récupère la valeur de la difficulté séléctionnée et passer à la suite
        global valeur_diff
        valeur_diff = var_diff.get()
        destroy()
        Quiz()


    def affiche_categories():  # Fonction qui affiche les catégories
        global categories
        taille = 150
        Label(fenetre, text="Choissisez une catégorie :",
              bg="grey", font=(10)).place(x=70, y=100)
        for (text, value) in categories.items():
            Radiobutton(fenetre, text=value, variable=var_cat, value=text,
                        command=select_cat,  bg="grey", font=(8)).place(x=100, y=taille)
            taille += 40


    def affiche_difficultes():  # Fonction qui affiche les difficultes
        global difficultes
        destroy()
        taille = 150
        Label(fenetre, text="Choissisez une difficulté :",
              bg="grey", font=(10)).place(x=70, y=100)
        for (text, value) in difficultes.items():
            Radiobutton(fenetre, text=value, variable=var_diff, value=text,
                        command=select_diff, bg="grey", font=(8)).place(x=100, y=taille)
            taille += 40


    var_cat = StringVar(fenetre, '0')
    var_diff = StringVar(fenetre, 'A')


    def accueil():  # Fonction remet tout à zéro et relance le script
        destroy()
        global categories, difficultes, questions, reponses, num_reponses, valeur_cat, valeur_diff
        categories = dict()
        difficultes = dict()
        questions = []
        reponses = []
        num_reponses = []
        valeur_cat = ''
        valeur_diff = ''

        core()


    def core():  # Fonction qui lance les différentes fonctions principales
        bienvenue.destroy()
        boutonStart.destroy()
        requete_categ()
        requete_diff()
        affiche_categories()


    def destroy():  # Fonction qui nettoie l'écran
        for c in fenetre.winfo_children():
            c.destroy()


    fenetre.title("Question pour un champion")
    fenetre.geometry("1000x500")
    fenetre.resizable(0, 0)
    fenetre.configure(bg="grey")
    # ---------------------------------------------------------------------------
    bienvenue = Label(fenetre, text='Bienvenue dans notre projet quiz !',
                      width=90, bg="orange", fg="white", font=(25))
    bienvenue.pack()

    boutonStart = Button(fenetre, text="Commencer", command=core,
                         width=10, bg="orange", fg="white", font=(16))
    boutonStart.pack(expand=YES)
    # ---------------------------------------------------------------------------
    fenetre.mainloop()

except Exception as msg:
    print("[Erreur]", msg)
    connection.rollback()

finally:
    connection.close()

if __name__ == '__main__':
    accueil()