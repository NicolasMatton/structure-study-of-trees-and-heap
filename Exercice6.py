# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 03:01:50 2018

@author: utilisateur
"""

from MyMD5 import *
from os import listdir
from TasBinomial import *
from FileBinomiale import *
from AVL import *
from ABR import *
import numpy as np
import matplotlib.pyplot as plt
import time

def Extraire():
    fichiers = [f for f in listdir("Shakespeare")]
    print(fichiers)
    listemots=[]
    
    for file in fichiers:
        f = open("Shakespeare/"+file)
        for mot in f:
            listemots.append(mot)
        f.close()
    
    ABR = ArbreVide()
    
    f = open("HacheShakespeareAll.txt","a")
    
#    for motl in listemots:
#        mot = motl[:-1]
#        hache = int("0x"+ md5(mot),0)
#        if(Recherche(hache,ABR)): #hachage deja existant
#            continue
#        else:   #mot n'étant pas en collision ou présent dans l'arbre
#            f.write("0x"+ md5(mot)+ "\n")
#            ABR = ABR_Ajout(hache,ABR)
    
    for mot in listemots:
        f.write("0x"+md5(mot)+"\n")
    f.close()
    return 

def ShakeSpeare():
    fichiers = [f for f in listdir("Shakespeare")]
    print(fichiers)
    listemots=[]
    
    for file in fichiers:
        f = open("Shakespeare/"+file)
        for mot in f:
            listemots.append(mot)
        f.close()
    
#    
#    file=fichiers[0]     
#    f = open("Shakespeare/"+file)
#    for mot in f:
#        listemots.append(mot)
#    f.close()
    
    print("\nfin de lecture des fichiers")

    dictionnaire_collisions = dict()
    
    liste_mots_differents = []
    
    nb_collisions = 0
    
    ABR = ArbreVide()
    
    f = open("HacheShakespeare.txt","a")
    for motl in listemots:
        mot = motl[:-1]
        hache = int("0x"+ md5(mot),0)
        if(Recherche(hache,ABR)): #hachage deja existant
            if(mot not in liste_mots_differents): #COLLISION
                liste_mots_differents.append(mot) #ajout a la liste de mots différents
                dictionnaire_collisions[hache].append(mot) # ajout dans le dico de collisions
                nb_collisions += 1
             
            
            else: #mot deja vu
                continue
        else:   #mot n'étant pas en collision ou présent dans l'arbre
            dictionnaire_collisions[hache] = [mot]
            liste_mots_differents.append(mot)
            ABR = ABR_Ajout(hache,ABR)
    f.close()
    
    print("dictionnaire_collision = ",dictionnaire_collisions)
    print("\nliste_mots_differents = ",liste_mots_differents)
    
    return nb_collisions, len(listemots), len(liste_mots_differents), len(dictionnaire_collisions)

def Comparer_Tas_File_ConsIter():
    cles=[]
    f = open("HacheShakespeare.txt")
    for l in f:
        cles.append(int(l[:-1],0)) #int(l[:-1],0) permet de recuperer la valeur 128 bit sous forme de 
                                          #chaine de caracteres et la converti en int (le second parametre
                                          #permettant de preciser que la valeur est en 128bit)
                                          #:-1 pour ne pas avoir le /n
    f.close()
    
    tailles = [i for i in range(1000,len(cles),1000)]
    tempsTas= []
    tempsFB = []
    
    for i in range(len(tailles)):
        cle = cles[:tailles[i]]
        print("------calcul du temps d'exécution pour la construction pour ",tailles[i]," valeurs------")
        start = time.time()
        Tas = ConsIter_Tableau(cle)
        end = (time.time() - start) * 1000.0
        tempsTas.append(end)
        print("temps de construction pour un Tas en millisecondes: ",end)
        start = time.time()
        FB  = ConsIter_FB(cle)
        end = (time.time() - start) * 1000.0 
        tempsFB.append(end)                                    
        print("temps de construction pour une File en millisecondes: ",end)
    
    xA = np.array(tailles)
    yA = np.array(tempsTas)
    
    xT = np.array(tailles)
    yT = np.array(tempsFB)
    
    plt.title("Complexite ConsIter Tas VS File")
    
    plt.plot(xA, yA, "o-", label="Tableau")
    plt.plot(xT, yT, "o--", label="File")
    plt.legend()
    plt.xlabel("taille")
    plt.ylabel("temps(millisecondes")
#    plt.savefig("Complexite_ConsIter_Tas_VS_File.png",dpi=1000)
    plt.show()
    return 

def Comparer_Tas_File_SupprMin():
    cles=[]
    f = open("HacheShakespeare.txt")
    for l in f:
        cles.append(int(l[:-1],0)) #int(l[:-1],0) permet de recuperer la valeur 128 bit sous forme de 
                                          #chaine de caracteres et la converti en int (le second parametre
                                          #permettant de preciser que la valeur est en 128bit)
                                          #:-1 pour ne pas avoir le /n
    f.close()
    
    tailles = [i for i in range(1000,len(cles),1000)]
    tempsTas= []
    tempsFB = []
    
    for i in range(len(tailles)):
        cle = cles[:tailles[i]]
#        print("------calcul du temps d'exécution pour la suppression pour ",tailles[i]," valeurs------")
        Tas = ConsIter_Tableau(cle)
        start = time.time()
        Tas = SupprMin_Tableau(Tas)
        end = (time.time() - start) * 1000.0
        tempsTas.append(end)
#        print("temps de suppression pour un Tas en millisecondes: ",end)
        FB = ConsIter_FB(cle)
        start = time.time()
        FB  = SupprMin(FB)
        end = (time.time() - start) * 1000.0                                     
        tempsFB.append(end)
#        print("temps de suppression pour une File en millisecondes: ",end)
    
    xA = np.array(tailles)
    yA = np.array(tempsTas)
    
    xT = np.array(tailles)
    yT = np.array(tempsFB)
    
    plt.title("Complexite SupprMin de 0 a 23000valeurs Tas VS File")
    
    plt.plot(xA, yA, "o-", label="Tableau")
    plt.plot(xT, yT, "o--", label="File")
    plt.legend()
    plt.xlabel("taille")
    plt.ylabel("temps(millisecondes")
#    plt.savefig("Complexite_SupprMin_Tas_VS_File.png",dpi=1000)
    plt.show()
    return 

def Comparer_Tas_File_Ajout():
    cles=[]
    f = open("HacheShakespeare.txt")
    for l in f:
        cles.append(int(l[:-1],0)) #int(l[:-1],0) permet de recuperer la valeur 128 bit sous forme de 
                                          #chaine de caracteres et la converti en int (le second parametre
                                          #permettant de preciser que la valeur est en 128bit)
                                          #:-1 pour ne pas avoir le /n
    f.close()
    
    tailles = [i for i in range(1000,len(cles),1000)]
    tempsTas= []
    tempsFB = []
    
    for i in range(len(tailles)):
        cle = cles[:tailles[i]]
        print("------calcul du temps d'exécution pour l'ajout de 0 pour ",tailles[i]," valeurs------")
        Tas = ConsIter_Tableau(cle)
        start = time.time()
        Tas = Ajout_Tableau(Tas, 0)
        end = (time.time() - start) * 1000.0
        tempsTas.append(end)
        print("temps de l'ajout de 0 pour un Tas en millisecondes: ",end)
        FB = ConsIter_FB(cle)
        start = time.time()
        FB  = Ajout_FB(0,FB)
        end = (time.time() - start) * 1000.0                                     
        tempsFB.append(end)
        print("temps de l'ajout de 0 pour une File en millisecondes: ",end)
        
        
    xA = np.array(tailles)
    yA = np.array(tempsTas)
    
    xT = np.array(tailles)
    yT = np.array(tempsFB)
    
    plt.title("Complexite Ajout Tas VS File")
    
    plt.plot(xA, yA, "o-", label="Tableau")
    plt.plot(xT, yT, "o--", label="File")
    plt.legend()
    plt.xlabel("taille")
    plt.ylabel("temps(millisecondes")
#    plt.savefig("Complexite_Ajout_Tas_VS_File.png",dpi=1000)
    plt.show()
    return 

def Comparer_Tas_File_Union():
    cles=[]
    f = open("HacheShakespeareAll.txt")
    for l in f:
        cles.append(int(l[:-1],0)) #int(l[:-1],0) permet de recuperer la valeur 128 bit sous forme de 
                                          #chaine de caracteres et la converti en int (le second parametre
                                          #permettant de preciser que la valeur est en 128bit)
                                          #:-1 pour ne pas avoir le /n
    f.close()
    
    tailles = [i for i in range(40000,len(cles),40000)]
    tempsTas= []
    tempsFB = []
    
    for i in range(len(tailles)):
        cle = cles[:tailles[i]]
#        print("------calcul du temps d'exécution pour l'union avec ",tailles[i],"valeurs------")
#        print("les deux listes sont les deux moitié de toutes les clés")
        Tas1 = ConsIter_Tableau(cle[:(len(cle)//2)-1])
        Tas2 = ConsIter_Tableau(cle[(len(cle)//2)-1:])
        FB1  = ConsIter_FB(cle[:(len(cle)//2)-1])
        FB2  = ConsIter_FB(cle[(len(cle)//2)-1:])
        start = time.time()
        Tas = Union_Tableau(Tas1, Tas2)
        end = (time.time() - start) * 1000.0
        tempsTas.append(end)
#        print("\ntemps de Union pour deux tas en millisecondes: ",end)
        start = time.time()
        FB  = UnionFile(FB1, FB2)
        end = (time.time() - start) * 1000.0
        tempsFB.append(end)                   
#        print("\ntemps de Union pour deux Files en millisecondes: ",end)
    
    xA = np.array(tailles)
    yA = np.array(tempsTas)
    
    xT = np.array(tailles)
    yT = np.array(tempsFB)
    
    plt.title("Complexite Union Tas VS File All")
    
    plt.plot(xA, yA, "o-", label="Tableau")
    plt.plot(xT, yT, "o--", label="File")
    plt.legend()
    plt.xlabel("taille")
    plt.ylabel("temps(millisecondes")
#    plt.savefig("Complexite_Union_Tas_VS_File_All.png",dpi=1000)
    plt.show()
    return 

#Comparer_Tas_File_Ajout()
#Comparer_Tas_File_ConsIter()
#Comparer_Tas_File_SupprMin()
#Comparer_Tas_File_Union()