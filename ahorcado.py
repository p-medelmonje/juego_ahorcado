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


while True:

    palabra = obtenerPalabra(palabras)

    pal_lista = []

    letras_por_adivinar = set(palabra)

    aciertos = []

    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    intentos = len(palabra) * 2


    # Comienzo del juego. Se selecciona una palabra aleatoria

    print("BIENVENIDO(A) AL JUEGO DEL AHORCADO")
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
                
                print("\nAcierto\n")
                letras_por_adivinar.remove(letra)
                aciertos.append(letra)
                intentos -= 1
                print(f"Te queda(n) {intentos} intento(s)")
                
            else:
                print("\nYa La letra ingresada ya está entre las acertadas. Intenta con otra")
                   
        else:
            print("\nFallaste\n")
            intentos -= 1
            print(f"Te queda(n) {intentos} intento(s)\n")



    if len(letras_por_adivinar) == 0:
        print(f"\nHas ganado. Acertaste todas las letras. La palabra es {palabra}")
        
    elif intentos == 0:
        print(f"\nHas perdido. La palabra era {palabra}. Más suerte para la próxima")
        
    continuar = input("\n¿Volver a jugar? ('s' para sí y cualquier otra opción para salir): ").upper()
    
    if continuar == "S":
        print("\nVolviendo a empezar...\n")
        
    else:
        print("\nHas elegido salir")
        exit()
        break
