# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:47:15 2017

@author: douria
"""



def RBCancer():
    with open("BCancer.data","r") as fichier:
        fich_donnees = fichier.read()
    fichRes = open("Cancer_resultat1.txt", 'w')    

    listdonnees = fich_donnees.split("\n")

    classe="M"
    listeDBC=normaliser(listdonnees,1)
    for i in range(len(listeDBC)-1):
       # listl=listeDBC[i].split(",")
        if(listeDBC[i][1]==classe):
             fichRes.write("+1") 
        else :
            fichRes.write("-1") 
        for j in range (len(listeDBC[i])-1):
           if(j>1):
                fichRes.write(" "+str(listeDBC[i][j]))
        if(i!=len(listeDBC)-1):
             fichRes.write("\n")
    fichRes.close() 


def spambase():
    with open("spambase.data","r") as fichier:
        fich_donnees=fichier.read()

    listdonnees = fich_donnees.split("\n")
    
    classe="1"
    listeM=normaliser(listdonnees,0)
    
    fichRes = open("spambase_resultat1.txt", 'w')    
    for i in range(len(listeM)-1):
        if(listeM[i][0]==classe):
            fichRes.write("+1")  
        else :
            fichRes.write("-1")  
        for j in range (len(listeM[i])-1):
           if(j>1):
               fichRes.write(" "+str(listeM[i][j]))  

        if(i!=len(listeM)-1):
             fichRes.write("\n")
    fichRes.close() 

    
def mushroom():
    with open("mushroom.data","r") as fichier:
         fich_donnees=fichier.read()
    listdonnees = fich_donnees.split("\n")
    
    listeM=normaliserAlph(listdonnees)
    fichRes = open("mushroom_resultat1.txt", 'w')    

    for i in range(len(listeM)-1):
        if(listeM[i][0]=='p'):
            fichRes.write("+1") 
        else :
            fichRes.write("-1") 
        for j in range (len(listeM[i])-1):
           if(j>1):
               fichRes.write(" "+str(listeM[i][j])) 
        if(i!=len(listeM)-1):
            fichRes.write("\n")
    fichRes.close() 

    
    
def iris():
    with open("iris.data","r") as fichier:
         fich_donnees=fichier.read()

    listdonnees = fich_donnees.split("\n")    
    
    listN = normaliser(listdonnees,0)
    fichRes = open("iris_resultat1.txt", 'w')    

    classe="Iris-setosa"
    for i in range(len(listdonnees)-1):
        listl=listdonnees[i].split(",")
        if(listl[4]==classe):
            fichRes.write("+1") 
        else :
            fichRes.write("-1") 
        fichRes.write(str(listN[i][0])+" "+str(listN[i][1])+" "+str(listN[i][2])+" "+str(listN[i][3])) 
        if(i!=len(listdonnees)-1):
            fichRes.write("\n")
    fichRes.close() 


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

iris()
spambase()
mushroom()
RBCancer()
#on affiche le resultat 
#fich_res=spambase(listdonnees)
#print fich_res