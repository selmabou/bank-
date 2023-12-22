import csv
import random

#les dictionnaires

comptes = {}
clients = {}
clientscomptes = {} # {numclient : numcompte} 

#csv
with open("clients.csv", 'r') as file:
    csvreader = csv.reader(file)

    for row in csvreader:
        clients[row[0]] = row[1]  


#Les Fonctions :

def client_associe_a_compte (numCompte):
    keys = list(clientscomptes.keys())
    values = list(clientscomptes.values())
    indexnumCompte = values.index(numCompte)
    numClient = keys[indexnumCompte] 
    return numClient



#Fonction ajouter
def ajouterclient ( numClient , motpasse , numCompte , solde):
    if numClient in clients:
        print("Le client deja existe !")
        return False

    if numCompte in comptes :
        print("Le compte deja existe !")
        return False
    numCompte = genererNumCompte(numClient)
    comptes[numCompte] = solde
    clients[numClient] = motpasse
    clientscomptes[numClient] = numCompte
    print(f"Client ajouté avec succès. Numéro de compte : {numCompte}")
    return True




#Fonction supprimer
def supprimerclient (numCompte):
    if numCompte not in comptes :
        print("Le compte n'est existe pas !")
        return False

    del comptes[numCompte]
    numClient = client_associe_a_compte(numCompte)
    del clients[numClient] 
    del clientscomptes[numClient] 
    print("Compte supprimé .")
    return True  



#Fonction modifier le mot de passe
def modifier_mote_passe_client (numClient , Newmotpasse):
    if numClient in clients:
        clients[numClient]= Newmotpasse
        print("Le mot de passe est modifier")
    else:
        print("Le compte est invalide ")   



#Fonction deposer l'argent
def deposer_argent (numCompte , argentdeposer):
    if argentdeposer <= 0:
        return False 
    if numCompte in comptes:
        comptes[numCompte] = comptes[numCompte] + argentdeposer
        print("Le montant ",argentdeposer,"Dhs est deposer.")
    else: 
        print("Le compte introuvable")   

#Fonction Retirer 
def retirer_argent (numCompte , argentretirer ):
    if numCompte not in comptes:
        print("il n'est a pas d'argent dans votre compte!")
        return False

    if argentretirer > comptes[numCompte]:
        print("votre solde est insuffisant!")
        return False

    comptes[numCompte] = comptes[numCompte] - argentretirer
    print("l'operation valider , Le reste est: ",comptes[numCompte]," Dhs")
    return True


#Fonction lambda (generer le num de compte)
def genererNumCompte(numClient):
    return int(str(numClient) + str(random.randint(0, 100)))            




while True :
    print("1. Agent")
    print("2. Client")
    choix = input(" Choisissez une option (1 ou 2): ")

#partie agent:
    if choix == '1':
        print("1.Ajouter client")
        print("2.Supprimer client")
        choix = input("Choisissez une option (1 ou 2): ")

        if choix == '1':
            numClient = int(input("Numéro du client: "))
            motpasse = input("Code secret: ")
            numCompte = 0
            solde = 0
            ajouterclient(numClient, motpasse,numCompte , solde )

        elif choix == '2':
            numCompte = int(input("Numéro du compte à supprimer: "))
            supprimerclient(numCompte)


#partie client:      
    elif  choix == '2':
        print("1. Modifier le mot de passe")
        print("2. Deposer de l'argent")
        print("3. Retirer de l'argent")
        print("4. Quitter")
        choix = input(" Choisissez une option (1 - 4): ")

        
        if choix == '1':
            numClient = int(input("Numéro du client: "))
            Newmotpasse = input("Nouveau mot de passe: ")
            modifier_mote_passe_client(numClient, Newmotpasse)
                

        elif choix == '2':
            numClient = int(input("Numéro du client: "))
            argentdeposer = float(input("Montant à déposer: "))
            deposer_argent(numClient, argentdeposer)

        elif choix == '3':
            numClient = int(input("Numéro du client: "))
            argentretirer = float(input("Montant à retirer: "))
            retirer_argent(numClient, argentretirer)

        elif choix == '4':
            break

       
   





   


        


