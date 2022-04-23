"""
Juego del ahorcado

Lo que debería hacer el programa:

- Seleccionar una palabra al azar de una lista y establecer la cantidad
de intentos según el largo de la palabra.

- El jugador ingresa una letra para tratar de acertar la palabra. A medida que
vaya acertando, el programa muestra las letras acertadas y su posición en la
palabra.

- Si el jugador falla o acierta, se resta al contador de intentos.

- El juego termina cuando el jugador ha acertado a la palabra o haya gastado
todos sus intentos.
"""

import random

from palabras import palabras


def obtenerPalabra(palabras):
    palabra = random.choice(palabras)
    return palabra


palabra = obtenerPalabra(palabras)

pal_lista = []

letras_por_adivinar = set(palabra)

aciertos = []

abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

intentos = len(palabra) + 4


# Comienzo del juego. Se selecciona una palabra aleatoria

print("Bienvenido(a) al juego del ahorcado")
print(f"\nLa palabra tiene {len(palabra)} letras y tienes {intentos} intentos")


while intentos > 0 and len(letras_por_adivinar) > 0:
    
    pal_lista = [letra if letra in aciertos else '_' for letra in palabra]
    print("\n", pal_lista)

    letra = input("\nIngresa una letra: ").upper()

    while not letra in abecedario:
        print("Ingreso inválido")
        letra = input("Ingresa una letra: ").upper()
        
    if letra in palabra:
        
        if letra not in aciertos:
            
            print("Acierto\n")
            letras_por_adivinar.remove(letra)
            aciertos.append(letra)
            print(letras_por_adivinar)
            intentos -= 1
            print(f"Te queda(n) {intentos} intento(s)")
            
        else:
            print("\nYa habías usado esa letra. Intenta con otra")
               
    else:
        print("Fallaste\n")
        intentos -= 1
        print(f"Te queda(n) {intentos} intento(s)")



if len(letras_por_adivinar) == 0:
    print("Has ganado. Acertaste todas las letras")
    
elif intentos == 0:
    print("Has perdido. Más suerte para la próxima")
