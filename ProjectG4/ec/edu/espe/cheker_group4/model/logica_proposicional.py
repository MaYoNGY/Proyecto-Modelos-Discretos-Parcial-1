import itertools
import re

def neg(p): return not p
def conj(p, q): return p and q
def disj(p, q): return p or q
def impl(p, q): return (not p) or q
def biimpl(p, q): return p == q


def parser(expr):
    expr = expr.replace(' ', '')  #
    expr = reemplazar_binario(expr, '↔', 'biimpl')
    expr = reemplazar_binario(expr, '→', 'impl')
    expr = reemplazar_binario(expr, '∨', 'disj')
    expr = reemplazar_binario(expr, '∧', 'conj')
    expr = reemplazar_negaciones(expr)
    return expr

def reemplazar_binario(expr, simbolo, funcion):
    
    patron = re.compile(r'([a-zA-Z()]+)' + re.escape(simbolo) + r'([a-zA-Z(¬)]+)')
    while re.search(patron, expr):
        expr = re.sub(patron, rf'{funcion}(\1,\2)', expr)
    return expr

def reemplazar_negaciones(expr):
    
    expr = re.sub(r'¬([a-zA-Z(])', r'neg(\1', expr)
 
    paréntesis_abiertos = expr.count('neg(')
    paréntesis_cerrados = expr.count(')')
    diferencia = paréntesis_abiertos - paréntesis_cerrados
    expr += ')' * diferencia  
    return expr

def obtener_variables(expr):
    return sorted(set(filter(str.isalpha, expr)))

def evaluar_expr(expr, valores):
    expr_funcional = parser(expr)
    for var, val in valores.items():
        expr_funcional = expr_funcional.replace(var, str(val))
    return eval(expr_funcional, {
        'neg': neg,
        'conj': conj,
        'disj': disj,
        'impl': impl,
        'biimpl': biimpl,
        'True': True,
        'False': False
    })

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
