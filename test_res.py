# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 12:00:07 2017

@author: douria
"""

import random


with open("iris_test","r") as fichier:
    iris_res=fichier.read()

listIris = iris_res.split("\n")
iris_res.close()

perf=0
N=length(listIris)

for i in range (0,N-1) :
    # on calcule le produit sclaire 
    produitScalaire=W[0]
    x=listIris[i].split(" ")
    for j in range(1,length(W)-1):
        somme=somme+x[j]*W[j]
    if((x[0]*somme)>0)
        perf=perf+1

#on affiche le pourcentage de bonne classification       
print perf/N
