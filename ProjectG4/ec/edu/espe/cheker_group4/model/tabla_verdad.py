# tabla_verdad.py
import itertools
from model.logica_proposicional import parser, evaluar_expr, obtener_variables
'''
Esta clase genera una tabla de verdad para una expresión lógica dada.
Tomando una expresión lógica, identifica las variables involucradas 
y evalúa todas las combinaciones posibles de valores de verdad (True/False) para esas variables. 
Luego, muestra una tabla que incluye los valores de las variables
y el resultado de la expresión lógica evaluada para cada combinación.
'''
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
            fila = {**valores, self.expresion: resultado}
            self.filas.append(fila)

    def mostrar(self):
        print("\nTabla de Verdad:")
        encabezado = ' | '.join(self.variables + [self.expresion])
        print(encabezado)
        print('-' * len(encabezado))
        for fila in self.filas:
            valores = [str(int(fila[var])) for var in self.variables]
            # Convertir valores booleanos a 1 o 0
            resultado = str(int(fila[self.expresion])) if isinstance(fila[self.expresion], bool) else str(fila[self.expresion])
            print(' | '.join(valores + [resultado]))
