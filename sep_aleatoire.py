# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:06:42 2017

@author: douria
"""
import random


with open("iris_resultat","r") as fichier:
    iris_res=fichier.read()

listIris = iris_res.split("\n")
random.shuffle(listIris)
pourcentage=int(0.66*len(listIris))
print pourcentage 

iris_apprentissage = open("iris_apprentissage.txt", 'w')
for i in range(pourcentage-2):
    iris_apprentissage.write(listIris[i]+"\n")
iris_apprentissage.write(listIris[pourcentage-1])
iris_apprentissage.close()

iris_test = open("iris_test.txt", 'w')
for i in range (pourcentage, (len(listIris)-2)):
    iris_test.write(listIris[i]+"\n")
iris_test.write(listIris[len(listIris)-1])  
iris_test.close()


    