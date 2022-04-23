import random


# funciones para extraer palabras aleatorias

def elige5():
    print("\nSeleccionada la opción Fácil")
    print("\nDispondrás de 10 intentos")
    print("\n _ _ _ _ _")
    palabra = random.choice(palabras5l)
    intentos = 10
    return palabra, intentos

def elige6():
    palabra = random.choice(palabras6l)
    intentos = 11
    print("Seleccionada la opción Intermedia")
    print("Dispondrás de 11 intentos")
    print("\n _ _ _ _ _ _")
    return palabra, intentos

def elige7():
    palabra = random.choice(palabras7l)
    intentos = 12
    print("Seleccionada la opción Difícil")
    print("Dispondrás de 12 intentos")
    print("\n _ _ _ _ _ _ _")
    return palabra, intentos

# función opción inválida

# def opcion_correcta(dificultad):
#     if dificultad == 1:
        
        

# listas con palabras

palabras5l = ["VAGON", "CANCER", "VIRGO", "ABEJA", "VERDE", "HIELO", "LIBRA",
              "GASTO", "APOLO", "APODO", "JOVEN", "AMADO", "AMADA", "MASAS",
              "MAZAS", "GATOS", "PERRO", "ASILO", "ARETE", "ATADO", "ATAUD",
              "ASPID", "ARBOL", "AROMA", "AREPA", "ARGAN", "ARIES", "LLAVE",
              "NINFA", "CHOLO", "BOTES", "ABONO", "MANGO", "ACIDO", "AGRIO",
              "AGUDO", "AGUAS", "MARES", "BAÑOS", "BEBES", "BESOS", "BODAS",
              "ALMAS", "ALOJO", "BRUMA", "CASAS", "CAZAS", "BOMBA", "BRUTO",
              "CACAO", "CARGO", "CAPAZ", "CARGA", "AVARO", "ALANO", "AZOTE",
              "ATAJO", "CREMA", "CASCO", "CASOS", "CASPA", "CAUSA", "CUEVA",
              "CAIDA", "CAÑAS", "PESCA", "CLAVO", "COGER", "CLARA", "CLARO",
              "ESPIA", "FALLA", "FORMA", "FALTA", "FRITO", "FRITA", "INDIO",
              "INDIA", "HUNOS", "GODOS", "LADRON", "LAURA", "LARGO", "LARGA",
              "PASTA", "PASTO", "PISTA", "LOCHA", "PARGO", "PERCA", "PISCO",
              "PULSO", "RIFLE", "CASTA", "LUCHA", "MALTA", "MONTO", "MOSCU",
              "NEPAL", "MENTA", "MAREA", "MINAS", "OGROS", "SHREK", "PATAS",
              "TAURO", "PECES", "PITON", "PYTHON", "DULCE", "SEÑOR", "CERDO",
              "COLON", "TURCO", "TURCA", "PERSA", "TOKIO", "CHINO", "CHINA",
              "BARCO", "BUQUE", "BUCLE", "CANTO", "POETA", "LINDO", "LINDA",
              "YEGUA", "BURRO", "BURRA", "LLAMA", "FUEGO", "NINFA"]
palabras5l.sort()

palabras6l = ["PISCIS", "CASTRO", "PERROS", "PISTAS", "ABADIA", "AHORRO",
              "VIBORA", "AGOBIO", "AMARGO", "DULCES", "SALADO", "PASTEL",
              "SEÑORA", "FLAUTA", "CERDOS", "PALOMA", "PICHON", "ZORZAL",
              "ANTENA", "ATENEA", "ATENAS", "ANTISA", "ARABIA", "GENOVA",
              "COSACO", "COSACA", "DRAGON", "HALCON", "AGUILA", "VIRGEN",
              "TOYOTA", "MADRID", "MONGOL", "CUMANO", "CUMANA", "POLACO",
              "POLACA", "VUELTA", "AMORIO", "AFINAR", "AFILAR", "ANIMAR",
              "LAZARO", "LESBOS", "TAMBOR", "CASTOR", "CANTOR", "ESPADA",
              "ESCUDO", "LLAMAR", "LLAMAS"]

palabras7l = ["GEMINIS", "ACUARIO", "ARBOLES", "JOVENES", "CULEBRA", "SEMILLA",
              "TORTOLA", "PALOMAS", "ARDILLA", "CHALECO", "ESPARTA", "ISFAHAN",
              "COLOMBO", "COLOMBA", "BOLIVIA", "TARTARO", "TARTARA", "VIKINGO",
              "VIKINGA", "GENOVES", "CAVERNA", "POLONIA", "MASHHAD", "TEHERAN",
              "FRANCIA", "FRANCOS", "FRANCAS", "VENTANA", "CANCION", "CANTORA",
              "POETISA", "GORRION", "VUELTAS", "DALMATA", "CABALLO", "COBAYA",
              "GLACIAR", ]


lista5l = ["_","_","_","_","_"]

lista6l = ["_","_","_","_","_","_"]

lista7l = ["_","_","_","_","_","_","_"]

palabra = None

intentos = 0

# Comienza el juego

print("Elige la dificultad: \n1- Fácil \n2- Intermedia \n3- Difícil")
dificultad = int(input("> "))

while not dificultad in [1, 2, 3]:
    print("Opción incorrecta")
    print("\nElige la dificultad: \n1- Fácil \n2- Intermedia \n3- Difícil")
    dificultad = int(input("> "))
    
if dificultad == 1:
    elige5()
    print(palabra)
    print(intentos)
    





