# BMI = vaha v kg / vyska v m ** 2
 
jmeno = "Martin"
vaha = 80 # kg
vyska = 200 # cm

bmi = vaha / (vyska / 100) ** 2 

kategorie = ""

if bmi > 40:
    kategorie = 'těžká obezita'
elif bmi > 30:
    kategorie = 'obezita'
elif bmi > 25:
    kategorie = 'mírná nadváha'
elif bmi > 18.5:
    kategorie = 'zdravá váha'
else:
    kategorie = 'podvýživa'

print(f"{jmeno} tvé BMI je {bmi}, což spadá do kategorie {kategorie}.")
