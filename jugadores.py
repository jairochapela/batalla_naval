import random
from barcos import Barco, Portaaviones, Destructor, Submarino, Fragata, Patrullero
from tablero import BarcoMalColocadoError

class Jugador:

    def __init__(self, nombre, tablero):
        self.nombre = nombre
        self.tablero = tablero
    
    def colocar_barcos(self):
        clases_barcos = [Portaaviones, Destructor, Submarino, Fragata, Patrullero]

        for clase in clases_barcos:
            while True:
                try:
                    print(f"{self.nombre}, coloca un {clase.__name__}.")
                    fila, columna, orientacion = self.obtener_posicion()
                    barco = clase(fila, columna, orientacion)
                    #print(f"Colocando {barco.nombre} en ({fila}, {columna}) con orientación {orientacion}")
                    self.tablero.colocar_barco(barco)
                    break
                except BarcoMalColocadoError as e:
                    print(e)

    def obtener_posicion(self):
        pass  # Se reserva la implementación de este método para las clases derivadas

    
    def disparar(self):
        pass  # Cada tipode jugador implementará su propia estrategia de disparo


    def recibir_disparo(self, fila, columna):
        return self.tablero.recibir_disparo(fila, columna)
    
    @property
    def barcos_vivos(self):
        return self.tablero.barcos_vivos


class JugadorHumano(Jugador):
    def obtener_posicion(self):
        print(self.tablero)
        print(f"{self.nombre}, indica la posición para tu próximo barco.")
        fila = int(input('Fila: ')) - 1
        columna = ord(input('Columna: ').upper()) - ord('A')
        orientacion = input('Orientación (H/V): ')
        return fila, columna, Barco.HORIZONTAL if orientacion.upper() == 'H' else Barco.VERTICAL

    def disparar(self):
        fila = int(input('Fila: ')) - 1
        columna = ord(input('Columna: ').upper()) - ord('A')
        return fila, columna


class JugadorMaquina(Jugador):
    def obtener_posicion(self):
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        orientacion = random.choice([Barco.HORIZONTAL, Barco.VERTICAL])
        return fila, columna, orientacion
    
    def disparar(self):
        fila = random.randint(0, 9)
        columna = random.randint(0, 9)
        return fila, columna