__author__ = 'YEHADJI Abilé ALexis-Honoré'
__license__ = 'BSD 3 Simplified'
__version__ = '0.1.0'
__email__ = 'yehadjialexis@gmail.com'


# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sqlite3


def nombre_manquant(tableau):
    x = min(tableau)
    y = max(tableau)
    somme_reelle = (y * (y + 1) // 2) - ((x - 1) * x // 2)
    somme_actuelle = sum(tableau)
    nombre_manquant = somme_reelle - somme_actuelle

    conn = sqlite3.connect('nombre_manquant.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS manquants (nombre INT)')
    cursor.execute('INSERT INTO manquants (nombre) VALUES (?)', (nombre_manquant,))
    conn.commit()
    conn.close()

    return nombre_manquant


#methode 2
def nombre_manquant2(tab):
    x = min(tab)
    y = max(tab)
    tous_les_nombres = set(range(x, y + 1))
    manquant = list(tous_les_nombres - set(tab))[0]

    conn = sqlite3.connect('nombre_manquant.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS manquants (nombre INT)')
    cursor.execute('INSERT INTO manquants (nombre) VALUES (?)', (manquant,))
    conn.commit()
    conn.close()

    return manquant



if __name__ == "__main__":
    tableau = [1, 2, 3, 4, 5, 7]
    nb = nombre_manquant2(tableau)
    print(f"Le nombre manquant est : {nb}")

