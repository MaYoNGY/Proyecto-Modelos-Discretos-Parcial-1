import itertools
import re
"""
Este módulo proporciona funciones para evaluar expresiones lógicas proposicionales.
Incluye la conversión de expresiones a funciones lógicas, evaluación de expresiones,
verificación de tautologías, indeterminaciones y contradicciones.
"""

# Definición de funciones lógicas básicas
def neg(p): return not p
def conj(p, q): return p and q
def disj(p, q): return p or q
def impl(p, q): return (not p) or q
def biimpl(p, q): return p == q

# Convierte una expresión lógica en una expresión evaluable por Python
def parser(expr):
    expr = convertir_a_funciones(expr)
    return expr

# Convierte los símbolos lógicos a operadores y funciones Python
def convertir_a_funciones(expr):
    expr = expr.replace('¬', '~')
    expr = expr.replace('∧', '&')
    expr = expr.replace('∨', '|')
    expr = expr.replace('→', '>')
    expr = expr.replace('↔', '=')

    # Funciones auxiliares para precedencia y operadores
    def precedencia(op):
        return {'~': 4, '&': 3, '|': 2, '>': 1, '=': 0}.get(op, -1)

    def es_operador(c):
        return c in {'~', '&', '|', '>', '='}

    # Algoritmo de Shunting Yard para convertir a notación postfija
    salida = []
    operadores = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c.isalpha():
            salida.append(c)
        elif c == '(':
            operadores.append(c)
        elif c == ')':
            while operadores and operadores[-1] != '(':
                salida.append(operadores.pop())
            operadores.pop()
        elif es_operador(c):
            if c == '~':
                operadores.append(c)
            else:
                while operadores and precedencia(c) < precedencia(operadores[-1]):
                    salida.append(operadores.pop())
                operadores.append(c)
        i += 1

    while operadores:
        salida.append(operadores.pop())

    # Convierte la notación postfija a una expresión Python evaluable
    pila = []
    for token in salida:
        if token.isalpha():
            pila.append(token)
        elif token == '~':
            op = pila.pop()
            pila.append(f'neg({op})')
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '&':
                pila.append(f'conj({a},{b})')
            elif token == '|':
                pila.append(f'disj({a},{b})')
            elif token == '>':
                pila.append(f'impl({a},{b})')
            elif token == '=':
                pila.append(f'biimpl({a},{b})')
    return pila[0]

# Reemplaza negaciones en la expresión por la función neg()
def reemplazar_negaciones(expr):
    resultado = ''
    i = 0
    while i < len(expr):
        if expr[i] == '¬':
            if i + 1 < len(expr) and expr[i + 1] == '(':
                subexpr, salto = extraer_parentesis(expr, i + 1)
                resultado += f'neg{subexpr}'
                i += salto
            else:
                resultado += f'neg({expr[i+1]})'
                i += 2
        else:
            resultado += expr[i]
            i += 1
    return resultado

# Reemplaza todos los operadores lógicos por sus funciones Python
def reemplazar_todos_los_operadores(expr):
    for simbolo, funcion in [('↔', 'biimpl'), ('→', 'impl'), ('∨', 'disj'), ('∧', 'conj')]:
        patron = re.compile(r'([a-zA-Z0-9_()]+)' + re.escape(simbolo) + r'([a-zA-Z0-9_()]+)')
        while re.search(patron, expr):
            expr = re.sub(patron, rf'{funcion}(\1,\2)', expr)
    return expr

# Extrae subexpresiones entre paréntesis
def extraer_parentesis(expr, inicio):
    i = inicio
    nivel = 0
    while i < len(expr):
        if expr[i] == '(':
            nivel += 1
        elif expr[i] == ')':
            nivel -= 1
            if nivel == 0:
                return expr[inicio:i + 1], i - inicio + 1
        i += 1
    raise ValueError("Paréntesis no balanceados")

# Obtiene todas las variables proposicionales de la expresión
def obtener_variables(expr):
    return sorted(set(filter(str.isalpha, expr)))

# Evalúa la expresión lógica usando los valores dados para las variables
def evaluar_expr(expr, valores):
    expr_traducida = parser(expr)
    for var, val in valores.items():
        expr_traducida = re.sub(rf'\b{var}\b', str(val), expr_traducida)
    return eval(expr_traducida, {
        'neg': neg,
        'conj': conj,
        'disj': disj,
        'impl': impl,
        'biimpl': biimpl,
        'True': True,
        'False': False
    })

# Verifica si la fórmula es tautología, contradicción o indeterminada
def verificar_formula(expr):
    variables = obtener_variables(expr)
    combinaciones = list(itertools.product([True, False], repeat=len(variables)))
    resultados = []

    for combinacion in combinaciones:
        valores = dict(zip(variables, combinacion))
        try:
            resultado = evaluar_expr(expr, valores)
        except Exception as e:
            return f"Error de sintaxis o evaluación: {e}"
        resultados.append(resultado)

    if all(resultados):
        return "Tautología"
    elif all(r is False for r in resultados):
        return "Contradicción"
    else:
        return "Indeterminada"
