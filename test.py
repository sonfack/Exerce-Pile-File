from Inheritance import *

Sp1 = SuperPile([0, 1, 5, 9, 12])
Sp2 = SuperPile([2, 3, 4, 5, 5, 6, 7, 8])


def creerPile():
    mapile = input("Elements pile : ")
    liste = mapile.split()

    nf = File()
    for element in liste:
        nf.Ajouter(int(element))

    return nf



newpile = creerPile()

print(newpile.items)
















"""
fl = File()

print(Sp1.items)
print(Sp2.items)


def alternance(pl1, pl2):
    fl = File()
    while not pl1.EstVide() and not pl2.EstVide():
        fl.Ajouter(pl1.Retirer())
        fl.Ajouter(pl2.Retirer())
        
    while not pl1.EstVide():
        fl.Ajouter(pl1.Retirer)
        
    while not pl2.EstVide():
        fl.Ajouter(pl2.Retirer())

    return fl

fl = File()

print(Sp1.items)
print(Sp2.items)



def alternanceRecursive(pl1, pl2, fl):
    if not pl1.EstVide() and not pl2.EstVide():
        fl.Ajouter(pl1.Retirer())
        fl.Ajouter(pl2.Retirer())
        
        alternanceRecursive(pl1, pl2, fl)
        
    elif not  pl1.EstVide():
        fl.Ajouter(pl1.Retirer())
        alternanceRecursive(pl1, pl2, fl)
        
    elif not pl2.EstVide(): 
        fl.Ajouter(pl2.Retirer())
        alternanceRecursive(pl1, pl2, fl)


#print(alternance(Sp1, Sp2).items)
alternanceRecursive(Sp1, Sp2, fl)
print(fl.items)

"""


























"""
Sf = SuperFile([2, 3, 4, 5, 5, 6, 7, 8])

fp, fi = Sf.RangerPairImpair()
print(fp.items)
print(fi.items)

def AjouterSeparer(liste):
    nf = File()
    for element in liste:
        nf.Ajouter(element)

    print("Nouvelle file", nf.items)

    fp, fi = RangerPairImpair(nf)

    print("Rang pair ", fp.items)
    print("Rang impair ", fi.items)

    

    
def RangerPairImpair(fl):
        filePair = File()
        fileImpair = File()
        count = 0
        while not fl.EstVide():
            if count % 2 == 0:
                filePair.Ajouter(fl.Retirer())
                count = count + 1
            else:
                fileImpair.Ajouter(fl.Retirer())
                count = count + 1
        return filePair, fileImpair


    

AjouterSeparer([3,6,8,4,7,9,2])
    
"""





















#print(Sp1.CompterElement())
"""
def deuxRetour():
    p = 23
    t = 89
    return p, t

p, t = deuxRetour()

print(p)
print(t)

"""

"""
Sf = SuperFile([],8)
fp, fi = Sf.RangerPairImpair()

print(fp.items)
print(fi.items)


def mrg (pf1,pf2) :
    pf3 = Pile()
    while (not pf1.EstVide()) and (not pf2.EstVide()) :
        if pf1.Premier() < pf2.Premier() :
            pf3.Ajouter(pf1.Retirer())
        else :
            pf3.Ajouter(pf2.Retirer())
    while not pf1.EstVide() :
        pf3.Ajouter(pf1.Retirer())
    while not pf2.EstVide() :
        pf3.Ajouter(pf2.Retirer())

    return pf3


print(Sp1.items)
print(Sp2.items)
p = mrg(Sp1, Sp2)
print(p.items)

"""

"""

Sp.AfficherRecursive()
Sp = SuperPile()
Sp.AfficherRecursiveInverse()

Sf = SuperFile()








# Affichage recursif 
def AfficherRecursive(pile_file):
    if  not pile_file.EstVide():
        print(pile_file.Retirer())
        AfficherRecursive(pile_file)




"""
        
"""
# Affichage recursif inverse
    def AfficherRecursiveInverse(self):
        if not self.EstVide():
            val = self.Retirer()
            self.AfficherRecursiveInverse()
            print(val)


# Affichage recursif 
def AfficherRecursive(pile_file):
    if  not pile_file.EstVide():
        print(pile_file.Retirer())
        AfficherRecursive(pile_file)

AfficherRecursive(Sp)
AfficherRecursive(Sf)
"""
