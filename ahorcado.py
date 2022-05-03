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
    
    print("===================================")
    print("BIENVENIDO(A) AL JUEGO DEL AHORCADO")
    print("===================================")
    
    print("""\nNOTA: El juego puede ser muy fácil; tan fácil que una palabra puede
tener una o más letras varias veces dentro de la palabra, pero puede
ser tan despiadadamente difícil que simplemente no vas a poder adivinar.""")
    
    while intentos > 0: #and len(letras_por_adivinar) > 0:
        
        pal_lista = [letra if letra in aciertos else '_' for letra in palabra]
        print("\n", pal_lista)
        print(f"\n{intentos} Intento(s) restante(s)")

        letra = input("\nIngresa una letra: ").upper()

        while not letra in abecedario or len(letra) > 1 or len(letra) == 0:
            print("\nIngreso inválido")
            letra = input("\nIngresa una letra: ").upper()
            
        if letra in palabra:
            
            if letra not in aciertos:
                
                print("\nACERTASTE, al fin...")
                letras_por_adivinar.remove(letra)
                aciertos.append(letra)
                intentos -= 1
                                
                if len(letras_por_adivinar) == 0:
                    print(f"\nHas ganado. Acertaste en todas las letras. La palabra es {palabra}\n")
                    print(f"""Resultado:
Largo de la palabra: {len(palabra)}
Intentos restantes: {intentos}""")
                    
                    # Calificación al jugador
                    
                    if intentos <= len(palabra) * 0.3:
                        calificacion = "El horror"
                        
                        print(f"Calificación: {calificacion}")
                        
                    elif intentos > len(palabra) * 0.3 and intentos <= len(palabra) * 0.6:
                        calificacion = "Decente"
                        print(f"Calificación: {calificacion}")
                        
                    else:
                        calificacion = "Legendario(a)"
                        print(f"Calificación: {calificacion}")
                        
                    break
                
            else:
                print("\nYa La letra ingresada ya está entre las acertadas. Intenta con otra")
                   
        else:
            print("\nFALLASTE")
            intentos -= 1
            
        if intentos < len(palabra) * 0.5:
            print("\nApúrate, que se te acaban los intentos... tu abuela habría ganado media hora antes")
                       
        if intentos == 0:
            print(f"\nPERDISTE. La palabra era {palabra}. Así de fácil era.\nCalificación: -10")
            break
        
    continuar = input("\n¿Volver a jugar? ('s' para sí y cualquier otra opción para salir): ").upper()
    
    if continuar == "S":
        print("\nVolviendo a empezar...\n")
        
    else:
        print("\nHas elegido salir")
        exit()
        