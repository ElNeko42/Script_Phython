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

def torneo(luchadores):
    while len(luchadores) > 1:
        ganadores = []
        random.shuffle(luchadores)  # Mezclar los luchadores aleatoriamente
        for i in range(0, len(luchadores), 2):
            luchador1 = luchadores[i]
            luchador2 = luchadores[i+1]
            ganador = batalla(luchador1, luchador2)
            ganadores.append(ganador)
        luchadores = ganadores
    imprimir_lento(f"\nEl ganador del torneo es {luchadores[0].nombre}!")

# Ejemplo de creación de luchadores
luchadores = [
    Luchador("Goku", 80, 90, 70),
    Luchador("Vegeta", 75, 85, 80),
    Luchador("Piccolo", 70, 75, 85),
    Luchador("Gohan", 85, 80, 75)
]

# Iniciar el torneo
torneo(luchadores)
