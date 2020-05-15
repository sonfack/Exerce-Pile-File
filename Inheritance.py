from Bib_TDA_PFA import *

class SuperPile(Pile):

    def __init__(self, liste=[]):
        if len(liste) == 0: 
            super().__init__()
            for i in range(5):
                self.Ajouter(i+1)
        else:
            super().__init__()
            for element in liste:
                self.Ajouter(element)



    
    # EXO 1
    # Affichage iteratif 
    def Afficher(self):
        while (not self.EstVide()):
            print(self.Retirer())




    # Affichage recursif inverse
    def AfficherRecursiveInverse(self):
        if not self.EstVide():
            val = self.Retirer()
            self.AfficherRecursiveInverse()
            print(val)


            
    # Affichage recursif 
    def AfficherRecursive(self):
        if  not self.EstVide():
            print(self.Retirer())
            self.AfficherRecursive()





            

    def CompterElement(self):
        count = 0
        while not self.EstVide():
            self.Retirer()
            count = count + 1
        return count 




    




    


    
class SuperFile(File):

    def __init__(self, liste=[]):
        if len(liste) == 0 : 
            super().__init__()
            for i in range(5):
                self.Ajouter(i+1)
        else:
            super().__init__()
            for element in liste:
                self.Ajouter(element)



    # EXO 4
    def RangerPairImpair(self):
        filePair = File()
        fileImpair = File()
        count = 0
        while not self.EstVide():
            if count % 2 == 0:
                filePair.Ajouter(self.Retirer())
                count = count + 1
            else:
                fileImpair.Ajouter(self.Retirer())
                count = count + 1
        return filePair, fileImpair

        






    
    def RangerPairImpairRecursive(self, fp, fi):
        if not self.EstVide():
            if self.Premier() % 2 == 0:
                fp.Ajouter(self.Premier())
            else:
                fi.Ajouter(self.Premier())
            self.RangerPairImpairRecursive(fp, fi)
        





            
            
    def Afficher(self):
        if not self.EstVide():
            print(self.Retirer())


    # Affichage recursif 
    def AfficherRecursive(self):
        if  not self.EstVide():
            print(self.Retirer())
            self.AfficherRecursive()
