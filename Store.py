# On voudrait faciliter la gestion d’un magasin de vente de prêt à porter.
# Les articles du magasin possèdent : une référence (un code), un libellé et un prix unitaire hors taxe.
# A partir d’une quantité d’un article acheté à un prix hors taxe, on souhaite établir les factures de 3 clients
# dont on connaît leurs noms. On suppose que chacun d’eux a acheté un seul article (quantité = 1).
# La facture fera apparaître le nom du client et le montant toute taxe (TTC), sachant qu’on applique un taux de
# TVA de 15% et le client bénéficie d'une remise de 2% sur le montant de ces achats.

# Donner le nom et prénom du client n`1 : Ali Mohamed
# Donner le nombre d’article pour le client n`1: 2
# Donner le prix de l’article 1: 15.87
# Donner le prix de l’article 2 : 9.23

# Donner le nom et prénom du client n`2 : Madani Brahim
# Donner le nombre d’article pour le client n`2: 5
# Donner le prix de l’article 1: 5.87
# Donner le prix de l’article 2 : 19.23
# Donner le prix de l’article 3 : 23.21
# Donner le prix de l’article 4 : 4.23
# Donner le prix de l’article 5 : 16.45

# _______________________________
# Facture
# _______________________________
# Le Total à payer pour le client Ali Mohamed est : 25.1 DH
# Le Total à payer pour le client Madani Brahim est : 68.99 DH
# Le Total à payer pour le client Amrani Khalid : 78.62 DH

ClientsNames = []
ClientsAmounts = []

for i in range(3):
    ClientsNames.append(input(f"enter FULLNAME For client number [{i+1}]: "))
    ArticlesNumber = int(input(f"enter number of ARTICLEs for client [{i+1}]: "))
    
    TotalArticlesAmount = 0
    for j in range(ArticlesNumber):
        HT = float(input(f"enter the price for article number[{j+1}]: "))
        TotalArticlesAmount = TotalArticlesAmount + HT

    TVA = TotalArticlesAmount * 15 / 100
    TTC = TotalArticlesAmount + TVA 
    AmountWithDiscount = TTC - TTC * 2/100

    ClientsAmounts.append(AmountWithDiscount)
    print("\n\n")


print("_______________________________")
print("        FACTURE")
print("_______________________________")
for i in range(3):
    print("Total amount for client [ ",ClientsNames[i],"] is : ",ClientsAmounts[i])

