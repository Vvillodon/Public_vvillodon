# -*- coding: utf-8 -*-
"""
Created on Mon May 22 22:02:45 2023

@author: vvill
"""
#Importation des modules 

import numpy as np
import matplotlib.pyplot as plt



#Definition des fonctions :
def debut_code():
     print("**************************************************************")
     print("*                                                            *")
     print("*         Bienvenue dans Profil NACA symétrique              *")
     print("*                                                            *")
     print("**************************************************************\n\n")
     print("=>Ce programme à pour but de tracer le le profil NACA symétrique d'une aile")
     
     
def entrer_information():
   
   
        
    numero_naca = input("Numéro du profil NACA 4 chiffres symétrique (NACA00XX) : ")
    longueur_de_corde = float(input("Corde du profil (en mètre) : "))
    nombre_de_point = int(input("Nombre de points le long de la corde pour le tracé : "))
    type_de_distribution = input("Type de distribution de points le long de la corde (linéaire ou non-uniforme) : ")
    
    
    return numero_naca,longueur_de_corde,nombre_de_point,type_de_distribution


def profile_NACA(numero_naca,longueur_de_corde,nombre_de_point,type_de_distribution):
    t = int(numero_naca[-2:]) / 100
    if type_de_distribution == "non-uniforme":
        theta = np.linspace(0, np.pi, nombre_de_point)
        xc = 0.5 * (1 - np.cos(theta))
    else :
        xc = np.linspace(0, 1, nombre_de_point)
   
    yt = 5 * t * (0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc**2 + 0.2843 * xc**3 - 0.1036 * xc**4)
    
    
    xup = xc * longueur_de_corde
    yup = yt * longueur_de_corde
    xdown = xup
    ydown = -yup
    
    epaisseur_max = np.max(yup)
    position_epaisseur_max = xup[np.argmax(yup)]

    return xup, yup, xdown, ydown, epaisseur_max, position_epaisseur_max

def affichage_data(epaisseur_max, position_epaisseur_max):
    print("Épaisseur maximale : ",format(epaisseur_max,4)," m")
    print("Position de l'épaisseur maximale : ",format(position_epaisseur_max), " m")


def affichage_courbe(xup, yup, xdown, ydown,numero_naca):
    plt.figure()
    plt.plot(xup, yup, label='Extrados')
    plt.plot(xdown, ydown, label='Intrados')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Profil  {}'.format(numero_naca))
    plt.grid(True)
    plt.legend()
    plt.show()
    
#Code principale

debut_code()
numero_naca,longueur_de_corde,nombre_de_point,type_de_distribution=entrer_information()
xup, yup, xdown, ydown, epaisseur_max, position_epaisseur_max = profile_NACA(numero_naca, longueur_de_corde, nombre_de_point, type_de_distribution)
affichage_data(epaisseur_max, position_epaisseur_max)
affichage_courbe(xup, yup, xdown, ydown,numero_naca)


