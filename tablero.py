from barcos import Barco, Portaaviones, Destructor, Submarino, Fragata, Patrullero
import random
from colorama import Fore, Back, Style

class BarcoMalColocadoError(Exception):
    pass


class Tablero:

    def __init__(self):
        self.barcos = []
        self.disparos = []

    def colocar_barco(self, barco):
        if any([not (0 <= fila < 10 and 0 <= columna < 10) for fila, columna in barco.casillas_ocupadas()]):
            raise BarcoMalColocadoError('El barco se sale del tablero')
        for otro_barco in self.barcos:
            if barco.colisiona_con(otro_barco):
                raise BarcoMalColocadoError('El barco colisiona con otro barco ya colocado')
        self.barcos.append(barco)

    def __str__(self):
        s = '    A   B   C   D   E   F   G   H   I   J\n  +---+---+---+---+---+---+---+---+---+---+\n'
        for fila in range(10):
            s += f"{fila+1:2d}"
            for columna in range(10):
                for barco in self.barcos:
                    # Si hay un disparo, lo mostramos
                    if (fila, columna) in self.disparos:
                        if (fila, columna) in barco.casillas_ocupadas():
                            s += '|' + Fore.RED + ' X ' + Fore.RESET
                            break                    
                    # Si no hay disparo, comprobamos si hay un barco y en ese caso mostramos su inicial
                    if (fila, columna) in barco.casillas_ocupadas():
                        s += '| ' + Fore.YELLOW + barco.nombre[0] + Fore.RESET + ' ' # Tomo la inicial del nombre del barco
                        break
                else:
                    s += '|' + Fore.CYAN + ' O ' + Fore.RESET if (fila, columna) in self.disparos else '|   '
            s += '|\n  +---+---+---+---+---+---+---+---+---+---+\n'
        return s
    
    def recibir_disparo(self, fila, columna):
        # Nos aseguramos de que el disparo esté dentro del tablero
        if not (0 <= fila < 10 and 0 <= columna < 10):
            raise ValueError('Disparo fuera del tablero')
        # Revisamos los disparos previos para no repetir
        if (fila, columna) in self.disparos:
            raise ValueError('Ya se ha disparado en esa casilla')
        self.disparos.append((fila, columna))
        # Comprobamos si el impacto afecta a alguno de los barcos
        for barco in self.barcos:
            if (fila, columna) in barco.casillas_ocupadas():
                return True
        # Si no hay barcos afectados, devolvemos False
        return False
    
    # Visualización únicamente de los impactos en el tablero
    @property
    def radar(self):
        s = '    A   B   C   D   E   F   G   H   I   J\n  +---+---+---+---+---+---+---+---+---+---+\n'
        for fila in range(10):
            s += f"{fila+1:2d}"
            for columna in range(10):
                # Primero vemos si hay un disparo en esa casilla
                if (fila, columna) not in self.disparos:
                    s += '|   '
                    continue
                # Si hay un disparo, comprobamos si ha tocado algún barco
                tocado = False
                for barco in self.barcos:
                    if (fila, columna) in barco.casillas_ocupadas():
                        tocado = True
                        break
                
                s += '|' + Fore.RED + ' X ' + Fore.RESET if tocado else '|' + Fore.CYAN + ' O ' + Fore.RESET  # En otros lenguajes: tocado ? "| X " : "| O "

            s += '|\n  +---+---+---+---+---+---+---+---+---+---+\n'
        return s

    @property
    def barcos_vivos(self):
        return [barco for barco in self.barcos if any(c not in self.disparos for c in barco.casillas_ocupadas())]


if __name__ == '__main__':
    t = Tablero()
    clases_barcos = [Portaaviones, Destructor, Submarino, Fragata, Patrullero]

    for clase in clases_barcos:
        while True:
            try:
                fila = random.randint(0, 9)
                columna = random.randint(0, 9)
                orientacion = random.choice([Barco.HORIZONTAL, Barco.VERTICAL])
                barco = clase(fila, columna, orientacion)
                print(f"Colocando {barco.nombre} en ({fila}, {columna}) con orientación {orientacion}")
                t.colocar_barco(barco)
                print(t)
                print('---')
                break
            except BarcoMalColocadoError as e:
                print(e)

    t.recibir_disparo(5, 5)
    t.recibir_disparo(5, 6)
    t.recibir_disparo(5, 7)

    print(t.radar)
    print(t)

