# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:18:10 2018

@author: utilisateur
"""
from math import log
import random
#exercice 1

def inf(cle1, cle2):
#    val32_1 = [(cle1 >> x) & 0xFFFFFF for x in reversed(range(0, 128, 32))]
#    val32_2 = [(cle2 >> x) & 0xFFFFFF for x in reversed(range(0, 128, 32))]
#    """decomposition en 4 entiers sur 32 bits pour chaque clefs"""
#    for i in range(0, 4):
#        if val32_1[0] < val32_2[1]:
#            return True
#        if val32_1[0] > val32_2[1]:
#            return False
    return cle1 < cle2
    """cle*cle->boolean
    prend deux nombre 128 bits et renvoie true si cle1< cle2"""
            
def eg(cle1, cle2):
   # val32_1 = [(cle1 >> x) & 0xFFFFFF for x in reversed(range(0, 128, 32))]
   # val32_2 = [(cle2 >> x) & 0xFFFFFF for x in reversed(range(0, 128, 32))]    
    return cle1 == cle2
    """cle*cle->boolean
    renvoie le test d'egalite entre 2 nombre 128 bit"""
    

#---------------------implementation en arbre----------------------------------
"""Un Noeud possède une clefs, et deux fils qui sont des Noeuds"""
class Noeud:
    def __init__(self, v, g, d):
        self.val   = v
        self.filsG = g
        self.filsD = d
        
    def setFG(self, g):
        self.filsG = g
        
    def setFD(self, d):
        self.filsD=d
    
    def setV(self, v):
        self.val = v
        
    def getV(self):
        return self.val
        
    def getFG(self):
        return self.filsG
        
    def getFD(self):
        return self.filsD

"""Un Tas possede le nombre de clefs stockees, et un pointeur sur la racine de l'arbre"""
class Tas:
    def __init__(self, nbv, r):
        self.nbv = nbv          #nombre de valeurs dans le tas
        self.racine = r         #racine de l'arbre
        
    def getR(self):
        return self.racine
    
    def setR(self, r):
        self.racine=r
    
    def getNbv(self):
        return self.nbv
        
    def setNbv(self, newNb):
        self.nbv = newNb        
        
    
def Creer_Noeud(v, g, d):#O(1)
    return Noeud(v, g, d)
    """cle*Noeud*Noeud-> Noeud
    crée un noeud de valeur v, de fils gauche g, de fils droit d"""

def Creer_Tas():#O(1)
    return Tas(0, None)
    """void-> Tas
    renvoie un Tas sans clefs"""

def Ajout_Arbre_aux(N, valeur, nbf, nbfmax): #O(log(n))
    if(inf(valeur, N.getV())):  #si la cle est inferieure, ont permute
            tmp = N.getV()
            N.setV(valeur)
            valeur = tmp
            
    if(N.getFG() == None):
        N.setFG(Creer_Noeud(valeur,None,None))
        return
    
    elif(N.getFG() != None and N.getFD() == None):
            N.setFD(Creer_Noeud(valeur,None,None))
            return
        
    else:
        if(nbf < nbfmax/2):         #on descend dans le sous arbre gauche
            Ajout_Arbre_aux(N.getFG(), valeur, nbf, nbfmax/2)
                         
        else:                       #on descend dans le sous arbre droit
            Ajout_Arbre_aux(N.getFD(), valeur, nbf-(nbfmax/2), nbfmax/2)
            
    """Noeud*cle*int*int-> Noeud
    fonction auxiliaire permettant de descendre jusqu'a la premiere feuille libre"""

#def Existe(N, val):#O(n)
#    if(N == None):
#        return False
#    elif(eg(N.getV(),val)):
#        return True
#    else:
#        return (Existe(N.getFG(),val) or Existe(N.getFD(),val))
#        
    
def Ajout_Arbre(T, val): #O(log(n))

    if(T.getNbv() == 0):
        return Tas(1, Creer_Noeud(val, None, None)) #initialisation de l'arbre
    
    nbv = T.getNbv()    
    if(log(nbv+1, 2) % 1 == 0.0):
        h = int(log(nbv, 2)) + 1              #cas ou toutes les feuilles sont pleines
    else:
        h = int(log(nbv, 2))                  #hauteur de l'arbre initial - 1
    
    nbfmax = 2**(h)                           #nombre de feuilles maximales  
    nbf = T.getNbv() - (2**(h)) + 1           #nombre de feuilles occupees actuelles
    
    Ajout_Arbre_aux(T.getR(), val, nbf, nbfmax) #nouvel arbre apres ajout
    T.setNbv(T.getNbv()+1)
    return T
    """Tas*cle->Tas
    ajoute une cle dans le Tas """
  

def Suppr_Arbre_aux(N, nbf, nbfmax): #O(log(n))
    if(N.getFG() == None):
        return None
        
    if(N.getFD() == None):  #N a donc un fils gauche mais pas de fils droit
                            #on supprime donc le fils gauche
        return Noeud(N.getV(), None, None)
    
    
    if(nbf <= nbfmax/2):    #suppression dans le sous arbre gauche
        return Noeud(N.getV(),
                     Suppr_Arbre_aux(N.getFG(),
                                     nbf,
                                     nbfmax/2),
                     N.getFD())
                     
    else:                   #suppression dans le sous arbre gauche
        return Noeud(N.getV(),
                     N.getFG(),
                     Suppr_Arbre_aux(N.getFD(),
                                     nbf - (nbfmax/2),
                                     nbfmax/2))   
    """Noeud*int*int->Noeud
    supprime  la derniere feuille pleine de l'arbre et renvoie la racine"""

def Chercher_Arbre_aux(N, nbf, nbfmax): #O(log(n))
    if(N.getFG() == None):
        return N.getV()     #le noeud n'a pas de fils, c'est donc uen feuille

    else:
        if(nbf <= nbfmax/2):   #recherche dans le sous arbre gauche
            return Chercher_Arbre_aux(N.getFG(), nbf, nbfmax/2)
            
        else:                   #recherche dans le sous arbre droit
            return Chercher_Arbre_aux(N.getFD(), nbf-(nbfmax/2), nbfmax/2)
    """Noeud*int*int->cle
    renvoie la cle de la derniere feuille pleine"""
            
def Entasser_Arbre(N): #O(log(n))
    if(N == None):
        return None             #N est uen feuile vide
        
    elif(N.getFG() == None):    #sinon N est une feuille pleine
        return N 
    
    elif(N.getFD() == None):    #N n'a qu'un fils a gauche
        if(inf(N.getFG().getV(), N.getV())):    #si la cle du fils gauche est >
            tmp = N.getFG().getV()              #a celle du pere, on permute
            N.getFG().setV(N.getV())
            N.setV(tmp)
        return Noeud(N.getV(), N.getFG(), None)
            
    
    
    #le fils gauche est inferieur au pere ET au fils droit
    elif(inf(N.getFG().getV(), N.getV()) and inf(N.getFG().getV(), N.getFD().getV())):
        tmp = N.getFG().getV()
        N.getFG().setV(N.getV())
        N.setV(tmp)
        return Noeud(N.getV(),
                     Entasser_Arbre(N.getFG()),
                     N.getFD())
   
    #le fils droit est inferieur au pere ET au fils gauche
     
    elif(inf(N.getFD().getV(), N.getV()) and inf(N.getFD().getV(), N.getFG().getV())):
        tmp = N.getFD().getV()
        N.getFD().setV(N.getV())
        N.setV(tmp)
        return Noeud(N.getV(),
                     N.getFG(),
                     Entasser_Arbre(N.getFD()))
        
    else: #le pere est superieur aux fils gauche et droit
        return Noeud(N.getV(), N.getFG(), N.getFD())
    
    """Noeud->Noeud 
    recoit la racine de l'arbre et renvoie l'arbre avec les valeurs rangees
    dans l'ordre croissant de la racine aux feuilles"""
        
    
def Suppr_Arbre(T): #O( 3 * log(n)) = O(log(n))
    if(T.getR() ==None or (T.getR().getFG() == None and T.getR().getFD() == None)):
        return None #l'arbre est vide ou l'arbre n'est qu'une feuille
        
    nbv = T.getNbv()    
    if(log(nbv+1, 2) % 1 == 0.0):
        h=int(log(nbv, 2))              #cas ou toutes les feuilles sont pleines
    else:
        h=int(log(nbv, 2))              #hauteur de l'arbre initial - 1
    
    nbfmax = 2**(h)                     #nombre de feuilles maximales  
    nbf = T.getNbv() - (2**(h)) + 1     #nombre de feuilles occupees actuelles
    val = Chercher_Arbre_aux(T.getR(), nbf, nbfmax) #recuperation de la derniere feuille
    N   = Suppr_Arbre_aux(T.getR(), nbf, nbfmax)    #suppression de la derniere feuille
     
    T.setNbv(T.getNbv() - 1)            #nombre de val - 1                                                   
    N.setV(val)                         #on rentre la valeur a la racine 
    N   = Entasser_Arbre(N)             #on tasse l'arbre                
    T.setR(N)                           #ont met a jour la structure
    return T
    """Tas->Tas
    recoit un tas, recupere et supprime la derniere feuille remplie, la remplace
    a la racine et entasse l'arbre, puis met a jour le Tas"""
    
def Afficher_Arbre(N): #O(n)
    if(N == None):
        return ''
#        
#    if(N.getFG() == None and N.getFD() == None):
#        return str(N.getV())
    else:    
        return (N.getV() , Afficher_Arbre(N.getFG()) ,Afficher_Arbre(N.getFD()))
    """Noeud->liste
    recoit la racine de l'arbre et l'affiche sous forme de liste"""
    
def Lister_Arbre(N): #O(n)
    if(N == None):
        return []
        
    if(N.getFG() == None and N.getFD() == None):
        return [N.getV()]
        
    return [N.getV()] + Lister_Arbre(N.getFG()) + Lister_Arbre(N.getFD())
    """Noeud->tableau
    recoit la racine de l'arbre et l'affiche sous forme de tableau"""
    
def ConsIter_Arbre(liste): #O(nlog(n))
    T = Creer_Tas()    
    for i in liste: 
        T = Ajout_Arbre(T, i)                    
    return T     
    """liste -> Tas
    recoit une liste de valeur et renvoie le Tas cree avec celles ci""" 

def Union_Arbre(T1,T2): #O(nlog(n)) + O(mlog(n+m)) = O(n+m(log(n+m))) 
    if(T1 == None):
        return T2
    
    if(T2 == None):
        return T1
    
    if(inf(T1.getR().getV(), T2.getR().getV())):
        l = Lister_Arbre(T2.getR())
        for e in l:
            T1 = Ajout_Arbre(T1, e)
        return T1
    else :
        l = Lister_Arbre(T1.getR())
        for e in l:
            T2 = Ajout_Arbre(T2, e)  
        return T2

    """Tas*Tas-> Tas 
    renvoie l'union de deux tas"""                                

############################
###implementation tableau###
############################
    
    
def Echanger(x, y): #O(1)
    tmp = x                      
    x = y                         
    y = tmp                      
    return (x, y)           
    """permute x et y"""
    
def SupprMin_Tableau(T): #O(log(n))
    if(T == []):                                      
        return T                                    
        
    T[0] = T[len(T) - 1]    #remplacement de la cle min par la derniere cle ajoutee                             
    T.pop(len(T) - 1)       #suppression de la derniere feuille pleine
    maxi = ((len(T) - 1) - 1)//2    #indice maximum possible
    i = 0                                             
    while(i <= maxi):
        if(2*i + 2 >= len(T)):
            newI = 2*i + 1    #derniere valeur du tableau                        
        else:
            if(inf(T[2*i+1],T[2*i+2])): 
                newI = 2*i+1    #recuperation de l'indice du fils gauche
            else:
                newI = 2*i+2    #recuperation de l'indice du fils droit
        if(inf(T[newI],T[i])):                          
            T[i], T[newI] = Echanger(T[i], T[newI])     
            i = newI                                 
        else:
            break   #le tableau est trie, plus besoin d'iterer                             
    return T            
    """Tableau->Tableau
    supprime la valeur minimale du tableau et le renvoie apres entassement"""                        

def ConsIter_Tableau(liste):#O(n)
    T= []
    
    for e in liste:
        T.append(e)
    
    nbfeuilles = 2 ** int(log(len(T),2)) 
    nbfeuillesoccupees = len(T) - nbfeuilles + 1
    i = len(T) - 1 - nbfeuillesoccupees
    maxi = len(T) - 1
    
    while(i != -1):
        if(2*i + 1 > maxi):     #passer le dernier etage
            i -= 1
            continue
        
        elif(2*i+2 > maxi):     #le noeud n'a qu'un fils (a gauche)
            if(inf(T[i*2 + 1],T[i])):
                T[i], T[i*2 + 1] = Echanger(T[i], T[i*2 + 1])
                
        else:                   #le noeud a deux fils
            pere = i 
            while(pere <= maxi):
                if(pere*2 + 1> maxi): #on est sur une feuille
                    break
                elif(pere*2 + 2 >maxi): #on est sur un noeud qui n'a qu'un fils gauche
                    if(inf(T[pere*2 + 1],T[pere])):
                        T[pere], T[pere*2 + 1] = Echanger(T[pere], T[pere*2 + 1])
                    break
                elif(inf(T[pere*2 +1],T[pere])): #le fils gauche est inferieur au pere
                    if(inf(T[pere*2 +1],T[pere*2 + 2])): #le fils gauche < fils droit
                        T[pere] , T[pere*2 + 1] = Echanger(T[pere] , T[pere*2 + 1])
                        pere = i*2 + 1
                        
                    else: #fils gauche > fils droit
                        T[pere] , T[pere*2 + 2] = Echanger(T[pere] , T[pere*2 + 2])
                        pere = pere*2 + 2
                        
                elif(inf(T[pere*2 + 2],T[pere])): #fils droit < pere
                    T[pere], T[pere*2 + 2] = Echanger(T[pere],T[pere*2 + 2 ])
                    pere = pere*2 +2
                else:
                    break
        i -= 1
    return T

def Ajout_Tableau(T,e):
    if(T == []):
        return [e]
    
    T.append(e)
    i = (len(T) - 1)
    while(inf(T[i],T[(i-1)//2])): #pere superieur au fils
        T[i],T[(i-1)//2] = Echanger(T[i],T[(i-1)//2])
        i = (i-1)//2            #i devient l'indice du pere
        if((i-1//2) == 0):      #le nouveau pere est la racine
            break
    
    return T
        
    
    
    
def Union_Tableau(T1, T2): #O(n + m)
    
    if T1 == []:
        return T2
    if T2 == []:
        return T1
    
    if(inf(T1[0],T2[0])):
        return ConsIter_Tableau(T1 + T2)
    else:
        return ConsIter_Tableau(T2 + T1)
        
    """Tableau*Tableau->Tableau
    construit l'union de deux tableaux sous forme de Tas, en ajoutant le plus
    petit au plus grand pour moins de temps de calcul"""


    
def MainT():
    print("construction a partir d'une liste")
    t=[i for i in range(20)]
    tas1=[2,6,10,8,12,14]
    tas2=[5,13,7,15]
    random.shuffle(t)
    print(t)
    print(ConsIter_Tableau(t))
#    testUnion=(Union_tableau(tas1,tas2))
#    print(testUnion)
#    for i in range(10):
#        testUnion = SupprMinTas_tableau(testUnion)
#        print(testUnion)

################################# jeu de test #################################

def Test_Arbre():
    print("\t----- test des Fonctions sur une structure Tas arborescente -----\n")
    print("\t\t---------- test de ConsIter ----------\n")
    liste1 = [i for i in range(20)]
    random.shuffle(liste1)
    print("\nliste1 = ", liste1)
    A1 = ConsIter_Arbre(liste1)
    print("\naprès construction:\n", Afficher_Arbre(A1.getR()))
    print("\n\t\t---------- test de Suppression ----------\n")
    print("avant suppression:\n ",Afficher_Arbre(A1.getR()))
    A1 = Suppr_Arbre(A1)
    print("\napres suppression:\n ",Afficher_Arbre(A1.getR()))
    print("\n\t\t---------- test de Ajout ----------\n")
    print("avant ajout:\n ",Afficher_Arbre(A1.getR()))
    A1 = Ajout_Arbre(A1, 0)
    print("\napres ajout de 0:\n ",Afficher_Arbre(A1.getR()))
    print("\n\t\t---------- test d'Union ----------\n")
    liste2 = [i for i in range(0,20)]
    random.shuffle(liste2)
    l1 = liste2[:10]
    l2 = liste2[10:]
    print("\nliste1 = ",l1,"\nliste2 = ",l2)
    A1 = ConsIter_Arbre(l1)
    A2 = ConsIter_Arbre(l2)
    
    print("avant union:\nA1: ",Afficher_Arbre(A1.getR()),"\nA2:",Afficher_Arbre(A2.getR()))
    A = Union_Arbre(A1,A2)
    print("\napres union:\n ",Afficher_Arbre(A.getR()))
    
def Test_Tableau():
    print("\t----- test des Fonctions sur une structure Tas Tableau -----\n")
    print("\t\t---------- test de ConsIter ----------\n")
    liste1 = [i for i in range(20)]
    random.shuffle(liste1)
    print("\nliste1 = ", liste1)
    T1 = ConsIter_Tableau(liste1)
    print("\naprès construction:\n", T1)
    print("\n\t\t---------- test de Suppression ----------\n")
    print("avant suppression:\n ",T1)
    T1 = SupprMin_Tableau(T1)
    print("\napres suppression:\n ",T1)
    print("\n\t\t---------- test de Ajout ----------\n")
    print("avant ajout:\n ",T1)
    T1 = Ajout_Tableau(T1, 0)
    print("\napres ajout de 0:\n ",T1)
    print("\n\t\t---------- test d'Union ----------\n")
    liste2 = [i for i in range(0,20)]
    random.shuffle(liste2)
    l1 = liste2[:10]
    l2 = liste2[10:]
    print("\nliste1 = ",l1,"\nliste2 = ",l2)
    T1 = ConsIter_Tableau(l1)
    T2 = ConsIter_Tableau(l2)
    
    print("avant union:\nT1:",T1,"\nT2:",T2)
    T = Union_Tableau(T1,T2)
    print("\napres union:\n ",T)

#Test_Arbre()
#print("#######################################################################")
#Test_Tableau()
