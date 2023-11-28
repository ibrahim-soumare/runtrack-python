def remplacer_par_somme_voisins(liste, index):
    if 0 < index < len(liste) - 1:
        somme_voisins = liste[index - 1] + liste[index + 1]
        liste[index] = somme_voisins

L = [1, 2, 3, 4, 5]

print("La liste sans aucun changement",L)

deuxieme_valeur = L[1]
print("Deuxième valeur de la liste :", deuxieme_valeur)

remplacer_par_somme_voisins(L, 3)

print("Tableau après la mise à jour :", L)

derniere_valeur = L[-1]
print("Dernière valeur de la liste :", derniere_valeur)