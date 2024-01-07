
import csv
import random



class ApplicationBancaire :
    def __init__(self) :
        self.comptes = {} #comptes[numCompte] = solde
        self.clients = {}  #clients[numClient] = motpasse
        self.clientscomptes = {}  #clientscomptes[numClient] = numCompte
    

    
    def client_associe_a_compte (self,numCompte):   
        keys = list(self.clientscomptes.keys())
        values = list(self.clientscomptes.values())
        indexnumCompte = values.index(numCompte)
        numClient = keys[indexnumCompte] 
        return numClient 
    
    
    
    
    def genererNumCompte(self,numClient):
        return int(str(numClient) + str(random.randint(0, 100))) 
    
    
    
    
    def ajouterclient ( self, numClient , motpasse , numCompte , solde):
        if numClient in self.clients:
            print("Le client deja existe !")
            return False

        if numCompte in self.comptes :
            print("Le compte deja existe !")
            return False
        numCompte = self.genererNumCompte(numClient)
        self.comptes[numCompte] = solde
        self.clients[numClient] = motpasse
        self.clientscomptes[numClient] = numCompte
        print(f"Client ajouté avec succès. Numéro de compte : {numCompte}")
        return True
    
    
    
    def supprimerclient (self,numCompte):
        if numCompte not in self.comptes :
            print("Le compte n'est existe pas !")
            return False

        del self.comptes[numCompte]
        numClient = self.client_associe_a_compte(numCompte)
        del self.clients[numClient] 
        del self.clientscomptes[numClient] 
        print("Compte supprimé .")
        return True  
    
    
    
    def modifier_mote_passe_client (self,numClient , Newmotpasse):
        if numClient in self.clients:
            self.clients[numClient]= Newmotpasse
            print("Le mot de passe est modifier")
        else:
            print("Le compte est invalide ")   



    def deposer_argent (self,numCompte , argentdeposer):
        if argentdeposer <= 0:
            return False 
        if numCompte in self.comptes:
            self.comptes[numCompte] = self.comptes[numCompte] + argentdeposer
            print("Le montant ",argentdeposer,"Dhs est deposer.")
        else: 
            print("Le compte introuvable")   




    def retirer_argent (self,numCompte , argentretirer ):
        if numCompte not in self.comptes:
            print("il n'est a pas d'argent dans votre compte!")
            return False

        if argentretirer > self.comptes[numCompte]:
            print("votre solde est insuffisant!")
            return False

        self.comptes[numCompte] = self.comptes[numCompte] - argentretirer
        print("l'operation valider , Le reste est: ",self.comptes[numCompte]," Dhs")
        return True
    
 


if __name__ == "__main__":
    appBancaire = ApplicationBancaire() 
    
    print("-----------------MENU--------------------")
    while True :
            print("1. Agent")
            print("2. Client")
            choix = input("--> Choisissez une option (1 ou 2): ")

#partie agent:
            if choix == '1':
                print("1.Ajouter client")
                print("2.Supprimer client")
                choix = input("--> Choisissez une option (1 ou 2): ")

                if choix == '1':
                    numClient = int(input("Numéro du client: "))
                    motpasse = input("Code secret: ")
                    numCompte = 0
                    solde = 0
                    appBancaire.ajouterclient(numClient, motpasse,numCompte , solde )

                elif choix == '2':
                    numCompte = int(input("Numéro du compte à supprimer: "))
                    appBancaire.supprimerclient(numCompte)


#partie client:      
            elif  choix == '2':
                print("1. Modifier le mot de passe")
                print("2. Deposer de l'argent")
                print("3. Retirer de l'argent")
                print("4. Quitter")
                choix = input("--> Choisissez une option (1 - 4): ")

        
                if choix == '1':
                    numClient = int(input("Numéro du client: "))
                    Newmotpasse = input("Nouveau mot de passe: ")
                    appBancaire.modifier_mote_passe_client(numClient, Newmotpasse)
                

                elif choix == '2':
                    numClient = int(input("Numéro du client: "))
                    argentdeposer = float(input("Montant à déposer: "))
                    appBancaire.deposer_argent(numClient, argentdeposer)

                elif choix == '3':
                    numClient = int(input("Numéro du client: "))
                    argentretirer = float(input("Montant à retirer: "))
                    appBancaire.retirer_argent(numClient, argentretirer)

                elif choix == '4':
                    break

