import random
import sqlite3 as sql
import os

from palabras import palabras


def obtenerPalabra(palabras):
    palabra = random.choice(palabras)
    return palabra

def crearTabla():
    conn = sql.connect("puntuaciones.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE if not exists puntajes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre TEXT NOT NULL,
            Largo_palabra INTEGER NOT NULL,
            Intentos_restantes INTEGER NOT NULL,
            Calificacion TEXT NOT NULL)
        """
        )
    print("Base de datos y tabla creadas exitosamente\n")
    conn.commit()
    conn.close()
    

def conectarBD():
    if not os.path.isfile("puntuaciones.db"):
        print("Creando base de datos para las puntuaciones...")
        conn = sql.connect("puntuaciones.db")
        crearTabla()
#         conn.commit()
#         conn.close()        

def guardarPuntaje(nombre):
    conn = sql.connect("puntuaciones.db")
    cursor = conn.cursor()
    instruccion =f"INSERT INTO puntajes VALUES(null,'{nombre}',{len(palabra)},{intentos},'{calificacion}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    
def mostrarPuntajes():
    conn = sql.connect("puntuaciones.db")
    cursor = conn.cursor()
    cursor.execute("""SELECT Nombre, Largo_palabra, Intentos_restantes, Calificacion
    FROM puntajes ORDER BY id DESC""")
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    while len(datos) > 10:
        datos.pop(-1)
    else:    
        print("\nPUNTAJES")
        print("Nombre - Largo palabra - Int. restantes - Calificación\n")
        for l in datos:
            print(l)            

# Comienza la ejecución del programa

conectarBD()

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
tener una o más letras varias veces dentro de la palabra, o también puede
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
                        calificacion = "Experto(a)"
                        print(f"Calificación: {calificacion}")
                        
                    # Guardar información en base de datos
                    
                    print("\nEscribe tu nombre para guardar la puntuación")
                    nombre = input("> ")
                    guardarPuntaje(nombre)
                    mostrarPuntajes()
                                            
                    break
                
            else:
                print("\nYa La letra ingresada ya está entre los aciertos. Intenta con otra")
                   
        else:
            print("\nFALLASTE")
            intentos -= 1
            
        if intentos < len(palabra) * 0.5 and intentos > len(palabra) * 0.25:
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
        