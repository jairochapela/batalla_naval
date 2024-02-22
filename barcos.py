
class Barco:
    
    HORIZONTAL = (0, 1)
    VERTICAL = (1, 0)

    # Constructor
    # nombre: nombre del barco
    # eslora: tamaño del barco (en casillas)
    # fila: fila en la que se encuentra el barco
    # columna: columna en la que se encuentra el barco
    # orientacion: orientación del barco (horizontal (0,1) o vertical (1,0))
    def __init__(self, nombre, eslora, fila, columna, orientacion):
        self.nombre = nombre
        self.eslora = eslora
        self.fila = fila
        self.columna = columna
        self.orientacion = orientacion

    # Método que devuelve las casillas que ocupa el barco
    def casillas_ocupadas(self):
        return [(self.fila + i * self.orientacion[0], self.columna + i * self.orientacion[1]) for i in range(self.eslora)]
    
    def en_zona_alrededor(self, fila, columna):
        if fila < self.fila - 1 or fila > self.fila + self.eslora*self.orientacion[0] + 1:
            return False
        if columna < self.columna - 1 or columna > self.columna + self.eslora*self.orientacion[1] + 1:
            return False
        return True
    
    def colisiona_con(self, otro_barco):
        return any([otro_barco.en_zona_alrededor(fila, columna) for fila, columna in self.casillas_ocupadas()])
    




class Portaaviones(Barco):
    def __init__(self, fila, columna, orientacion):
        super().__init__('Portaaviones', 5, fila, columna, orientacion)

class Destructor(Barco):
    def __init__(self, fila, columna, orientacion):
        super().__init__('Destructor', 4, fila, columna, orientacion)

class Submarino(Barco):
    def __init__(self, fila, columna, orientacion):
        super().__init__('Submarino', 3, fila, columna, orientacion)

class Fragata(Barco):
    def __init__(self, fila, columna, orientacion):
        super().__init__('Fragata', 3, fila, columna, orientacion)

class Patrullero(Barco):
    def __init__(self, fila, columna, orientacion):
        super().__init__('Patrullero', 2, fila, columna, orientacion)






if __name__ == '__main__':
    b1 = Portaaviones(5, 5, Barco.VERTICAL)
    b2 = Destructor(4, 0, Barco.HORIZONTAL)
    print(b1.casillas_ocupadas())
    print(b2.casillas_ocupadas())

    b3 = Destructor(3, 1, Barco.VERTICAL)
    for fila, columna in b3.casillas_ocupadas():
        print(fila, columna, b2.en_zona_alrededor(fila, columna))
