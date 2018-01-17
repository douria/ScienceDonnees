# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:06:42 2017

@author: douria
"""
import random



def random_sep(name,nameResApprentissage,nameResTest):
    with open(name,"r") as fichier:
        res=fichier.read()    


    list = res.split("\n")
    random.shuffle(list)
    pourcentage=int(0.66*len(list))
    print pourcentage 
    
    iris_apprentissage = open(nameResApprentissage+".txt", 'w')
    for i in range(pourcentage-2):
        iris_apprentissage.write(list[i]+"\n")
    iris_apprentissage.write(list[pourcentage-1])
    iris_apprentissage.close()
    
    iris_test = open(nameResTest+".txt", 'w')
    for i in range (pourcentage, (len(list)-2)):
        iris_test.write(list[i]+"\n")
    iris_test.write(list[len(list)-1])  
    iris_test.close()


random_sep("iris_resultat1.txt","iris_apprentissage", "iris_test")
random_sep("mushroom_resultat1.txt","mushroom_apprentissage", "mushroom_test")
random_sep("spambase_resultat1.txt","spambase_apprentissage", "spambase_test")
random_sep("bCancer_resultat1.txt","bCancer_apprentissage", "bCancer_test")
random_sep("iris_resultatN.txt","iris_apprentissageN", "iris_testN")
random_sep("mushroom_resultatN.txt","mushroom_apprentissageN", "mushroom_testN")
random_sep("spambase_resultatN.txt","spambase_apprentissageN", "spambase_testN")
random_sep("bCancer_resultatN.txt","bCancer_apprentissageN", "bCancer_testN")
    