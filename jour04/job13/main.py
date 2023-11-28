def supprimer_doublons(liste):
    liste_sans_doublons = []

    for element in liste:
        est_present = False
        for unique_element in liste_sans_doublons:
            if element == unique_element:
                est_present = True
                break
        if not est_present:
            liste_sans_doublons.append(element)

    return liste_sans_doublons

# Exemple d'utilisation
ma_liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
liste_sans_doublons = supprimer_doublons(ma_liste)
print("Liste sans doublons:", liste_sans_doublons)