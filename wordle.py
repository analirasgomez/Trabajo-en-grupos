# Explicamos las instrucciones del juego.
print ("¡Empezamos!")
print ("REGLAS:")
print ("La palabra se debe escribir entera en mayúsculas.")
print ("- Si la letra aparece en rojo, esa letra no esta en la palabra")
print ("- Si la letra aparece en amarillo, esa letra está en la palabra pero no en esa posición.")
print ("- Si la letra aparece en verde, esa letra esta bien colocada y es la correcta.")
print ("dele al intro para empezar")


import random

class JuegoAhorcado:
    def __init__(self):
        self.palabra = self.eleccion_palabra()
        self.ganar = False
        self.tablero = [[" _ " for _ in range(len(self.palabra))] for _ in range(6)]
        self.colores = {
            "verde": "\033[92m",
            "amarillo": "\033[93m",
            "rojo": "\033[91m",
            "ENDC": "\033[0m",
        }

    def eleccion_palabra(self):
        palabras_generadas = ["ACCESO", "POQUER", "PARQUE", "IRAQUI", "ABEDUL", "CACTUS", "AHUMAR", "SONICO", "BUFALO", "CESPED"]
        return random.choice(palabras_generadas)

    def color_letra(self, letra, color):
        return self.colores[color] + letra + self.colores["ENDC"]

    def jugar(self):
        contador_bucle = 0
        while (not self.ganar) and (contador_bucle < 6):
            texto = input("")
            while len(texto) != len(self.palabra):
                print(f"La palabra debe tener {len(self.palabra)} letras")
                texto = input("")

            # Lógica para ganar
            if self.palabra == texto:
                self.tablero[contador_bucle] = [l for l in texto]
                self.ganar = True
                break
            else:
                test_line = []
                for j in range(len(self.palabra)):
                    if texto[j] == self.palabra[j]:
                        test_line.append(self.color_letra(texto[j], "verde"))
                    elif texto[j] in self.palabra:
                        test_line.append(self.color_letra(texto[j], "amarillo"))
                    else:
                        test_line.append(self.color_letra(texto[j], "rojo"))
                self.tablero[contador_bucle] = test_line

            # Dibujar el tablero
            for i in range(6):
                print(" ".join(self.tablero[i]))

            contador_bucle += 1

        if self.ganar:
            print("¡Has ganado!")
        else:
            print("¡Perdiste!")

# Crear un objeto de la clase y comenzar el juego
juego = JuegoAhorcado()


juego.jugar()