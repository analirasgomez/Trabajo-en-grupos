#Chose one topic and build a program with your group
#PRESENTA TION TEM PLA TE
#• In a new repo
#• There must be commitsfromall teammembers
#• All teammembersmust upload the repository toMoodle
# • Minimumrequirements:
#• Use at least one class and several instantiated objects of each class.
#• Use functions wisely.
#• Avoid repeating code.
#• Use at least 1 while orforloop.
#• Use at least one library (it can be math, matpotlib orothers)





#El programa que vamos a crees va a consistir en un juego para adivinar la palabra correcta.
print("")


import random

palabra = ["Tembloroso", "Engranaje", "Independencia", "Colarse", "Corto", "Gritar", "Multimillonario", "Sonic", "Disculparse", "Prueba"]
palabra_generada = random.choice (palabra)

letra = input(f"La palabra genrada tiene {len(palabra_generada)} letras, elige una letra o intenta adivinar la palabra: ")

intentos = 5 

if letra in palabra_generada:
    letra_correcta = input("Esa letra está en la palabra, elige otra otra")
else:
    letra_incorrecta = input(f"Esa letra no está en la palabra, te quedan {intentos-1}")


if letra_correcta or letra_incorrecta in palabra_generada:
    letra_correcta = input("Esa letra está en la palabra, elige otra otra")
else:
    letra_incorrecta = input(f"Esa letra no está en la palabra, te quedan {intentos-1}")


if letra or letra_correcta or letra_incorrecta == palabra_generada:
    print(f"Enhorabuena! has acertado la palabra {palabra_generada}")

if intentos == 0:
    print(f"No te quedan intentos! La palabra elegida era {palabra_generada}")



#hacer menú de si quieres volver a jugar