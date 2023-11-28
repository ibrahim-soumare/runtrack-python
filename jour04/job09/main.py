def recuperer_infos_liste(liste):
    if not liste:
        print("La liste est vide.")
        return None

    valeur = liste[0]
    maximum = max(liste)
    minimum = min(liste)

    return valeur, maximum, minimum

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

resultat = recuperer_infos_liste(L)

if resultat is not None:
    valeur, maximum, minimum = resultat
    print("Valeur de la liste :", valeur)
    print("Maximum de la liste :", maximum)
    print("Minimum de la liste :", minimum)