import random
import time

# Función para imprimir texto con retraso
def imprimir_lento(texto, delay=0.05):
    for char in texto:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Nueva línea al final

# Función para mostrar barras de salud en la terminal
def mostrar_barra_salud(luchador, longitud=20):
    barra_completa = int((luchador.salud / 100) * longitud)
    barra = '█' * barra_completa + '-' * (longitud - barra_completa)
    print(f"{luchador.nombre} [ {barra} ] {luchador.salud}/100")

class Luchador:
    def __init__(self, nombre, velocidad, ataque, defensa):
        self.nombre = nombre
        self.velocidad = velocidad
        self.ataque = ataque
        self.defensa = defensa
        self.salud = 100

    def __str__(self):
        return f"Luchador: {self.nombre}, Salud: {self.salud}, Velocidad: {self.velocidad}, Ataque: {self.ataque}, Defensa: {self.defensa}"

def batalla(luchador1, luchador2):
    imprimir_lento(f"\nBatalla entre {luchador1.nombre} y {luchador2.nombre}!")
    
    while luchador1.salud > 0 and luchador2.salud > 0:
        # Mostrar las barras de salud antes de cada turno
        mostrar_barra_salud(luchador1)
        mostrar_barra_salud(luchador2)
        
        if luchador1.velocidad >= luchador2.velocidad:
            atacar(luchador1, luchador2)
            if luchador2.salud > 0:
                atacar(luchador2, luchador1)
        else:
            atacar(luchador2, luchador1)
            if luchador1.salud > 0:
                atacar(luchador1, luchador2)

    # Mostrar las barras de salud finales
    mostrar_barra_salud(luchador1)
    mostrar_barra_salud(luchador2)

    if luchador1.salud > 0:
        imprimir_lento(f"{luchador1.nombre} gana la batalla!")
        return luchador1
    else:
        imprimir_lento(f"{luchador2.nombre} gana la batalla!")
        return luchador2

def atacar(atacante, defensor):
    imprimir_lento(f"{atacante.nombre} ataca a {defensor.nombre}")
    
    if random.random() <= 0.2:
        imprimir_lento(f"{defensor.nombre} esquivó el ataque!")
        return
    
    daño = max(0, atacante.ataque - defensor.defensa)
    
    if defensor.defensa > atacante.ataque:
        daño = atacante.ataque * 0.1
    
    defensor.salud -= daño
    defensor.salud = max(0, defensor.salud)
    
    imprimir_lento(f"{atacante.nombre} hace {daño} de daño. {defensor.nombre} tiene {defensor.salud} de salud restante.")

# Función para generar el cuadro del torneo aleatorio y guardarlo en una lista
def generar_cuadro(luchadores):
    random.shuffle(luchadores)  # Aleatorizamos el orden de los luchadores
    cuadro = []
    for i in range(0, len(luchadores), 2):
        if i + 1 < len(luchadores):
            cuadro.append((luchadores[i], luchadores[i + 1]))
        else:
            cuadro.append((luchadores[i], None))  # Luchador sin oponente
    return cuadro

# Función para mostrar el cuadro del torneo a partir de la lista generada
def mostrar_cuadro_torneo(cuadro, ronda_actual):
    imprimir_lento(f"\nCuadro de la ronda {ronda_actual}:")
    max_name_length = max(len(luchador.nombre) for par in cuadro for luchador in par if luchador)
    espacio = " " * 5

    # Mostrar los enfrentamientos
    for luchador1, luchador2 in cuadro:
        if luchador2:
            print(f"{luchador1.nombre.ljust(max_name_length)} {espacio} vs {espacio} {luchador2.nombre.ljust(max_name_length)}")
        else:
            print(f"{luchador1.nombre.ljust(max_name_length)} avanza automáticamente.")

# Función principal para gestionar el torneo
def torneo(luchadores):
    ronda_actual = 1
    while len(luchadores) > 1:
        cuadro = generar_cuadro(luchadores)  # Generar el cuadro de la ronda
        mostrar_cuadro_torneo(cuadro, ronda_actual)  # Mostrar el cuadro

        ganadores = []
        for luchador1, luchador2 in cuadro:
            if luchador2:  # Si hay dos luchadores, se realiza la batalla
                ganador = batalla(luchador1, luchador2)
                ganadores.append(ganador)
            else:  # Si no hay oponente, el luchador avanza automáticamente
                ganadores.append(luchador1)
                imprimir_lento(f"{luchador1.nombre} avanza automáticamente a la siguiente ronda.")
        
        luchadores = ganadores  # Actualizamos los luchadores para la siguiente ronda
        ronda_actual += 1

    imprimir_lento(f"\nEl ganador del torneo es {luchadores[0].nombre}!")

# Función para crear luchadores personalizados
def crear_luchador():
    nombre = input("Introduce el nombre del luchador: ")
    velocidad = int(input("Introduce la velocidad (0-100): "))
    ataque = int(input("Introduce el ataque (0-100): "))
    defensa = int(input("Introduce la defensa (0-100): "))
    return Luchador(nombre, velocidad, ataque, defensa)

# Menú de selección
def menu_principal():
    imprimir_lento("¡Bienvenido al Torneo Dragon Ball!")
    imprimir_lento("1. Usar luchadores predeterminados (Goku, Vegeta, Piccolo, Gohan)")
    imprimir_lento("2. Crear luchadores personalizados")
    opcion = input("Elige una opción (1 o 2): ")
    
    if opcion == "1":
        luchadores = [
            Luchador("Goku", 80, 90, 70),
            Luchador("Vegeta", 75, 85, 80),
            Luchador("Piccolo", 70, 75, 85),
            Luchador("Gohan", 85, 80, 75)
        ]
    elif opcion == "2":
        luchadores = []
        cantidad = int(input("¿Cuántos luchadores quieres crear? (mínimo 2): "))
        for _ in range(cantidad):
            luchador = crear_luchador()
            luchadores.append(luchador)
    else:
        imprimir_lento("Opción no válida. Saliendo del programa.")
        return
    
    imprimir_lento("¡Que comience el torneo!")
    torneo(luchadores)

# Iniciar el programa
menu_principal()
