# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 12:00:07 2017

@author: douria
"""
import numpy as np

with open("iris_test.txt","r") as fichier:
    iris_res=fichier.read()

listIris = iris_res.split("\n")
W=np.array([1, 2, 3, 4, 5])
#W={2,3,4,8,1,2,6}
perf=0
N=len(listIris)

for i in range (0,N-1) :
    # on calcule le produit sclaire 
    produitScalaire=W[0]
    x=listIris[i].split(" ")
    for j in range(1,len(W)-1):
        produitScalaire=produitScalaire+(float(x[j])*float(W[j]))
    if((float(x[0])*produitScalaire)>0):
        perf=perf+1

#on affiche le pourcentage de bonne classification       
print perf/N
