# Litotājs ievada tekstu un aprēķiniet burtu un vārdu skaitu tajā.

# Lietotāja ievadītais teksts
teksts=input("Ievadīt tekstu: ") #Saule spīd



# Aprēķināt burtu skaitu ... kā programa zinās ka tas ir burts? aka%
# isalpha()
burtuskaits=0
for burts in teksts:
  if burts.isalpha():
    burtuskaits==1 # burtuskaits=burtuskaits+1
# Sadalīt tekstu pa vārdiem
Vārdi=teksts.split() # atdalītājs splt(",")

# Aprēķināt vārdu skaitu

vārduskaits=len(vārdi)
# Izvadīt rezultātu
print(f"Burtu skaits ir {burtuskaits}")
print(f"")