# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 08:33:07 2017

@author: alice
"""
import random

# Dans un premier temps on récupère les éléments du fichier iris apprentissage
with open("iris_apprentissage.txt","r") as fichier:
    iris_res=fichier.read()

listIris = iris_res.split("\n")

# On sépare pour chacun des éléments les différentes valeurs de leurs caractéristiques
mylist = [(listIris[i].split(" ")) for i in range(0,len(listIris)-1)]

# Enfin on cast les éléments de la liste pour en faire des nombres float au lieu de string
for i in range(len(mylist)):
    for j in range(len(mylist[i])):
        try:
            mylist[i][j] = float(mylist[i][j])
        except ValueError,e:
            print "error",e,"on line",i, j

# Autres initialisations
w0=[0,0,0,0]
mu_tab = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
T = 5*len(mylist)

resultat_perceptron= []

# Définition des fonctions permettant de calculer le Perceptron
def produitScalaire(w, x):
    res = w[0]
    for i in range(1,len(x)-1):
        res = res + w[i]*x[i]
    return res


def perceptron(w0, mu, T, liste):
    w = w0
    for t in range(1, T):
        elt = random.choice(liste)
        if (elt[0]*produitScalaire(w,elt) <= 0):
            w[0] = w[0]+ mu*elt[0] 
            for i in range(1, len(w)):
                w[i] = w[i]+ mu*elt[0]*elt[i]
    return w

# On exécute le Perceptron pour les différentes valeurs de mu 
for m in range(0, len(mu_tab)):
    resultat_perceptron.append(perceptron(w0, mu_tab[m], T, mylist))

print (resultat_perceptron)