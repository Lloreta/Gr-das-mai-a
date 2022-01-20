#komantārs
import math

def gridas_izmaksa(cena, linoleja_platums, telpas_platums, telpas_garums):
    telpas_izmers = math.ceil(telpas_garums) * math.ceil(telpas_platums)
    ruli = math.ceil(telpas_platums) / math.ceil(linoleja_platums)
    izmaksa = ruli*linoleja_platums*telpas_garums*cena

    
    return izmaksa
  

cena1 = float(input("Ievadiet linoleja cenu: "))
linoleja_platums1 = float(input("Ievadiet linoleja platumu: "))
platums1 = float(input("Ievadi telpas platumu: "))
garums1 = float(input("Ievadiet telpas garumu: "))


print("izklājot garumā:")
print(gridas_izmaksa(cena1, linoleja_platums1, platums1, garums1))
print("izklājot platumā:")
print(gridas_izmaksa(cena1, linoleja_platums1, garums1, platums1))
