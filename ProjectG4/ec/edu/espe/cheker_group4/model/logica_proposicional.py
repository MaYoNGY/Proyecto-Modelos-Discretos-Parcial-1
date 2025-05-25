import itertools


def neg(p):
    return not p

def conj(p, q):
    return p and q

def disj(p, q):
    return p or q

def impl(p, q):
    return (not p) or q

def biimpl(p, q):
    return p == q

def traducir(expr):
    expr = expr.replace('¬', 'neg')
    expr = expr.replace('~', 'neg')
    expr = expr.replace('∧', 'and').replace('&', 'and')
    expr = expr.replace('∨', 'or').replace('|', 'or')
    expr = expr.replace('→', 'impl').replace('=>', 'impl')
    expr = expr.replace('↔', 'biimpl').replace('<=>', 'biimpl')
    return expr


def obtener_variables(expr):
    return sorted(set(filter(str.isalpha, expr)))

def evaluar_expr(expr, valores):
    expr_traducida = traducir(expr)
    for var, val in valores.items():
        expr_traducida = expr_traducida.replace(var, str(val))
    return eval(expr_traducida)


def verificar_formula(expr):
    variables = obtener_variables(expr)
    combinaciones = list(itertools.product([True, False], repeat=len(variables)))

    resultados = []
    for combinacion in combinaciones:
        valores = dict(zip(variables, combinacion))
        resultado = evaluar_expr(expr, valores)
        resultados.append(resultado)

    if all(resultados):
        return "Tautología"
    elif all(r is False for r in resultados):
        return "Contradicción"
    else:
        return "Indeterminada"
