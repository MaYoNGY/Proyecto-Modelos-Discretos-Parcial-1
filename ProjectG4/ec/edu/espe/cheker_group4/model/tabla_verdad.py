
class TablaVerdad:
    def __init__(self, cantidad_proposiciones):
        self.cantidad_proposiciones = cantidad_proposiciones
        self.filas = 2 ** cantidad_proposiciones
        self.columnas = cantidad_proposiciones
        self.matriz = self.generar_tabla()
    def generar_tabla(self):
        matriz = []
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                repeticion = 2 ** (self.columnas - j - 1)
                valor = (i // repeticion) % 2 == 1
                fila.append(valor)
            matriz.append(fila)
        return matriz
    