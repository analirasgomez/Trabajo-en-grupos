# Explicamos las instrucciones del juego.
print ("¡Empezamos!")
print ("REGLAS:")
print ("La palabra se debe escribir entera en mayúsculas.")
print ("- Si la letra aparece en rojo, esa letra no esta en la palabra")
print ("- Si la letra aparece en amarillo, esa letra está en la palabra pero no en esa posición.")
print ("- Si la letra aparece en verde, esa letra esta bien colocada y es la correcta.")
print ("dele al intro para empezar")

palabra = "TROMPA" #Hay que hacer un diccionario de palabras en mayuscula de 6 letras e importar una ramdon de esa lista cada vez que se juegue.
# Definimos los colores de las letras
colores = {
    "verde" : "\033[92m",
    "amarillo" : "\033[93m",
    "rojo" : "\033[91m",
    "ENDC" : "\033[0m",
}

def color_letra (letra, color):
    return colores[color] + letra + colores["ENDC"]
    


# Condicion de bucle para ganar 
ganar = False
tablero = []
for i in range (6):                                 # Dibujar el tablero de juego donde se escribira la palabra
    tablero.append ([" _ " for l in range(6)])        # Creamos el tablero como una matriz de 6x6 con 6 intentos de palabra (las filas (i)) y 6 letras la palabra (las columnas (l))
    continue

contador_bucle = 0

while (not ganar) and (contador_bucle < 6):
    texto = input ("")
    while len(texto) != len(palabra):
        print (f"La palabra debe tener {len(palabra)} letras")
        texto = input ("")
        continue
    

    #logica de ganar
    if palabra == texto:
        tablero [contador_bucle] = [l for l in texto]
        ganar = True
        break

    #letra en la palabra aplicando los colores.
    else:
        test_line = []
        for j in range (len(palabra)):
            if texto [j] == palabra [j]:
                test_line.append (color_letra(texto[j], "verde"))
            elif texto [j] in palabra:
                test_line.append (color_letra(texto[j], "amarillo"))
            else:
                test_line.append (color_letra (texto[j], "rojo"))

        tablero[contador_bucle] = test_line

    # Draw                                            # Separamos las filas dandole forma de matriz y juntamos las letras de cada fila.
    for i in range(6):
        print (" ".join(tablero[i]))
    
    contador_bucle += 1
    
    
if ganar == True:
    print ("¡Has ganado!")
else: 
    print ("ooooo, perdiste")