##--------------------------------------------------
##     Bibliothèque TDA - Arbres
##     Suppléments : gestion d'Arbres binaires syntaxiques à partir d'équations...
##--------------------------------------------------
from Bib_TDA_PFA import *

OPERATEUR="*+/-"
PARENTHESE='()'

#Extrait le signe et les chiffres
def extrait_float(eq):
    i=eq.find(' ')
    if i!=-1:
        val=float(eq[:i])
        return eq[i+1:],val
    val=float(eq)
    return '',val
    
#Extrait l'élément significatif en début d'une partie d'une équation
def extrait_eq_val(eq) :
# la chaine de caractères doit contenir une partie d'une équation.
#   Les parenthèses, opératieurs et nombres doivent être séparés par des espaces.
#   Un nombre négatif ne doit pas avoir d'espace entre le signe - et le nombre.
# Exemple valide : ( ( ( 0.1 + 10 ) / 2 ) + ( -3.6 - 7.85 ) )
    # nombre négatif
    if eq[0] == '-':
        if eq[1]!=' ':
            return extrait_float(eq)
    # pas un nb négatif
    # parenthèse ou opérateur
    if eq[0] in PARENTHESE or eq[0] in OPERATEUR:
        return eq[2:],eq[0]
    # nombre
    return extrait_float(eq)

# création d'un arbre avec une racine et deux sous arbres
def faire_arbre_R_FG_FD(racine, fg, fd) :
    a=AB(racine)
    a.AjouterFG(fg)
    a.AjouterFD(fd)
    return a

# création d'un arbre à partir d'une équation et d'une pile, la pile doit être vide
#   initialement
def arbre_from_eq_p(eq,p) :
    eq,val=extrait_eq_val(eq)
    if val != ')':
        p.Ajouter(val)
    else :
        fd=p.Retirer()
        r=p.Retirer()
        fg=p.Retirer()
        p.Retirer()
        arbre = faire_arbre_R_FG_FD(r,fg,fd)
        if p.EstVide():
            return arbre
        p.Ajouter(arbre)
    return arbre_from_eq_p(eq,p)

# création d'un arbre à partir d'une équation sous forme de chaîne de caractères
# la chaine de caractères doit contenir une partie d'une équation.
#   Les parenthèses, opératieurs et nombres doivent être séparés par des espaces.
#   Un nombre négatif ne doit pas avoir d'espace entre le signe - et le nombre.
# Exemple valide : ( ( ( 0.1 + 10 ) / 2 ) + ( -3.6 - 7.85 ) )
def arbre_from_eq(eq) :
    p=Pile()
    if eq[0] !='(':
        eq,nb=extrait_float(eq)
        return AB(nb)
    return arbre_from_eq_p(eq,p)
