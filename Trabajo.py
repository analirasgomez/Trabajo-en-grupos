#El programa que vamos a crees va a consistir en un juego para adivinar la palabra correcta.
print("")


import random

palabra = ["Tembloroso", "Engranaje", "Independencia", "Colarse", "Corto", "Gritar", "Multimillonario", "Sonic", "Disculparse", "Prueba"]
palabra_generada = random.choice (palabra)

letra = input(f"La palabra genrada tiene {len(palabra_generada)} letras, elige una letra")

intentos = 5 

if letra in palabra_generada:
    letra_correcta = input("Esa letra está en la palabra, elige otra otra")
else:
    letra_incorrecta = input(f"Esa letra no está en la palabra, te quedan {intentos-1}")

if intentos == 0:
    print(f"No te quedan intentos! La palabra elegida era {palabra_generada}")
    