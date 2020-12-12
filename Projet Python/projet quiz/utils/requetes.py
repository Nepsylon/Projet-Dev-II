import sqlite3

connection = sqlite3.connect("data/projet.db")
cursor = connection.cursor()


def requete_categ():
    categ = 'SELECT * FROM tb_categories'
    table_cat = cursor.execute(categ)

    return table_cat


def requete_diffic():
    difficulty = 'SELECT * FROM tb_difficulte'
    table_difficulty = cursor.execute(difficulty)

    return table_difficulty


def requete_commu():
    pass
