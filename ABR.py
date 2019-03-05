# -*- coding: utf-8 -*-
 #-*- coding: utf-8 -*-
"""
Created on Sat Dec 15 14:42:43 2018

@author: utilisateur
"""
"""Un Noeud possède une clefs, et deux fils qui sont des Noeuds"""

class Arbre:
    def __init__(self):
        self.val   = None
        self.filsG = None
        self.filsD = None
        self.pere  = None
        
    def setV(self, v):
        self.val = v
        
    def setFG(self, g):
        self.filsG = g
        
    def setFD(self, d):
        self.filsD = d
    
    def setP(self,p):
        self.pere = p
    
    def getP(self):
        return self.pere
        
    def getV(self):
        return self.val
        
    def getFG(self):
        return self.filsG
        
    def getFD(self):
        return self.filsD
    

"""Un Tas possede le nombre de clefs stockees, et un pointeur sur la racine de l'arbre"""
#class Arbre:
#    def __init__(self, nbv, r):
#        self.nbv = nbv          #nombre de valeurs dans le tas
#        self.racine = r         #racine de l'arbre
#        
#    def getR(self):
#        return self.racine
#    
#    def setR(self, r):
#        self.racine=r
#    
#    def getNbv(self):
#        return self.nbv
#        
#    def setNbv(self, newNb):
#        self.nbv = newNb   
        
def ArbreVide():
    return Arbre()
    """−>ArbreBin Renvoie l’arbre vide."""
#
#def Creer_Noeud(v, g, d):#O(1)
#    return Noeud(v, g, d)
#    """cle*Noeud*Noeud-> Noeud
#    crée un noeud de valeur v, de fils gauche g, de fils droit d"""
#    
def ArbreBinaire(e, G, D):
    a = Arbre()
    a.setFG(G)
    a.setFD(D)
    a.setV(e)
    return a
    """elt∗ArbreBin∗ArbreBin−>ArbreBin 
    Renvoie l’arbre binaire dont la racine a pour contenue, 
    et pour fils gauche et droit, respectivement G et D."""

def EstArbreVide(A): 
    return A.getV() == None
    """ArbreBin−>booleen 
    Renvoie vrai ssi l’arbre A est vide."""

def Racine(A): 
    return A.getV()
    """ArbreBin−>elt 
    Renvoie le contenu de la racine de A."""

def SousArbreGauche(A):
    return A.getFG()
    """ArbreBin−>ArbreBin 
    Renvoie une copie du sous−arbre gauche de l’arbre A."""

def SousArbreDroit(A): 
    return A.getFD()
    """ArbreBin−>ArbreBin 
    Renvoie une copie du sous−arbre droit de l’arbre A."""
    
def ABR_Ajout(x,A):
    """elt∗ArbreBin−>AVL 
    Renvoie l’AVL resultant de l’ajout de x a A."""
    
    if EstArbreVide(A): 
        return ArbreBinaire(x, ArbreVide(), ArbreVide()) 
    
    if x == Racine(A): 
        return A 
    
    if x < Racine(A): 
        return ArbreBinaire(Racine(A), 
                                        ABR_Ajout(x, 
                                                  SousArbreGauche(A)), 
                                                  SousArbreDroit(A))
    else: 
        return ArbreBinaire(Racine(A), 
                                        SousArbreGauche(A), 
                                        ABR_Ajout(x, SousArbreDroit(A)))
        
def ConsIter_ABR(liste):
    A = ArbreVide()
    
    for e in liste:
       # if(not Recherche(e,A)):
       A = ABR_Ajout(e,A)
        
    return A

def Recherche(e, A):
    if EstArbreVide(A): 
        return False
    if e == Racine(A): 
        return True
    
    if e < Racine(A): 
        return Recherche(e, A.getFG())
    else: 
        return Recherche(e, A.getFD())
    
def Afficher(A):
    if(A==None):
        return ''
    else:
        return "->" + str(A.getV()) , Afficher(A.getFG()) , Afficher(A.getFD())

def afftableau(A):
    if(A == None):
        return []
    else:
        return [A.getV()] + afftableau(A.getFG())+ afftableau(A.getFD())

import random
def main():
    l=[i for i in range(20)]
    random.shuffle(l)
#    l=[16, 14, 5, 13, 17, 1, 19, 10, 4, 18, 11, 3, 12, 9, 0, 8, 15, 6, 7, 2]
   # print(l)
    A= ArbreVide()
    for e in l:
        A = ABR_Ajout(e,A)
    print("fin de construction")
    return Afficher(A)
    
main()
