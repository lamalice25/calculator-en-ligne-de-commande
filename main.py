# Importations de packets requis
import time 

# définir un variable qui est vrai 
running = True

enter  = input('Enter si vous voulais - , + , * : ')

while running:
    
    
    if '*' in enter:
        y1_multiplier = int(input('Entrer un chiffre le premier chiffre a multiplier : '))
        y2_multiplier = int(input('Enter le deuxième chiffre a multiplier : '))

        x_multiplier = y1_multiplier*y2_multiplier

        print("le resultat est : ", x_multiplier)

    
    elif '+' in enter:
        y1_aditionner = int(input("Enter le premier chiffre a aditionner : "))
        y2_aditionner = int(input("Enter le deuxième chiffre a aditionner : "))


        x_aditionner = y1_aditionner+y2_aditionner

        print("le resultat est : ", x_aditionner)

    elif '-' in enter:
        y1_soustraire = int(input("Entrer le premier chiffre a soustraire : "))
        y2_soustraire = int(input("Entrer le deuxième chiffre a soustraire : "))

        x_soustraire = y1_soustraire-y2_soustraire

        print("le resultat est : ", x_soustraire)
    
 


    elif 'cls' in enter:
        running = False
