
import random
# Definición de la clase Equipo
class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosGanados = 0
        self.partidosPerdidos = 0
        self.setGanados = 0

def RegistraSet(equipo1, equipo2, Ganador):
    # Registra el set ganado por el equipo ganador
    if Ganador == 1:
        equipo1.setGanados += 1
        if equipo1.setGanados == 3:
            equipo1.partidosGanados += 1
            equipo2.partidosPerdidos += 1
            equipo1.setGanados = 0
            equipo2.setGanados = 0
    elif Ganador == 2:
        equipo2.setGanados += 1
        if equipo2.setGanados == 3:
            equipo2.partidosGanados += 1
            equipo1.partidosPerdidos += 1
            equipo1.setGanados = 0
            equipo2.setGanados = 0

def Puntos():
    return random.randint(10, 28)

def PuntosExtras():
    return random.randint(0, 6)

def JugarPartido(equipo1, equipo2):
    while True:
        puntos1 = Puntos()
        puntos2 = Puntos()
        
        if puntos1 <= 25 or puntos2 <= 25:
            if puntos1 >= 25 and puntos1 >= puntos2:
                RegistraSet(equipo1, equipo2, 1)
                print(f"{equipo1.nombre} gana el set con {puntos1} puntos contra {puntos2} del equipo {equipo2.nombre}")
                break
            elif puntos2 >= 25 and puntos2 > puntos1:
                RegistraSet(equipo1, equipo2, 2)
                print(f"{equipo2.nombre} gana el set con {puntos2} puntos contra {puntos1} del equipo {equipo1.nombre}")
                break
        
        else:
            puntos1 += PuntosExtras()
            puntos2 += PuntosExtras()
            print("Ningún equipo superó 25 puntos, sumando puntos extras:")
            print(f"Quedó {equipo1.nombre} {puntos1} contra {equipo2.nombre} {puntos2}")

def ResultadoTorneo(equipo1, equipo2):
    print("\nResultados totales del Torneo:")
    print(f"{equipo1.nombre}: Partidos Ganados: {equipo1.partidosGanados}, Partidos Perdidos: {equipo1.partidosPerdidos}")
    print(f"{equipo2.nombre}: Partidos Ganados: {equipo2.partidosGanados}, Partidos Perdidos: {equipo2.partidosPerdidos}")

    if equipo1.partidosGanados > equipo2.partidosGanados:
        print(f"\nFelicidades {equipo1.nombre} por ganar el torneo!")
    elif equipo2.partidosGanados > equipo1.partidosGanados:
        print(f"\nFelicidades {equipo2.nombre} por ganar el torneo!")
    else:
        print("\nEl torneo terminó en empate.")

if __name__ == "__main__":
    nombre1 = input("Nombre del Equipo 1: ")
    nombre2 = input("Nombre del Equipo 2: ")

    equipo1 = Equipo(nombre1)
    equipo2 = Equipo(nombre2)

    cantidadPartido = int(input("¿Cuántos partidos se jugará? "))

    for _ in range(cantidadPartido):
        JugarPartido(equipo1, equipo2)

    ResultadoTorneo(equipo1,equipo2)
