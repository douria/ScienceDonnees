# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 10:25:56 2018

@author: alice
"""

import random
import numpy as np

def recuplistfich(name):
    # Dans un premier temps on récupère les éléments du fichier iris apprentissage
    with open(name,"r") as fichier:
        apprentissage_res=fichier.read()
    
    list_res = apprentissage_res.split("\n")
    
    # On sépare pour chacun des éléments les différentes valeurs de leurs caractéristiques
    mylist = [(list_res[i].split(" ")) for i in range(0,len(list_res)-1)]
    
    # Enfin on cast les éléments de la liste pour en faire des nombres float au lieu de string
    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            try:
                mylist[i][j] = float(mylist[i][j])
            except ValueError,e:
                print "error",e,"on line",i, j
    
    return mylist


    
# Définition des fonctions permettant de calculer Logistique
def produitScalaire(w, x):
    res = w[0]
    for i in range(1,len(x)-1):
        res = res + w[i]*x[i]
    return res
    
def sigma(x) :
    return 1 / (1 + np.exp(-x))
    
def L(w,S):
    m = len(S)
    res = 0
    for i in range(0, len(S)):
        res = res + produitScalaire(w,S[i]) -S[i][0]
    return res/m

def L_logistique(w,S) :
    m = len(S)
    somme = 0
    for i in range(1,m) :
        somme = somme + np.log(1 + np.exp(-S[i][0] * produitScalaire(w,S[i])))
    return somme/m

def logistique(mu, T, E, liste):
    w = [0.0]
    for i in range(1, len(liste[0])):
        w.append(random.randint(0,100)/100.)
    t = 0
    Rold = 1
    Rnew = 0
    while (t<T and abs(Rnew-Rold) > E ) :
        Rold = L_logistique(w, liste)
        
        # Choisir un exemple au hasard
        elt = random.choice(liste)
        s = 1 - sigma(elt[0]*produitScalaire(w, elt)) 
        w[0] = w[0] - mu*(-elt[0] * s)
        #print(str(elt)+" " + str(w))
        for i in range(1, len(w)):                
            w[i] = w[i] - mu*(-elt[0] * elt[i] * s)
        t = t+1
        
        Rnew = L_logistique(w, liste)
    return w

def executeLogistique(listNorm, T, mu_tab, E):
    resultat_logistique= []
    # On exécute la méthode logistique pour les différentes valeurs de mu 
    for m in range(0,len(mu_tab)):
        resultat_logistique.append(logistique(mu_tab[m], T, E, listNorm))
    
    #print (resultat_logistique)
    return resultat_logistique
    

# Fonctions de calcul de la performance sur l'échantillon test
def testerLogistique(w_res, liste, N):
    perf = 0.0
    for i in range(0, N):
        ps = produitScalaire(w_res, liste[i])
        if((liste[i][0]*ps)>0):
            perf=perf+1.0
    #print(perf/float(N))
    return perf/float(N)

def perfLogistique(w_res, mylistTest, N):
    perf_tab = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(0,len(w_res)):
        print(w_res[i])
        r = testerLogistique(w_res[i], mylistTest, N)
        print(r)
        perf_tab[i] = r
    return perf_tab

# Partie apprentissage
# récupérer les éléments
print("\nIRIS")
iris_list = recuplistfich("iris_apprentissageN.txt")
print("BCANCER")
bCancer_list = recuplistfich("bCancer_apprentissageN.txt")
print("MUSHROOM")
mushroom_list = recuplistfich("mushroom_apprentissageN.txt")
print("SPAMBASE")
spambase_list = recuplistfich("spambase_apprentissageN.txt")
print("\n")

# Autres initialisations
#le pas d'appentissage
mu_tab = [0.001, 0.01, 0.1, 1]
mu_tab = [0.001, 0.01, 0.1, 1, 10, 100, 1000]

#précision
E = 0.001
#le nombre max d'itération
Tiris = 20*len(iris_list)
TbCancer = 20*len(bCancer_list)
Tmushroom = 20*len(mushroom_list)
Tspambase = 20*len(spambase_list)

# Exécution de Logistique
resultat_logistique_Iris = executeLogistique(iris_list, Tiris, mu_tab, E)
resultat_logistique_BCancer = executeLogistique(bCancer_list, TbCancer, mu_tab, E)
resultat_logistique_Mushroom = executeLogistique(mushroom_list, Tmushroom, mu_tab, E)
resultat_logistique_Spambase = executeLogistique(spambase_list, Tspambase, mu_tab, E)

print("Iris Apprentissage:\n")
print(resultat_logistique_Iris)
print("\nBCancer Apprentissage:\n")
print(resultat_logistique_BCancer)
print("\nMushroom Apprentissage:\n")
print(resultat_logistique_Mushroom)
print("\nSpambase Apprentissage:\n")
print(resultat_logistique_Spambase)

# Partie test
iris_listTest = recuplistfich("iris_test.txt")
bCancer_listTest = recuplistfich("bCancer_testN.txt")
mushroom_listTest = recuplistfich("mushroom_testN.txt")
spambase_listTest = recuplistfich("spambase_testN.txt")

# Autres initialisations
Niris = len(iris_listTest)
NbCancer = len(bCancer_listTest)
Nmushroom = len(mushroom_listTest)
Nspambase = len(spambase_listTest)


perf_Iris = perfLogistique(resultat_logistique_Iris,iris_listTest,Niris)
perf_bCancer = perfLogistique(resultat_logistique_BCancer,bCancer_listTest,NbCancer)
perf_mushroom = perfLogistique(resultat_logistique_Mushroom,mushroom_listTest,Nmushroom)
perf_spambase = perfLogistique(resultat_logistique_Spambase,spambase_listTest,Nspambase)

print ("\n Performances Logistique Iris: \n")
print (perf_Iris)
print ("\n Performances Logistique bCancer: \n")
print (perf_bCancer)
print ("\n Performances Logistique Mushroom: \n")
print (perf_mushroom)
print ("\n Performances Logistique Spambase: \n")
print (perf_spambase)
