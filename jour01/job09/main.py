class Produit:
    def __init__(self, nom, prix_unitaire, quantite_stock):
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.quantite_stock = quantite_stock

    def afficher_informations(self):
        print(f"Produit : {self.nom}")
        print(f"Prix unitaire : {self.prix_unitaire} €")
        print(f"Quantité en stock : {self.quantite_stock} unités")
        print()

    def mettre_a_jour_prix(self):
        self.prix_unitaire *= 1.10  

    def ajouter_stock(self, quantite_ajoutee):
        self.quantite_stock -= quantite_ajoutee


produit1 = Produit("gourde", 10.0, 100)

print("Informations initiales du produit :")
produit1.afficher_informations()

quantite_achetee = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))
produit1.ajouter_stock(quantite_achetee)

print("Informations après l'ajout de produits en stock :")
produit1.afficher_informations()

produit1.mettre_a_jour_prix()

print("Informations après la mise à jour du prix suite à l'inflation :")
produit1.afficher_informations()