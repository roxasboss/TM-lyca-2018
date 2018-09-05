import numpy as np

def produit_matrice_vecteur():
    #initialisation d' une liste pour le permier vecteur-colonne/matrice:
    a1 = []
    nombre_de_ligne= int(input("nombre de ligne de la 1ère matrice: "))
    #une boucle pour former remplir la liste a1 selon le nombre de lignes voulus avec l'input de l'utilisateur :
    while nombre_de_ligne >0:
        #supression des espaces comme valeur pour permettre d'utiliser des espaces afin d'avoir des nombres:
        row = list(input("nombres sur la ligne: ").split(" "))
        #liste compréshensive pour transformer l'input en integrer afin de pouvoir faire des calculs:
        row = [int(i) for i in row]
        a1.append(row)
        nombre_de_ligne-=1
    np_a1 =np.array(a1)
    #mêmes intstructions que pour le premier vecteur colonne/matrice:
    a2 = []
    nombre_de_ligne1= int(input("nombre de ligne de la 2ème matrice: "))
    while nombre_de_ligne1 >0:
        row1 = list(input("nombres sur la ligne: ").split(" "))
        row1 = [int(i) for i in row1]
        a2.append(row1)
        nombre_de_ligne1-=1
    np_a2 = np.array(a2)
    #prduit des 2 matrice(s) ou vecteur(s) colonne(s):
    return np.dot(np_a1,np_a2)
print(produit_matrice_vecteur())














