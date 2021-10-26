# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 17:26:21 2021

@author: Adity
"""

class Capital:
    def __init__(self, sporsmaal, svar_liste, korrekt_svar):
        self.sporsmaal = sporsmaal
        self.svar_alternative = svar_liste
        self.korrektsvar = korrekt_svar
# the lines above are the functions that are needed for the assignment to work
    
    def __str__(self):
        return f"{self.sporsmaal} \n {self.svar_alternative}"
        
    def sjekk_svar(self):
        input_user = int(input("hva er svaret ditt? "))
        if self.korrektsvar == input_user:
            print("riktig \n")
        
        else:
            print("feil")
            
# these line from __str__ to sjekk_svar are used to produce when the result i correct or false    
        
if __name__=="__main__":
    hovedstad_liste = ("stavenger trykk (0) \n oslo trykk (1) \n trondheim trykk (2) \n bergen trykk (3)")
    sporsmaal= ("hva er hovedstaden i Norge ?")
    
    hovedstad_i_norge = Capital(sporsmaal, hovedstad_liste, 1)
    
    print(hovedstad_i_norge)
    
    hovedstad_i_norge.sjekk_svar()

########
    
    number_liste = ("1 trykk (0) \n 2 trykk (1) \n 3 trykk (2) \n 4 trykk (3)")
    sporsmaal = ("hva er 1 + 2")
    
    number = Capital(sporsmaal, number_liste, 2)
    
    print(number)
    
    number.sjekk_svar()
    
   
    