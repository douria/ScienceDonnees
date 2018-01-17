# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 09:20:03 2018

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

#  récupérer les éléments
iris_list = recuplistfich("iris_apprentissage.txt")
#bCancer_list = recuplistfich("bCancer_apprentissageN.txt")
#mushroom_list = recuplistfich("mushroom_apprentissageN.txt")
#spambase_list = recuplistfich("spambase_apprentissageN.txt")

def norm(mylist):
    mylist_norm = mylist
    #fonction pour normaliser
    def maxi(tab, ind):
        m = tab[0][ind]
        for i in range(1,len(tab)):
            if tab[i][ind]>m:
                m=tab[i][ind]
        return m
        
    #on normalise les valeurs
    for i in range(1, len(mylist[0])):
        maxim = maxi(mylist, i)
        for j in range(0, len(mylist)):
            mylist_norm[j][i] = mylist[j][i]/maxim
    
    return mylist_norm

iris_list = norm(iris_list)

# Autres initialisations
#le pas d'appentissage
mu_tab = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
#précision
E = 0.01
#le nombre max d'itération
Tiris = 20*len(iris_list)
#TbCancer = 20*len(bCancer_list)
#Tmushroom = 20*len(mushroom_list)
#Tspambase = 20*len(spambase_list)



# Définition des fonctions permettant de calculer Adaline
def produitScalaire(w, x):
    res = w[0]
    for i in range(1,len(x)-1):
        res = res + w[i]*x[i]
    return res
    
def L(w,S):
    m = len(S)
    res = 0
    for i in range(0, len(S)):
        res = res + produitScalaire(w,S[i]) -S[i][0]
    return res/m

def adaline(mu, T, E, liste):
    w = [0,0,0,0,0]
    t = 0
    while t<T or E<=L(w,liste):
        elt = random.choice(liste) #choix exemple aléatoire
        #print(elt)
        w[0] = w[0] - 2*mu*(produitScalaire(w,elt)-elt[0])
        for i in range(1, len(w)):
            w[i] = w[i] - 2*mu*elt[i]*(produitScalaire(w,elt)-elt[0])
        t = t+1
    return w

def executeAdaline(listNorm, T, mu_tab, E):
    resultat_adaline= []
    # On exécute Adaline pour les différentes valeurs de mu 
    for m in range(0,len(mu_tab)):
        resultat_adaline.append(adaline(mu_tab[m], T, E, listNorm))
    
    print (resultat_adaline)
    return resultat_adaline

print("Iris Apprentissage:\n")
resultat_adaline_Iris = executeAdaline(iris_list, Tiris, mu_tab, E)
#print("BCancer Apprentissage:\n")
#resultat_adaline_BCancer = executeAdaline(bCancer_list, TbCancer, mu_tab, E)
#print("Mushroom Apprentissage:\n")
#resultat_adaline_Mushroom = executeAdaline(mushroom_list, Tmushroom, mu_tab, E)
#print("Spambase Apprentissage:\n")
#resultat_adaline_Spambase = executeAdaline(spambase_list, Tspambase, mu_tab, E)

# Partie test

iris_listTest = recuplistfich("iris_test.txt")
#bCancer_listTest = recuplistfich("bCancer_testN.txt")
#mushroom_listTest = recuplistfich("mushroom_testN.txt")
#spambase_listTest = recuplistfich("spambase_testN.txt")

# Autres initialisations
Niris = len(iris_listTest)
#NbCancer = len(bCancer_listTest)
#Nmushroom = len(mushroom_listTest)
#Nspambase = len(spambase_listTest)
perf_tab = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# Fonctions de calcul de la performance sur l'échantillon test
def testerAdaline(w_res, liste, N):
    perf = 0.0
    for i in range(0, N):
        ps = produitScalaire(w_res, liste[i])
        if((liste[i][0]*ps)>0):
            perf=perf+1.0
    print(perf/float(N))
    return perf/float(N)

def perfAdaline(w_res, mylistTest, N):    
    for i in range(0,len(w_res)):
        print(w_res[i])
        r = testerAdaline(w_res[i], mylistTest, N)
        print(r)
        perf_tab[i] = r
    return perf_tab

perf_Iris = perfAdaline(resultat_adaline_Iris,iris_listTest,Niris)
#perf_bCancer = perfAdaline(resultat_adaline_BCancer,bCancer_listTest,NbCancer)
#perf_mushroom = perfAdaline(resultat_adaline_Mushroom,mushroom_listTest,Nmushroom)
#perf_spambase = perfAdaline(resultat_adaline_Spambase,spambase_listTest,Nspambase)

print ("\n Performances Adaline Iris: \n")
print (perf_Iris)
#print ("\n Performances Adaline bCancer: \n")
#print (perf_bCancer)
#print ("\n Performances Adaline Mushroom: \n")
#print (perf_mushroom)
#print ("\n Performances Adaline Spambase: \n")
#print (perf_spambase)
