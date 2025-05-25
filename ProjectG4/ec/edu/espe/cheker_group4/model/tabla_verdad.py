# tabla_verdad.py
import itertools
from model.logica_proposicional import parser, evaluar_expr, obtener_variables

class TablaVerdad:
    def __init__(self, expresion):
        self.expresion = expresion
        self.variables = obtener_variables(expresion)
        self.filas = []

    def generar(self):
        combinaciones = list(itertools.product([True, False], repeat=len(self.variables)))
        for combinacion in combinaciones:
            valores = dict(zip(self.variables, combinacion))
            try:
                resultado = evaluar_expr(self.expresion, valores)
            except:
                resultado = "Error"
            fila = {**valores, 'Resultado': resultado}
            self.filas.append(fila)

    def mostrar(self):
        print("\nTabla de Verdad:")
        encabezado = ' | '.join(self.variables + ['Resultado'])
        print(encabezado)
        print('-' * len(encabezado))
        for fila in self.filas:
            valores = [str(fila[var]) for var in self.variables]
            print(' | '.join(valores + [str(fila['Resultado'])]))
