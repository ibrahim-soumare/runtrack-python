def afficher_tables_multiplication(N):
    for i in range(1, N + 1):
        print(f"\nTable de multiplication de {i} :")
        for j in range(1, 11):
            print(f"{i} * {j} = {i * j}")

N = int(input("Veuillez saisir un entier supérieur à zéro : "))
afficher_tables_multiplication(N)

