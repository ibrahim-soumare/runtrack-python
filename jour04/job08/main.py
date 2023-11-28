def compter_multiples_de_trois(liste):
    nombre_multiples_trois = 0

    for nombre in liste:
        if nombre % 3 == 0:
            nombre_multiples_trois += 1

    return nombre_multiples_trois

L = [8, 24, 48, 2, 16]

resultat = compter_multiples_de_trois(L)

print("Nombre de multiples de 3 dans la liste :", resultat)