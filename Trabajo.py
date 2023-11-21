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
print("Bienvenido! En este juego deberás adivinar una palagra generada al azar, tienes 5 intentos en los cuales puedes ir diciendo letras que creas que pueden estar en la palabra, si no aciertas la palabra en los 5 intentos habras perdido. Suerte!")


import random

class JuegoAdivinanza:
    def __init__(self):
        # Lista de palabras para el juego
        self.palabras = ["Tembloroso", "Engranaje", "Independencia", "Colarse", "Corto", "Gritar", "Multimillonario", "Sonic", "Disculparse", "Prueba"]
        # Número de intentos disponibles
        self.intentos = 5
        # Palabra seleccionada al azar para el juego
        self.palabra_generada = random.choice(self.palabras)
        # Conjunto para almacenar las letras adivinadas, evitando duplicados
        self.letras_adivinadas = set()

    def mostrar_palabra_oculta(self):
        # Construir la representación de la palabra oculta con letras adivinadas y guiones bajos
        palabra_oculta = ""
        for letra in self.palabra_generada:
            if letra in self.letras_adivinadas:
                palabra_oculta += letra
            else:
                palabra_oculta += "_"
        return palabra_oculta

    def jugar(self):
        # Bucle principal del juego
        while self.intentos > 0:
            # Mostrar la palabra oculta y los intentos restantes, y obtener la entrada del jugador
            letra = input(f"Palabra: {self.mostrar_palabra_oculta()} - Intentos restantes: {self.intentos}. Elige una letra o intenta adivinar la palabra: ")

            if letra in self.letras_adivinadas:
                # La letra ya ha sido elegida
                print("Ya has elegido esa letra. Intenta con otra.")
                continue

            if len(letra) == 1 and letra.isalpha():
                # El jugador eligió una letra
                self.letras_adivinadas.add(letra)
                if letra in self.palabra_generada:
                    print("¡Letra correcta!")
                else:
                    print(f"Letra incorrecta. Te quedan {self.intentos - 1} intentos.")
                    self.intentos -= 1
            elif len(letra) == len(self.palabra_generada) and letra.isalpha():
                # El jugador intenta adivinar la palabra completa
                if letra == self.palabra_generada:
                    print(f"¡Enhorabuena! Has adivinado la palabra: {self.palabra_generada}")
                    break
                else:
                    print("Palabra incorrecta. ¡Inténtalo de nuevo!")
                    self.intentos -= 1
            else:
                # Entrada no válida
                print("Entrada no válida. Por favor, elige una letra o intenta adivinar la palabra.")

        # Verificar si el jugador se quedó sin intentos
        if self.intentos == 0:
            print(f"No te quedan intentos. La palabra correcta era: {self.palabra_generada}")

# Crear un objeto del juego
juego = JuegoAdivinanza()

# Iniciar el juego
juego.jugar()

#hacer menú de si quieres volver a jugar