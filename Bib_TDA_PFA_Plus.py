##--------------------------------------------------
##     Bibliothèque TDA Piles - Files - Arbres
##     Suppléments : affichage, ajout dasn un ABR...
##--------------------------------------------------
import copy
from Bib_TDA_PFA import *
##--------------------------------------------------
##     Piles - Files
##--------------------------------------------------
def Affiche(fp):
    inter=copy.deepcopy(fp)
    while not inter.EstVide():
        print(inter.Retirer(), end=" ")
    print()
        
##--------------------------------------------------
##     Arbres Binaires : AB 
##--------------------------------------------------
def ParcoursPre(A) :
    if not A.EstVide():
        print(A.GetRacine(),end=" ")
        ParcoursPre(A.GetSAG())
        ParcoursPre(A.GetSAD())

def ParcoursSym(A) :
    if not A.EstVide():
        ParcoursSym(A.GetSAG())
        print(A.GetRacine(),end=" ")
        ParcoursSym(A.GetSAD())

def ParcoursPost(A) :
    if not A.EstVide():
        ParcoursPost(A.GetSAG())
        ParcoursPost(A.GetSAD())
        print(A.GetRacine(),end=" ")

def Rechercher(e, A) :
    if  A.EstVide():
        return None
    else :
        if e < A.GetRacine():
            return Rechercher(e, A.GetSAG())
        else :
            if e > A.GetRacine() :
                return Rechercher(e, A.GetSAD())
            else :
                return A

def Inserer(e, A) :
    if A.EstVide():
        A.SetRacine(e)
    else :
        if e < A.GetRacine():
            if A.GetSAG().EstVide() :
                A.AjouterFG(e)
            else :
                Inserer(e,A.GetSAG())
        else :
            if A.GetSAD().EstVide() :
                A.AjouterFD(e)
            else :
                Inserer(e,A.GetSAD())
                