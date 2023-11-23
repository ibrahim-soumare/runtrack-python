def verifier_pair_impair(nombre):
   
    if isinstance(nombre, int) and nombre >= 0:
       
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre pair.")
        else:
            print(f"{nombre} est un nombre impair.")
    else:
        print("incorrect")


verifier_pair_impair(5)
verifier_pair_impair(80)
verifier_pair_impair(17)
verifier_pair_impair(-3)
verifier_pair_impair(50)
