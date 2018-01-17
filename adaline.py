# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 09:20:03 2018

@author: alice
"""

import random
import numpy as np
import Science_donnees as sdd

## Dans un premier temps on récupère les éléments du fichier iris apprentissage
#with open("iris_apprentissage.txt","r") as fichier:
#    iris_apprentissage_res=fichier.read()
#
#listIris = iris_apprentissage_res.split("\n")
#
## On sépare pour chacun des éléments les différentes valeurs de leurs caractéristiques
#mylist = [(listIris[i].split(" ")) for i in range(0,len(listIris)-1)]
#
## Enfin on cast les éléments de la liste pour en faire des nombres float au lieu de string
#for i in range(len(mylist)):
#    for j in range(len(mylist[i])):
#        try:
#            mylist[i][j] = float(mylist[i][j])
#        except ValueError,e:
#            print "error",e,"on line",i, j
#
#mylist_norm = mylist
##fonction pour normaliser
#def maxi(tab, ind):
#    m = tab[0][ind]
#    for i in range(1,len(tab)):
#        if tab[i][ind]>m:
#            m=tab[i][ind]
#    return m
#    
##on normalise les valeurs
#for i in range(1, len(mylist[0])):
#    maxim = maxi(mylist, i)
#    for j in range(0, len(mylist)):
#        mylist_norm[j][i] = mylist[j][i]/maxim


#  récupérer les éléments
listNormRBCancer = sdd.RBCancer
listNormIris = sdd.iris
listNormMushroom = sdd.mushroom
listNormSpambase = sdd.spambase


# Autres initialisations
#le pas d'appentissage
mu_tab = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
#précision
E = 0.01
#le nombre max d'itération
T = 20*len(mylist)

resultat_adaline= []

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

# On exécute Adaline pour les différentes valeurs de mu 
for m in range(0,len(mu_tab)):
    resultat_adaline.append(adaline(mu_tab[m], T, E, mylist_norm))

print (resultat_adaline)



# Partie test
# Dans un premier temps on récupère les éléments du fichier iris test
with open("iris_test.txt","r") as fichier:
    iris_test_res=fichier.read()

listIrisTest = iris_test_res.split("\n")

# On sépare pour chacun des éléments les différentes valeurs de leurs caractéristiques
mylistTest = [(listIrisTest[i].split(" ")) for i in range(0,len(listIrisTest)-1)]

# Enfin on cast les éléments de la liste pour en faire des nombres float au lieu de string
for i in range(len(mylistTest)):
    for j in range(len(mylistTest[i])):
        try:
            mylistTest[i][j] = float(mylistTest[i][j])
        except ValueError,e:
            print "error",e,"on line",i, j


# Autres initialisations
N=len(mylistTest)
perf_tab = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# Fonction de calcul de la performance sur l'échantillon test
def testerAdaline(w_res, liste):
    perf = 0.0
    for i in range(0, N):
        ps = produitScalaire(w_res, liste[i])
        if((liste[i][0]*ps)>0):
            perf=perf+1.0
    print(perf/float(N))
    return perf/float(N)

#for i in range(0,len(resultat_adaline)):
#    print(resultat_adaline[i])
#    r = testerAdaline(resultat_adaline[i], mylistTest)
#    print(r)
#    perf_tab[i] = r

#print (perf_tab)
