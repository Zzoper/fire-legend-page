import random

# Inventario del jugador (usaremos un conjunto para evitar duplicados)
inventario = set()

def obtener_nombre():
    nombre = input("Por favor, ingresa un nombre para tu personaje: ")
    return nombre

def inicio():
    nombre_personaje = obtener_nombre()
    print(f"{nombre_personaje}, despiertas en una celda oscura en una prisión espacial. Tu objetivo es escapar.")
    print("Tienes dos puertas frente a ti, una a la izquierda y otra a la derecha.")

    decision = input("¿Qué puerta eliges? (izquierda/derecha): ").lower()

    if decision == "izquierda":
        puerta_izquierda()
    elif decision == "derecha":
        puerta_derecha()
    else:
        print("No comprendo tu elección. Por favor, elige izquierda o derecha.")
        inicio()

def puerta_izquierda():
    print("Abres la puerta de la izquierda y encuentras una sala de control abandonada.")
    print("Ves un panel de control con varios botones y una computadora.")
    print("¿Qué haces?")
    
    decision = input("1. Intentar encender la computadora\n2. Presionar botones al azar\n3. Salir de la sala\nElije 1, 2 o 3: ")

    if decision == "1":
        print("Logras encender la computadora y descubres información crucial sobre la prisión.")
        inventario.add("Código de acceso")
        print("Has obtenido un código de acceso. Lo guardas en tu inventario.")
        puerta_derecha()
    elif decision == "2":
        print("Presionas botones al azar y activas una alarma. Los guardias te atrapan.")
        final_triste()
    elif decision == "3":
        print("Sales de la sala y te encuentras con una patrulla de guardias que te detiene.")
        final_triste()
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
        puerta_izquierda()

def puerta_derecha():
    print("Abres la puerta de la derecha y te encuentras en un pasillo oscuro.")
    print("Ves una escalera que lleva hacia arriba y una puerta al final del pasillo.")
    print("¿Qué haces?")

    decision = input("1. Subir la escalera\n2. Abrir la puerta al final del pasillo\n3. Volver a la celda\nElige 1, 2 o 3: ")

    if decision == "1":
        print("Subes la escalera y encuentras una nave de escape. ¡Escapas con éxito!")
        final_feliz()
    elif decision == "2":
        sala_secreta()
    elif decision == "3":
        print("Decides volver a tu celda y esperar. Los guardias te descubren y te atrapan.")
        final_triste()
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
        puerta_derecha()

def sala_secreta():
    print("Abres la puerta al final del pasillo y entras en una sala secreta.")
    print("Ves un pedestal con un objeto brillante encima y una puerta con una cerradura electrónica.")
    print("¿Qué haces?")

    decision = input("1. Tomar el objeto brillante\n2. Examinar la cerradura electrónica\n3. Volver al pasillo\nElige 1, 2 o 3: ")

    if decision == "1":
        if "Llave electrónica" not in inventario:
            inventario.add("Llave electrónica")
            print("Has obtenido una llave electrónica. Lo guardas en tu inventario.")
        else:
            print("Ya tienes una llave electrónica. No necesitas otra.")
        sala_secreta()
    elif decision == "2":
        if "Llave electrónica" in inventario:
            print("Usas la llave electrónica para desbloquear la puerta y encuentras un tesoro.")
            if "Tesoro" not in inventario:
                inventario.add("Tesoro")
                print("Has encontrado un tesoro. Lo guardas en tu inventario.")
            else:
                print("Ya has recogido el tesoro anteriormente.")
        else:
            print("La cerradura electrónica está bloqueada. Necesitas una llave electrónica para abrirla.")
        sala_secreta()
    elif decision == "3":
        print("Decides volver al pasillo.")
        puerta_derecha()
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
        sala_secreta()

def final_feliz():
    print("¡Felicidades! Has escapado de la prisión espacial y ganaste el juego.")
    print("Tu inventario:")
    for item in inventario:
        print(f"- {item}")

def final_triste():
    print("Tu aventura llega a un trágico final. Te han atrapado y no lograste escapar.")

# Salas y finales trágicos adicionales
def sala_tragica_1():
    print("Abres una puerta oculta y entras en una sala llena de trampas mortales.")
    print("Te mueves con cautela, pero caes en una trampa y no puedes escapar.")
    final_triste()

def sala_tragica_2():
    print("Abres otra puerta oculta y te encuentras en una habitación llena de gases tóxicos.")
    print("No puedes encontrar una salida y caes víctima de los gases.")
    final_triste()

# Inicia el juego
inicio()
