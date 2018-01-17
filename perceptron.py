# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 08:33:07 2017

@author: alice
"""
import random

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


# Définition des fonctions permettant de calculer le Perceptron
def produitScalaire(w, x):
    res = w[0]
    for i in range(1,len(x)-1):
        res = res + w[i]*x[i]
    return res


def perceptron(mu, T, liste):
    w = [0,0,0,0]
    for t in range(1, T):
        elt = random.choice(liste)
        #print(elt)
        if (elt[0]*produitScalaire(w,elt) <= 0):
            w[0] = w[0]+ mu*elt[0] 
            for i in range(1, len(w)):
                w[i] = w[i]+ mu*elt[0]*elt[i]
    return w

def executePerceptron(mylist, T, mu_tab):
    resultat_perceptron= []
    # On exécute Perceptron pour les différentes valeurs de mu 
    for m in range(0,len(mu_tab)):
        resultat_perceptron.append(perceptron(mu_tab[m], T, mylist))
    #print (resultat_perceptron)
    
    return resultat_perceptron


# Fonction de calcul de la performance sur l'échantillon test
def testerPerceptron(w_res, liste, N):
    perf = 0.0
    for i in range(0, N):
        ps = produitScalaire(w_res, liste[i])
        if((liste[i][0]*ps)>0):
            perf=perf+1.0
    #print(perf/float(N))
    return perf/float(N)

def perfPerceptron(resultat_perceptron,mylistTest, N):
    perf_tab = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(0,len(resultat_perceptron)):
        #print(resultat_perceptron[i])
        r = testerPerceptron(resultat_perceptron[i], mylistTest, N)
        #print(r)
        perf_tab[i] = r
    
    #print (perf_tab)
    return perf_tab


# Partie Apprentissage
#  récupérer les éléments
iris_list = recuplistfich("iris_apprentissage.txt")
#bCancer_list = recuplistfich("bCancer_apprentissage.txt")
#mushroom_list = recuplistfich("mushroom_apprentissage.txt")
#spambase_list = recuplistfich("spambase_apprentissage.txt")

# Autres initialisations
mu_tab = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
T = 7

print("Iris Apprentissage:\n")
resultat_perceptron_Iris = executePerceptron(iris_list, T, mu_tab)
print(resultat_perceptron_Iris)
#print("BCancer Apprentissage:\n")
#resultat_perceptron_BCancer = executePerceptron(bCancer_list, T, mu_tab)
#print(resultat_perceptron_BCancer)
#print("Mushroom Apprentissage:\n")
#resultat_perceptron_Mushroom = executePerceptron(mushroom_list, T, mu_tab)
#print(resultat_perceptron_Mushroom)
#print("Spambase Apprentissage:\n")
#resultat_perceptron_Spambase = executePerceptron(spambase_list, T, mu_tab)
#print(resultat_perceptron_Spambase)

# Partie test
iris_listTest = recuplistfich("iris_test.txt")
#bCancer_listTest = recuplistfich("bCancer_test.txt")
#mushroom_listTest = recuplistfich("mushroom_test.txt")
#spambase_listTest = recuplistfich("spambase_test.txt")


# Autres initialisations
Niris = len(iris_listTest)
#NbCancer = len(bCancer_listTest)
#Nmushroom = len(mushroom_listTest)
#Nspambase = len(spambase_listTest)

perf_Iris = perfPerceptron(resultat_perceptron_Iris,iris_listTest,Niris)
#perf_bCancer = perfPerceptron(resultat_perceptron_BCancer,bCancer_listTest,NbCancer)
#perf_mushroom = perfPerceptron(resultat_perceptron_Mushroom,mushroom_listTest,Nmushroom)
#perf_spambase = perfPerceptron(resultat_perceptron_Spambase,spambase_listTest,Nspambase)

print ("\n Performances Perceptron Iris: \n")
print (perf_Iris)
#print ("\n Performances Perceptron bCancer: \n")
#print (perf_bCancer)
#print ("\n Performances Perceptron Mushroom: \n")
#print (perf_mushroom)
#print ("\n Performances Perceptron Spambase: \n")
#print (perf_spambase)
