def tri_selection_croissante(liste):
    n = len(liste)
    for i in range(n - 1):
        indice_min = i
        for j in range(i + 1, n):
            if liste[j] < liste[indice_min]:
                indice_min = j

        liste[i], liste[indice_min] = liste[indice_min], liste[i]

def arrondir_et_trier(liste):
    liste_arrondie = [int(nombre + 0.5) for nombre in liste]

    tri_selection_croissante(liste_arrondie)

    return liste_arrondie

ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

resultat = arrondir_et_trier(ma_liste)

print("Liste arrondie et triée :", resultat)