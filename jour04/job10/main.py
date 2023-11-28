def produit_dans_intervalle(liste, borne_inf, borne_sup):
    produit = 1

    for nombre in liste:
        if borne_inf <= nombre <= borne_sup:
            produit *= nombre

    return produit

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

borne_inf = 25
borne_sup = 90

resultat = produit_dans_intervalle(L, borne_inf, borne_sup)

print("Produit des valeurs dans l'intervalle [25, 90] :", resultat)