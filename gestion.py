# les sous-programmes 
from pickle import *
from numpy import array
date={"j":int(),
      "m":int(),
      "a":int()}
enreg={"cp":str(),
       "dg":str(),
       "dc":date,
       "quantite":int()}

def remplir(np):
    F = open(np,"wb")
    e = dict(enreg)
    saisir(e,0)
    dump(e,F)
    x = 1
    test = True
    while test :
        rep = input("voulez-vous contunier O/N : ")
        while not ( rep == "O" or rep == "N"):
            rep = input("voulez-vous contunier O/N : ")
        if rep == "O" :
            print("---------------------")
            saisir(e,x)
            dump(e,F)
            x += 1
        test =  rep == "O"
    F.close()
    return x

def saisir(e,i):
    # remplir premier champ
    e["cp"] = input("Enter le code du produit n " + str(i + 1) + ": ")
    while not((len(e["cp"])==5) and (verif(e["cp"])) ):
        e["cp"] = input("Le code du produit doit etre une chaine numerique de longueur 5 : ")
    # remplir deuxieme champ
    e["dg"] = input("Enter la designation n " + str(i + 1) + ": ")
    while not( len(e["dg"]) <= 20):
        e["dg"] = input("La designation doit etre une chaine contenant au maximum 20 caracteres : ")
    # remplir troisieme champ
    e["dc"]["j"] = int(input("Enter le jour de consommation n " + str(i + 1) + ": "))
    while not( 1 <= e["dc"]["j"] <= 31):
        e["dc"]["j"] = int(input("Le jour doit etre entre 1 et 31 : "))
    e["dc"]["m"] = int(input("Enter le mois de consommation n " + str(i + 1) + ": "))
    while not( 1 <= e["dc"]["m"] <= 12):
        e["dc"]["m"] = int(input("Le mois doit etre entre 1 et 12 : "))
    e["dc"]["a"] = int(input("Enter l'annee de consommation n " + str(i + 1) + ": "))
    while not( 2022 <= e["dc"]["a"] <= 2025):
        e["dc"]["a"] = int(input("L'anne doit etre entre 2022 et 2025 : "))   
    # remplir dernier champ
    e["quantite"] = int(input("Enter la quantite n " + str(i + 1) + ": "))
    while not(e["quantite"] >= 0):
        e["quantite"] = input("La quantite doit etre un entier positive : ")
        
def verif(ch):
    i = 0
    while i < len(ch) :
        test = "0" <= ch[i] <= "9"
        i +=  1
    return test

def gestion(np,x):
    print("******** GESTION DE PRODUIT ******** ")
    print("A : Ajouter un nouveau produit .")
    print("S : Supprimer un produit .")
    print("M : Modifier le designation d'un produit .")
    print("T : Trier en ordre croissant de la designation .")
    rep = input("Quelle gestion voulez-vous faire ? A/S/M/T ")
    if rep == "A" :
        ajouter(np,x)
    elif rep == "S" :
        code = input("Enter le code du produit : ")
        supprimer(np,x,code)
    elif rep == "M" :
        code = input("Enter le code du produit : ")
        modifier(np,x,code)
    elif rep == "T" :
        trier(np,x)
 
def ajouter(np,x):
    np1 = "stock1.dat"
    F = open(np,"rb")
    e = dict(enreg)
    D = open(np1,"wb")
    for i in range (x):
        e = load(F)
        dump(e,D)
    saisir(e,x)
    n1 = x + 1
    dump(e,D)
    affiche(np1,n1)
    F.close()
    D.close()
    
    
def supprimer(np,x,c):
    np1 = "stock1.dat"
    F = open(np,"rb")
    e = dict(enreg)
    D = open(np1,"wb")
    n1 = 0
    for i in range (x):
        e = load(F)
        if c != e["cp"] :
            dump(e,D)
            n1 += 1 
    affiche(np1,n1+1)
    F.close()
    D.close()
    
def modifier(np,x,c):
    np1 = "stock1.dat"
    F = open(np,"rb")
    e = dict(enreg)
    e1 = dict(enreg)
    D = open(np1,"wb")
    for i in range (x):
        e = load(F)
        if c == e["cp"] :
            e1["cp"] = e["cp"]
            e1["dg"] = input("Enter la nouvelle designation n " + str(i + 1) + ": ")
            while not( len(e1["dg"]) <= 20):
                e1["dg"] = input("La designation doit etre une chaine contenant au maximum 20 caracteres : ")
            e1["dc"]["j"] = e["dc"]["j"]
            e1["dc"]["m"] = e["dc"]["m"]
            e1["dc"]["a"] = e["dc"]["a"]
            e1["quantite"] = e["quantite"]
            
        else:
            e1["cp"] = e["cp"]
            e1["dg"] = e["dg"] 
            e1["dc"]["j"] = e["dc"]["j"]
            e1["dc"]["m"] = e["dc"]["m"]
            e1["dc"]["a"] = e["dc"]["a"]
            e1["quantite"] = e["quantite"]
        dump(e1,D)
    affiche(np1,x)
    F.close()
    D.close()

def trier(np,x):
    np1 = "stock1.dat"
    F = open(np,"rb")
    e = dict(enreg)
    D = open(np1,"wb")
    t = array([enreg]*x)
    for i in range(x):
        e = load(F)
        t[i] = e
    tri(t,x)
    for i in range(x):
        dump(t[i],D)
    affiche(np1,x)
    F.close()
    D.close()
def tri(t,x):
    aux = dict(enreg)
    permut = False
    while permut == False and x > 1 :
        permut = False
        for i in range(x-2):
            if t["dg"][i] > t["dg"][i+1]:
                aux = t[i]
                t[i] = t[i+1]
                t[i+1] = aux
                permut = True
            x = x - 1
    return t
def affiche(np,x):
    F = open(np,"rb")
    e = dict(enreg)
    for i in range(x):
        e = load(F)
        print("le code du produit : ",e["cp"])
        print("la designation : ",e["dg"])
        print("la date consommation : ",e["dc"]["j"],"/",e["dc"]["m"],"/",e["dc"]["a"])
        print("la quantite : ",e["quantite"])
    F.close()
        
# le PP
nph = "stock.dat"
n = remplir(nph)
gestion(nph,n)

        
    
        
    
    
    
    
    
    
