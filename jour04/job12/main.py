def tri_selection_croissante(liste):
    for i in range(len(liste)):
        indice_minimum = i
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[indice_minimum]:
                indice_minimum = j

        liste[i], liste[indice_minimum] = liste[indice_minimum], liste[i]

ma_liste = [64, 25, 12, 22, 11]

print("Liste avant le tri :", ma_liste)

tri_selection_croissante(ma_liste)

print("Liste après le tri croissant :", ma_liste)