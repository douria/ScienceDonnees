# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:47:15 2017

@author: douria
"""

with open("spambase.data","r") as fichier:
    fich_donnees=fichier.read()

fich_res=""
listdonnees = fich_donnees.split("\n")

def RBCancer(listdonnees):
    fich_resultat=""
    classe="M"
    listeDBC=normaliser(listdonnees,1)
    for i in range(len(listeDBC)-1):
       # listl=listeDBC[i].split(",")
        if(listeDBC[i][1]==classe):
            fich_resultat+="+1"
        else :
            fich_resultat+="-1"
        for j in range (len(listeDBC[i])-1):
           if(j>1):
               fich_resultat+=" "+str(listeDBC[i][j])
        if(i!=len(listeDBC)-1):
            fich_resultat+="\n"
    return fich_resultat

def spambase(listdonnees):
    fich_resultat=""
    classe="1"
    listeM=normaliser(listdonnees,0)
    for i in range(len(listeM)-1):
        if(listeM[i][0]==classe):
            fich_resultat+="+1"
        else :
            fich_resultat+="-1"
        for j in range (len(listeM[i])-1):
           if(j>1):
               fich_resultat+=" "+str(listeM[i][j])
        if(i!=len(listeM)-1):
            fich_resultat+="\n"
    return fich_resultat
    
def mushroom(listdonnees):
    fich_resultat=""
    listeM=normaliserAlph(listdonnees)
    for i in range(len(listeM)-1):
        if(listeM[i][0]=='p'):
            fich_resultat+="+1"
        else :
            fich_resultat+="-1"
        for j in range (len(listeM[i])-1):
           if(j>1):
               fich_resultat+=" "+str(listeM[i][j])
        if(i!=len(listeM)-1):
            fich_resultat+="\n"
    return fich_resultat
    
    
def iris():
    fich_resultat=""
    classe="Iris-setosa"
    for i in range(len(listdonnees)-1):
        listl=listdonnees[i].split(",")
        if(listl[4]==classe):
            fich_resultat+="+1 "
        else :
            fich_resultat+="-1 "
        fich_resultat+=listl[0]+" "+listl[1]+" "+listl[2]+" "+listl[3]
        if(i!=len(listdonnees)-1):
            fich_resultat+="\n"
    return fich_resultat


def normaliserAlph (tabLecture): 
   listA=tabLecture[0].split(",")
   listMax=[]
   # on met tout l'alphabet en entier 
   for i in range(len(listA)-1):
       listMax.append(ord(listA[i])-96)
   listTab=[]
   #on reparcours tout le data afin de trouver le tableau max 
   for i in range(len(tabLecture)-1):
      listl=tabLecture[i].split(",")
      for j in range(len(listl)-1):
          if( j>0 and ((ord(listl[j])-96)>listMax[j])):
              listMax[j]=ord(listl[j])-96
   
   #normaliser les caracteristiques du tableau 
   for i in range(len(tabLecture)-1):  
       listl=tabLecture[i].split(",")
       for j in range(len(listl)-1):
           if(j>0):
              listl[j]=float(ord(listl[j])-96)/float(listMax[j])
       listTab.append(listl)
   return listTab


def normaliser (tabLecture,startindex): 
   listMax=tabLecture[0].split(",")
   listTab=[]
   for i in range(len(tabLecture)-1):
      listl=tabLecture[i].split(",")
      for j in range(len(listl)-1):
          if( j>startindex and float(listl[j])>float(listMax[j])):
              listMax[j]=listl[j]
   
   #normaliser les caracteristiques du tableau 
   for i in range(len(tabLecture)-1):  
       listl=tabLecture[i].split(",")
       for j in range(len(listl)-1):
           if(j>startindex):
              listl[j]=float(listl[j])/float(listMax[j])
       listTab.append(listl)
   return listTab
#on affiche le resultat 
fich_res=spambase(listdonnees)
print fich_res