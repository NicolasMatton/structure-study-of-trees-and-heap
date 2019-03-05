# -*- coding: utf-8 -*-

from FileBinomiale import *
import time
import numpy as np
import matplotlib.pyplot as plt
import copy


plt.show() # affiche la figure a l'ecra
"""Question 3.10"""

def Calcul_ConsIter_File():
    tailles=[100, 200, 500, 1000, 5000, 10000, 20000, 50000]
    temps=[]
    for t in tailles:
        jeux=[]
        for i in range(1,6):
            f=open("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(t)+".txt")
            cles=[]
            for l in f:
               cles.append(int(l[:-1],0)) 
            jeux.append(cles)
            f.close()
        time_tmp=[]
        ##print(jeux)
        
        print("\n------\ncalcul de temps de construction pour",t,"valeurs")
        for j in jeux:
            t1_start=time.time()
            FB=ConsIter_FB(j)
            t2_end=time.time()
            t_exec = (t2_end - t1_start)*1000.0
            time_tmp.append(t_exec)
            print("pour le jeu ",jeux.index(j),":",t_exec, "millisecondes")
            moyenne=sum(time_tmp)/len(time_tmp)
        temps.append(moyenne)
        print("temps moyen",moyenne)
    
    return tailles,temps

taillesF, tempsF = Calcul_ConsIter_File()



def graphique():
    xF = np.array(taillesF)
    yF = np.array(tempsF)
    
    plt.title("Complexite ConsIter File Binomiale")
    
    plt.plot(xF, yF, "o-", label="File")
    plt.legend()
    plt.xlabel("taille")
    plt.ylabel("temps(millisecondes")
    plt.savefig("Complexite_ConsIter_FileBinomiale.png",dpi=1000)
    plt.show()
    
    #-----------ZOOM----------#
    
    xFz = np.array(taillesF[:4])
    yFz = np.array(tempsF[:4])
    
    plt.close()
    plt.title("Complexite ConsIter File Binomiale Zoom")
    
    plt.plot(xFz, yFz, "o-", label="File")
    plt.legend()
    plt.xlabel("taille")
    plt.ylabel("temps(millisecondes")
#    plt.savefig("Complexite_ConsIter_FileBinomiale_Zoom.png",dpi=1000)
    plt.show()

graphique()
    
    
def Calcul_Union_File():
    tailles=[100, 200, 500, 1000, 5000, 10000, 20000, 50000]
    temps=[]
    for i in range(1,2):
        print("pour le jeu ",i,"\n")
        listes=[]
        for  t in tailles:
            f=open("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(t)+".txt")
            cles = []
            for l in f:
               cles.append(int(l[:-1],0)) #int(l[:-1],0) permet de recuperer la valeur 128 bit sous forme de 
                                          #chaine de caracteres et la converti en int (le second parametre
                                          #permettant de preciser que la valeur est en 128bit)
                                          #:-1 pour ne pas avoir le /n
            listes.append(ConsIter_FB(cles))
            f.close()
        time_tmp=[]
        
        print("\n------\ncalcul de temps de union pour",t,"valeurs")
        for j in range(len(listes)):
            tmp = copy.deepcopy(listes[len(listes)-1])          
            tmp2 =copy.deepcopy(listes[j])
            t1_start=time.time()
            a=UnionFile(tmp2, tmp)
            t2_end=time.time()
            t_exec = (t2_end - t1_start)*1000.0
            time_tmp.append(t_exec)
            print(Afficher_File(a),"\n---")
            print("pour les tailles ",tailles[j],"et",tailles[len(listes)-1],":",t_exec, "millisecondes")
        temps.append(time_tmp)
        
    moyenne = []
        
    for i in range(8):
        s = sum(j[i] for j in temps)
        m = s / 5.0
        moyenne.append(m)
            
        
        print("temps moyen",m)
    return tailles, moyenne
#
taillesUnionF, tempsUnionF = Calcul_Union_File()



def graphiqueUnion():
    xF = np.array(taillesUnionF)
    yF = np.array(tempsUnionF)
    
    plt.title("Complexite Union File Binomiale")
    
    plt.plot(xF, yF, "o-", label="File")
    plt.legend()
    plt.xlabel("taille")
    plt.ylabel("temps(millisecondes")
    plt.savefig("Complexite_Union_FileBinomiale.png",dpi=1000)
    plt.show()
    
    #-----------ZOOM----------#
    
    xFz = np.array(taillesUnionF[:4])
    yFz = np.array(tempsUnionF[:4])
    
    plt.close()
    plt.title("Complexite Union File Binomiale Zoom")
    
    plt.plot(xFz, yFz, "o-", label="File")
    plt.legend()
    plt.xlabel("taille")
    plt.ylabel("temps(millisecondes")
#    plt.savefig("Complexite_Union_FileBinomialeZoom.png",dpi=1000)
    plt.show()



graphiqueUnion()









