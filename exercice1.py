__author__ = 'YEHADJI Abilé ALexis-Honoré'
__license__ = 'BSD 3 Simplified'
__version__ = '0.1.0'
__email__ = 'yehadjialexis@gmail.com'


# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd

#methode 1
def transform(chain):
    entiers_array1 = set(chain[0].split(", "))
    entiers_array2 = set(chain[1].split(", "))

    intersection = entiers_array1.intersection(entiers_array2)
    sorted_intersection = sorted(map(int, intersection), reverse=True)

    if sorted_intersection:
        return ','.join(map(str, sorted_intersection)) + ":alexis_yehadji_master1"
    else:
        return 'None'



#methode 2
def transform2(chain):
    entiers_array1 = chain[0].split(", ")
    entiers_array2 = chain[1].split(", ")

    serie1 = pd.Series(entiers_array1)
    serie2 = pd.Series(entiers_array2)

    intersection = serie1[serie1.isin(serie2)]

    if len(intersection) > 0:
        intersection = sorted(intersection, reverse=True)
        chaine_finale = ",".join(intersection)
        chaine_finale += ":alexis_yehadji_master1"
        return chaine_finale
    else:
        return 'None'


def trouver_element(tableau, valeur):
    elements_trouves = [element for element in tableau if element == valeur]
    return elements_trouves

# Press the green button in the gutter to run the script.
# vous ne modifierez rien après cette ligne
if __name__ == "__main__":
    arr1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    out = transform2(arr1)
    print(out) # doit afficher ---> 31,4,1:nom_prenom_classe
    arr3 = ["9, 3, 5, 7, 14", "10, 2, 6, 16, 15"]
    out = transform2(arr3)
    print(out) # doit afficher ---> None

