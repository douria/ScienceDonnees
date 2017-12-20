# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:47:15 2017

@author: douria
"""
with open("iris.data","r") as fichier:
    iris=fichier.read()

iris_resultat=""
listIris = iris.split("\n")

for i in range(len(listIris)-1):
    listl=listIris[i].split(",")
    if(listl[4]=="Iris-setosa"):
        iris_resultat+="+1 "
    else :
        iris_resultat+="-1 "
    iris_resultat+=listl[0]+" "+listl[1]+" "+listl[2]+" "+listl[3]
    if(i!=len(listIris)-1)
    iris_resultat+="\n"
print(iris_resultat)
