# -*- coding: utf-8 -*-
"""
Created on Tue May 16 14:28:12 2023

@author: vvill

Jeu du pendu 

Ce code permet de jouer au jeu du pendu. 
Il fonctionne avec un fichier mot_pendu.txt qui sert de dictionnaire de mot.

"""

#Importation des modules 
import string
import random

#Définition des fonctions 

def choix_de_mot(dictionnaire="mots_pendu.txt"):

    with open(dictionnaire, 'r') as file:  
        liste_mots = []
        lignes = file.readlines()
        for ligne in lignes:
            mot = ligne.strip()  # Permet d'enlever les caractères de nouvelle ligne (\n) 
            liste_mots.append(mot)
    return random.choice(liste_mots) #Choisi un mot au hasard dans la liste


def affichage(mot,lettre_trouvees,nombre_de_chance,lettres_entrees):
    print("Il reste ",nombre_de_chance," chances. Le mot a trouvé est : ")
    mots_tronque=""   #Création du mot à trou en fonction des lettres déjà trouvé
    for char in mot :
        if char in lettre_trouvees:
            mots_tronque+=char + " "
        else :
            mots_tronque+=" _ "
    print(mots_tronque)        
    print("\nVous avez déja entré les lettres : ",lettres_entrees) 
  

def entrer_une_lettre(lettres_trouvees,lettres_entrees,alphabet):
    lettre=(input("Entrez une lettre  : "))
    
      
    if lettre in alphabet :   # Vérifie si la lettre est un caractère le l'alphabet
        if lettre in lettres_entrees or lettre in lettres_trouvees or len(lettre)!=1:      #Vérifi si le caractère est une seule lettre ou si la lettre à déjà été trouvée
            print("Vous avez déjà entrer cette lettre, veuillez recommencer.\n")
            return entrer_une_lettre(lettres_trouvees, lettres_entrees,alphabet)
        else :
            return lettre.lower()    
    else :
        print("Vous n'avez pas entré une lettre minuscule, veuillez recommencer.\n")
        return entrer_une_lettre(lettres_trouvees, lettres_entrees,alphabet)
        

def debut_partie():
    print("**************************************************************")
    print("*                                                            *")
    print("*            Bienvenue dans le jeu du pendu                  *")
    print("*                                                            *")
    print("**************************************************************\n\n")
    print("=>L'objectif est de trouver le mot choisit par l'ordianteur. Vous avez le droit à 6 chances.\n")
    reponse=str(input("Etes-vous-prêt? yes/no \n"))
    if reponse=="yes" :
        jouer()
    else :
        fin_de_partie()
        

def fin_de_partie():
    print("Merci d'avoir jouer au pendu")
    
def verification_mot(mots,lettres_trouvees):
    erreur=0
    for char in mots:
        if char in lettres_trouvees:
            erreur+=0
        else :
            erreur+=1
    if erreur==0:
        return True
    else :
        return False
    

def jouer():
    print("----------Debut de la partie----------------\n")
    mots=choix_de_mot()
    print("L'odinateur à choisi un mot")
    lettres_trouvees=""
    lettres_entrees=""
    nombre_de_chance=6
    verif=False
    while nombre_de_chance!=0 and verif==False:
        affichage(mots, lettres_trouvees, nombre_de_chance, lettres_entrees)
        lettre=entrer_une_lettre(lettres_trouvees, lettres_entrees,string.ascii_letters)   
        if lettre in mots : 
            lettres_trouvees+=lettre
        else :
            lettres_entrees+=lettre
            nombre_de_chance-=1
        verif=verification_mot(mots, lettres_trouvees)
    print("----------Fin de la partie----------------\n")
    if verif==True :
        print("Bravo ! Vous avez trouver le mot", mots," en ", 6-nombre_de_chance, "tours.")
    else :
        print("Dommage, vous n'avez pas réussi à trouver le mots. Le mot à trouvé était :", mots)
    reponse=input("Voulez vous rejouer? yes/no \n")
    if reponse=="yes" :
        jouer()
    else :
        fin_de_partie()
    



    
    
#Code principale
debut_partie()