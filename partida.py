from jugadores import JugadorHumano, JugadorMaquina
from tablero import Tablero


class Partida:

    def __init__(self, jugador1, jugador2):
        self.turno = 0
        self.jugadores = [jugador1, jugador2]
        for jugador in self.jugadores:
            jugador.colocar_barcos()
            if isinstance(jugador, JugadorHumano):
                print(jugador.tablero)

    def jugar(self):
        # El juego se desarrolla en un bucle que se repite mientras haya barcos vivos en ambos jugadores
        while all(len(j.barcos_vivos) > 0 for j in self.jugadores):
            jugador_actual = self.jugadores[self.turno]
            contrincante = self.jugadores[1 - self.turno]

            print(f"Turno de {jugador_actual.nombre}")

            while True:  # Bucle para gestionar el disparo, reintentando en caso de excepción
                try:
                    fila, columna = jugador_actual.disparar()
                    if contrincante.recibir_disparo(fila, columna):
                        print('¡Tocado!')
                    else:
                        print('Agua')
                except Exception as e:
                    print(e)
                else:
                    break # Si llegamos aquí, es que el disparo ha sido válido: salimos del bucle

            
            if len(contrincante.barcos_vivos) == 0:
                print(f"¡{jugador_actual.nombre} ha ganado!")
            else:
                print(f"¡{contrincante.nombre} ha ganado!")

            
            # Después de gestionar el disparo, mostraremos el tablero:
            # radar para la máquina, tablero completo para el humano
            if isinstance(contrincante, JugadorMaquina):
                print(contrincante.tablero.radar)
            if isinstance(contrincante, JugadorHumano):
                print(contrincante.tablero)

            self.turno = 1 - self.turno # Cambio de turno
        


if __name__ == '__main__':
    nombre = input('¿Cómo te llamas? ')
    p = Partida(
        JugadorHumano(nombre, Tablero()), 
        JugadorMaquina('HAL', Tablero())
    )
    p.jugar()
