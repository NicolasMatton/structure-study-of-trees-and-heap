# -*- coding: utf-8 -*-

from TasBinomial import *
import numpy as np
import matplotlib.pyplot as plt
import time
plt.show() # affiche la figure a l'ecra
"""Question 2.5"""



#------------------------Q2.5---------------------------

def Calcul_ConsIter_Arbre():
    tailles=[100, 200, 500, 1000, 5000, 10000, 20000, 50000]
    temps=[]
    for t in tailles:
        jeux=[]
        for i in range(1,6):
            f=open("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(t)+".txt")
            cles=[]
            for l in f:
               cles.append(int(l[:-1],0)) #int(l[:-1],0) permet de recuperer la valeur 128 bit sous forme de 
                                          #chaine de caracteres et la converti en int (le second parametre
                                          #permettant de preciser que la valeur est en 128bit)
                                          #:-1 pour ne pas avoir le /n
            jeux.append(cles)
            f.close()
        time_tmp=[]
        ##print(jeux)
        
        print("\n------\ncalcul de temps de construction pour",t,"valeurs")
        for j in jeux:
            t1_start=time.time()
            a=ConsIter_Arbre(j)
            t2_end=time.time()
            t_exec = (t2_end - t1_start)*1000.0
            time_tmp.append(t_exec)
            print("pour le jeu ",jeux.index(j),":",t_exec, "millisecondes")
            moyenne=sum(time_tmp)/len(time_tmp)
        temps.append(moyenne)
        print("temps moyen",moyenne)
    
    return tailles,temps

def Calcul_ConsIter_Tableau():
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
            t1_start = time.time()
            a = ConsIter_Tableau(j)
            
            t2_end = time.time()
            t_exec = (t2_end - t1_start)*1000.0
            time_tmp.append(t_exec)
            print("pour le jeu ",jeux.index(j),":",t_exec, "millisecondes")
            moyenne=sum(time_tmp)/len(time_tmp)
        temps.append(moyenne)
        print("temps moyen",moyenne)
    
    return tailles,temps

#taillesA, tempsA = Calcul_ConsIter_Arbre()
#taillesT, tempsT = Calcul_ConsIter_Tableau()
##
#

def graphique():
    xA = np.array(taillesA)
    yA = np.array(tempsA)
    
    xT = np.array(taillesT)
    yT = np.array(tempsT)
    
    plt.title("Complexite ConsIter Tas Binomial")
    
    plt.plot(xA, yA, "o-", label="Arbre")
    plt.plot(xT, yT, "o--", label="Tableau")
    plt.legend()
    plt.xlabel("taille")
    plt.ylabel("temps(millisecondes")
    plt.savefig("Complexite_ConsIter_Tas_Binomial.png",dpi=1000)
    plt.show()
    
    #-----------ZOOM----------#
    
    xAz = np.array(taillesA[:4])
    yAz = np.array(tempsA[:4])
    
    xTz = np.array(taillesT[:4])
    yTz = np.array(tempsT[:4])
    plt.close()
    plt.title("Complexite ConsIter Tas Binomial Zoom")
    
    plt.plot(xAz, yAz, "o-", label="Arbre")
    plt.plot(xTz, yTz, "o--", label="Tableau")
    plt.legend()
    plt.xlabel("taille")
    plt.ylabel("temps(millisecondes")
    #plt.savefig("Complexite_ConsIter_Tas_Binomial_Zoom.png",dpi=1000)
    plt.show()

#graphique()

#--------------------------2.6---------------------
    
def Calcul_Union_Arbre():
    tailles=[100, 200, 500, 1000, 5000, 10000, 20000, 50000]
    temps=[]
    for i in range(1,6):
        
        print("\npour le jeu ",i,"\n")
        listes=[]
        for  t in tailles:
            f=open("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(t)+".txt")
            cles=[]
            for l in f:
               cles.append(int(l[:-1],0)) #int(l[:-1],0) permet de recuperer la valeur 128 bit sous forme de 
                                          #chaine de caracteres et la converti en int (le second parametre
                                          #permettant de preciser que la valeur est en 128bit)
                                          #:-1 pour ne pas avoir le /n
            listes.append(ConsIter_Arbre(cles))
            f.close()
        time_tmp=[]
        for j in range(len(listes)):
            t1_start=time.time()
            a=Union_Arbre(listes[j],listes[len(listes)-1])
            t2_end=time.time()
            t_exec = (t2_end - t1_start)*1000.0
            time_tmp.append(t_exec)
            print("pour les tailles ",tailles[j],"et",tailles[len(listes)-1],":",t_exec, "millisecondes")
        temps.append(time_tmp)
        
    moyenne = []
        
    for i in range(8):
        s = sum(j[i] for j in temps)
        m = s / 5.0
        moyenne.append(m)
            
        
        print("temps moyen",m)
    return tailles, moyenne

def Calcul_Union_Tableau():
    tailles=[100, 200, 500, 1000, 5000, 10000, 20000, 50000]
    temps=[]
    for i in range(1,6):
        
        print("\npour le jeu ",i,"\n")
        listes=[]
        for  t in tailles:
            f=open("cles_alea/jeu_"+str(i)+"_nb_cles_"+str(t)+".txt")
            cles=[]
            for l in f:
               cles.append(int(l[:-1],0)) #int(l[:-1],0) permet de recuperer la valeur 128 bit sous forme de 
                                          #chaine de caracteres et la converti en int (le second parametre
                                          #permettant de preciser que la valeur est en 128bit)
                                          #:-1 pour ne pas avoir le /n
            listes.append(ConsIter_Tableau(cles))
            f.close()
        time_tmp=[]
        
        
        for j in range(len(listes)):
            t1_start=time.time()
            a=Union_Tableau(listes[j],listes[len(listes)-1])
            t2_end=time.time()
            t_exec = (t2_end - t1_start)*1000.0
            time_tmp.append(t_exec)
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
taillesUnionA, moyenneUnionA = Calcul_Union_Arbre()
taillesUnionT, moyenneUnionT = Calcul_Union_Tableau()



def graphiqueUnion():
    xA = np.array(taillesUnionA)
    yA = np.array(moyenneUnionA)
    
    xT = np.array(taillesUnionT)
    yT = np.array(moyenneUnionT)
    
    plt.title("Complexite Union Tas Binomial")
    
    plt.plot(xA, yA, "o-", label="Arbre")
    plt.plot(xT, yT, "o--", label="Tableau")
    plt.legend()
    plt.xlabel("taille")
    plt.ylabel("temps(millisecondes")
    plt.savefig("Complexite_Union_TasBinomial.png",dpi=1000)
    plt.show()
    
    #-----------ZOOM----------#
    
    xAz = np.array(taillesUnionA[:4])
    yAz = np.array(moyenneUnionA[:4])
    
    xTz = np.array(taillesUnionT[:4])
    yTz = np.array(moyenneUnionT[:4])
    plt.close()
    plt.title("Complexite Union Tas Binomial Zoom")
    
    plt.plot(xAz, yAz, "o-", label="Arbre")
    plt.plot(xTz, yTz, "o--", label="Tableau")
    plt.legend()
    plt.xlabel("taille")
    plt.ylabel("temps(millisecondes")
    #plt.savefig("Complexite_Union_TasBinomial_Zoom.png",dpi=1000)
    plt.show()




graphiqueUnion()




