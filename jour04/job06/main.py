L = [1, 2, 3, 4, 5]
print(L)
l = len(L)
changement = L[0]
L[0] = L[l-1]
L[l-1] = changement
print (L) 