# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 11:37:10 2021

@author: Adity
"""
#with open ("sporsmaalsfil.txt","r", encoding = "UTF8") as fila: 
"""
class Quiz:
    def __init__(self, sporsmaal, svar_liste, korrekt_svar):
        self.sporsmaal = sporsmaal
        self.svar_liste = svar_liste
        self.korrektsvar = korrekt_svar
"""

"""
Sporsmaal =[]



with open("sporsmaalsfil.txt", "r") as fila:
    for linje in fila:
        spm = linje.split(":")
        print(spm)
        alteernative = linje[1].split(",") 
        rett_svar = linje[1]
        
        #liste_over_alle_spm.append(Question(spm, alternativ, svar))
        
        print(rett_svar)
"""






















class Quiz:
    def __init__(self, sporsmaal, svar_liste, korrekt_svar):
        self.sporsmaal = sporsmaal
        self.svar_liste = svar_liste
        self.korrekt_svar = korrekt_svar
        self.korrekt_svar_tekst = self.svar_liste[int(self.korrekt_svar)] 
        
        #not necessary to define korrek_svar_tekst as a self because it is defined by existing 
        #values, which are svar_liste[int(self.korrekt_svar)]

    def __str__(self):
        return f"{self.sporsmaal} \n {self.svar_liste}"
        
    def sjekk_svar(self, input_user):
        if self.korrekt_svar == input_user:
            return True
        else:
            return False
     
    def korrekt_svar_tekst(self):
        return (f"svaret er: {self.svar_liste[self.korrekt_svar]}")
    
    
        
if __name__=="__main__":
    
    sporsmaal =[]
   
    spiller1_score = 0
    spiller2_score = 0
    
    
    with open("sporsmaalsfil.txt", "r", encoding= "UTF8") as fila:
        for linje in fila:
            liste_av_linje = linje.split(":")
            spm = liste_av_linje[0]
            rett_svar = liste_av_linje[1].strip()
            alternativ = liste_av_linje[2].split(",") 
            rett_svar = int(rett_svar)
            sporsmaal.append(Quiz(spm, alternativ, rett_svar))
            
    for spm in sporsmaal:
        print(spm)
        input_user_1 = int(input("skriv svaret ditt"))
        input_user_2 = int(input("skriv svaret ditt"))
        if spm.sjekk_svar(input_user_1) :
            print("riktig")
            spiller1_score +=1
        else:
            print("feil")
        if spm.sjekk_svar(input_user_2) :
            print("riktig")
            spiller2_score +=1
        else:
            print("feil")
        print(spm.korrekt_svar_tekst)
    
    print(f"spiller 1 fikk {spiller1_score} poeng")
    print(f"spiller 2 fikk {spiller2_score} poeng")
    







































































"""        
st1=F1.readline()
print(st1)
"""






















"""
linje = 0

ordliste = dict()

with open ("sporsmaalsfil.txt","r", encoding = "UTF8") as fila:
    for i in fila:
                        #ordene= i.replace(" .", "")
                        #ordene = i.replace(",", "  ")
        ordene = i.split()
        linje = linje + 1
        
        
        for ordet in ordene:
            ordet = ordet.lower()
            
            if ordet not in ordliste:
                ordliste[ordet] = linje
                print(ordliste)
    
    
"""