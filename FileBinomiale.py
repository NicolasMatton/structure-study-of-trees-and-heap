# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 17:06:24 2018

@author: utilisateur
"""
import random

def inf(cle1, cle2):
    return cle1 < cle2
            
def eg(cle1, cle2):
    return cle1 == cle2
    
    
class File_Binomiale:
    def __init__(self, nbv):
        self.nbv = nbv
        self.FB = []
        
    def getFB(self):
        return self.FB
        
    def getNbv(self):
        return sum(tb.getNbv() for tb in self.FB)
    
    def setNbv(self, n):
        self.nbv = n
        
    def setFB(self, f):
        self.FB = f
        
class Tournoi_Binomial:
    def __init__(self, Nbv, listeF, racine, degre):
        self.listeF = listeF
        self.Nbv = Nbv
        self.racine = racine
        self.degre = degre
        
    def getListeF(self):
        return self.listeF
        
    def getNbv(self):
        return self.Nbv
    
    def setNbv(self, n):
        self.Nbv = n
    
    def getR(self):
        return self.racine
    
    def getDeg(self):
        return self.degre
    
    def setDeg(self, degre):
        self.degre = degre
        
    def setR(self, r):
        self.racine = r
        
    def setListeF(self, listeF):
        self.listeF = listeF
        
def creer_TournoiVide():
    return Tournoi_Binomial(0, [], None, 0)

def creer_Tournoi(v):
    return Tournoi_Binomial(1, [], v, 0)
    
def creer_FileB():
    return File_Binomiale(0)

def EstVideT(T):
    return T.getR()==None
    """TournoiB−>booleen Renvoie vrai ssi le tournoi est vide."""

    
def Degre(T):
    return T.getDeg()
    """TournoiB−>entier Renvoie le degre de la racine du tournoi."""

def Union2Tid(TB1,TB2):
    if(inf(TB2.getR(), TB1.getR())):
        return Tournoi_Binomial(TB1.getNbv() + TB2.getNbv(), 
                                [TB1] + TB2.getListeF(),
                                TB2.getR(),
                                Degre(TB1) + 1)
                                
    else:
        return Tournoi_Binomial(TB1.getNbv() + TB2.getNbv(), 
                                [TB2] + TB1.getListeF(),
                                TB1.getR(),
                                Degre(TB1) + 1)
    """TournoiB ∗ TournoiB−>TournoiB
    Renvoie l’union de 2 tournois de meme taille."""
    
def Decapite(T):
    l = T.getListeF()         #recuperation de la liste des feuilles
    f = creer_FileB()         #creation d'une file
    f.setNbv(T.getNbv() - 1)  #ajout du nbr d'elem dans la file - la racine
    f.setFB(l)              # ajout des feuilles dans la liste de tournois 
    return f
    """TournoiB−>FileB 
    Renvoie la file binomiale obtenue en supprimant la racine du tournoi
    T_k −> <T_{k−1},T_{k−2},...,T_1,T_0>."""

def File(T):
    f = creer_FileB()
    f.setFB([T])
    return f
    """TournoiB−>FileB Renvoie la file binomiale
    reduite au tournoi T_k−><T_k>."""
    
def EstVide(F):
    return (F.getFB() == [])
    """FileB−>booleen Renvoie vrais si la file est vide."""
    
def MinDeg(F):
    if(not EstVide(F)):
        return F.getFB()[-1]
    return False
    """FileB−>TournoiB Renvoie le tournoi de degre minimal dans la file.
    Precision: ce tournoi se situe par definition des FB a la fin
    de la file"""
    

    
def Reste(F):
    if(not EstVide(F)):
        F.setFB(F.getFB()[0:-1]) #-1 permettant d'acceder au dernier element
        return F
        
    return F
    """FileB−>FileB Renvoie la file privee de son tournoi de degre minimal.
    Precision: le tournoi de DegMin se situe par definition des FB a la fin
    de la file """

    
def AjoutMin(T, F):
    F.setFB(F.getFB() + [T])
    return F
    """Tournoi ∗ FileB−>FileB 
       Hypothese:le tournoi est de degre inferieur au MinDeg de la file
       Renvoie la file obtenue en ajoutant le tournoi comme 
       tournoi de degre minimal de la file initiale."""

def UFret(F1, F2, T):
    if (EstVideT(T)):  #pas de tournoi en retenue
        if (EstVide(F1)):
            return F2
        if (EstVide(F2)):
            return F1
        
        T1 = MinDeg(F1)
        T2 = MinDeg(F2)
        if(Degre(T1) < Degre(T2)):
            return AjoutMin(T1, UnionFile(Reste(F1), F2))
        if(Degre(T2) < Degre(T1)): 
            return AjoutMin(T2, UnionFile(Reste(F2), F1))
        if(Degre(T1) == Degre(T2)): 
            return UFret(Reste(F1), Reste(F2), Union2Tid(T1, T2))
            
    else: #T tournoi en retenu
        if (EstVide(F1)):
            return UnionFile(File(T), F2)
        if (EstVide(F2)):
            return UnionFile(File(T),F1)
        T1 = MinDeg(F1)
        T2 = MinDeg(F2)
        if (Degre(T) < Degre(T1) and Degre(T) < Degre(T2)): 
            return AjoutMin(T, UnionFile(F1, F2)) 
        if (Degre(T) == Degre(T1) and Degre(T) == Degre(T2)):
            return AjoutMin(T, UFret(Reste(F1), Reste(F2), Union2Tid(T1, T2)))
        if (Degre(T) == Degre(T1) and Degre(T) < Degre(T2)):
            return UFret(Reste(F1), F2, Union2Tid(T1, T))
        if (Degre(T) == Degre(T2) and Degre(T) < Degre(T1)):
            return UFret(Reste(F2), F1, Union2Tid(T2, T))

            
            
    """FileB∗FileB∗TournoiB−>FileB 
    Renvoie la file binomiale union de deux files et d’un tournoi."""

            
def UnionFile(F1, F2):
    return UFret(F1, F2, creer_TournoiVide())
    """FileB∗FileB−>FileB
        Renvoie la file binomiale union des deux files F1 et F2."""
 
def Ajout_FB(v, FB): 
    T=FB.getFB()
    return UnionFile(FB, File(creer_Tournoi(v)))

def SupprMin(FB):
    T = FB.getFB()[0]
    IdSuppression = 0
    l=FB.getFB()
    for i in range(1, len(l)):
        if(inf(l[i].getR(), T.getR())):
            T = l[i]
            IdSuppression = i
    l.pop(IdSuppression)    #on enleve le tournoi contenant le min
    FB.setFB(l)             #et ont l'enregistre
    f = Decapite(T)
    return UnionFile(f, FB)
    """fusion de la file privee de son tournoi comportant la clef minimale
    avec la file obtenue apres decapitation de ce tournoi"""
    
def ConsIter_FB(listeE):
    FB=creer_FileB()
    for e in listeE:
        FB=UnionFile(FB, File(creer_Tournoi(e)))
        #print(Afficher_File(FB))
    return FB
    
def Afficher_File(FB):
    l=FB.getFB()
    for TB in l:
            print ("TB ", Degre(TB), "--->", Afficher_Tournoi(TB))
            print("")
    return ""
        
def Afficher_Tournoi(TB):
    if(TB.getListeF()==[]):
        return [TB.getR()]
    else:
        return [TB.getR()]+[Afficher_Tournoi(t) for t in TB.getListeF()]
        

def Main():
    print("construction a partir d'une liste melange de 20 elements")
    t1=[i for i in range(100)]
    t2=[i for i in range(100,200)]
    random.shuffle(t1)
    random.shuffle(t2)
    f1=ConsIter_FB(t1)
    f2=ConsIter_FB(t2)
#    print (f.getNbv(),'elements')
    print("-----------------------------------------------")
    print("Suppression de la cle min")
    print(Afficher_File(f1))
    print(Afficher_File(f2))
    f = (UnionFile(f1,f2))
    print(Afficher_File(f))
    print(Afficher_File(f1))
    print(Afficher_File(f2))
    return Afficher_File(f), "\n", f.getNbv(),"\n"

def Test_FileBinomiale():
    print("\t----- test des Fonctions sur une File binomiale -----\n")
    print("\t\t---------- test de ConsIter ----------\n")
    liste1 = [i for i in range(40)]
    random.shuffle(liste1)
    print("\nliste1 = ", liste1)
    F1 = ConsIter_FB(liste1)
    
    print("\naprès construction:\n")
    print(Afficher_File(F1))
    print("\n\t\t---------- test de Suppression ----------\n")
    print("avant suppression:\n ")
    print(Afficher_File(F1))
    F1 = SupprMin(F1)
    print("\napres suppression:\n ")
    print(Afficher_File(F1))
    print("\n\t\t---------- test de Ajout ----------\n")
    print("avant ajout:\n ")
    print(Afficher_File(F1))
    F1 = Ajout_FB(0, F1)
    print("\napres ajout de 0:\n ")
    print(Afficher_File(F1))
    print("\n\t\t---------- test d'Union ----------\n")
    liste2 = [i for i in range(0,40)]
    random.shuffle(liste2)
    l1 = liste2[:20]
    l2 = liste2[20:]
    print("\nliste1 = ",l1,"\nliste2 = ",l2)
    F1 = ConsIter_FB(l1)
    F2 = ConsIter_FB(l2)
    
    print("avant union:\nF1:")
    print(Afficher_File(F1))
    print("\nF2:")
    print(Afficher_File(F2))
    F = UnionFile(F1,F2)
    print("\napres union:\n ")
    print(Afficher_File(F))
#    
#Test_FileBinomiale()
#    
