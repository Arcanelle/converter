#programme de conversion de miles/h en km/h
#Pour rappel, 1 mile = 1.609Km
#Essayez d'arrondir au centième près

E = input('Votre vitesse à convertir se trouve dans quelle unité: km/h ou mph ? ')

if E == str('mph'):
    mph = float(input('Veuillez saisir une vitesse en mph: '))
    coefficient_de_conversion = 1.609
    conversion = mph * coefficient_de_conversion
    #print(conversion), pour rendre ça plus joli:
    print(f"Voici le résultat: {mph}mph = {round(conversion, 2)}km/h")

elif E == str('km/h'):
    kmh = float(input('Veuillez entrer une vitesse en km/h: '))
    kmh_to_mph = 1.609
    speed_mph = kmh / kmh_to_mph
    print(f"{kmh}km/h = {round(speed_mph, 2)}mph")

else:
    print('Vous n\'avez pas saisi une unité correcte')    


