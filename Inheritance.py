from Bib_TDA_PFA import *

class SuperPile(Pile):
    """
    La classe SuperPile hérite de la classe pile et implement les méthodes liées à cette classe
    """

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


    # Compte le nombre d'element dans la pile
    def CompterElement(self):
        count = 0
        while not self.EstVide():
            self.Retirer()
            count = count + 1
        return count 

    
    
class SuperFile(File):
    """
    La classe SuperFile hérite de la classe File et implement les méthodes liées à cette classe
    """

    def __init__(self, liste=[]):
        if len(liste) == 0 : 
            super().__init__()
            for i in range(5):
                self.Ajouter(i+1)
        else:
            super().__init__()
            for element in liste:
                self.Ajouter(element)



    # EXO 4 les éléments de rang pair dans une file (filePaire) et ceux de rang impair dans une autre file (fileImpaire)
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

        


     # EXO 4 version recursive les éléments de rang pair dans une file (filePaire) et ceux de rang impair dans une autre file (fileImpaire)
    def RangerPairImpairRecursive(self, fp, fi):
        if not self.EstVide():
            if self.Premier() % 2 == 0:
                fp.Ajouter(self.Premier())
            else:
                fi.Ajouter(self.Premier())
            self.RangerPairImpairRecursive(fp, fi)
        

            
    # Affiche les éléments de la file        
    def Afficher(self):
        if not self.EstVide():
            print(self.Retirer())


    # Affichage recursif 
    def AfficherRecursive(self):
        if  not self.EstVide():
            print(self.Retirer())
            self.AfficherRecursive()
