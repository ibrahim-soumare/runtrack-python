def augmenter_elements_liste(liste):
    for i in range(len(liste)):
        liste[i] += 1

L = [7, 11, 42, 39, 2]

print("Liste avant modification :", L)

augmenter_elements_liste(L)

print("Liste après modification :", L)