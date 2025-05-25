import re

def validar_parentesis(expr):
    """
    Valida si una expresión compleja requiere paréntesis para evitar ambigüedades.
    Se permite una expresión simple con solo dos variables y un operador.
    Además, verifica que solo se usen las letras que se utilizan en proposiciones.
    """
    expr = expr.replace(" ", "")
    
    # Verifica letras desde p hasta z (minúsculas)
    letras_invalidas = re.findall(r"[a-oA-O]", expr)
    
    if letras_invalidas:
        return True
    #Verifica si la expresión es una proposición simple
    patron_simple = re.fullmatch(r"[a-zA-Z]([∨∧→↔])[a-zA-Z]", expr)

    if patron_simple:
        return False
    # Verifica si la expresión tiene operadores lógicos y paréntesis
    tiene_operadores = any(op in expr for op in ['∧', '∨', '→', '↔'])
    tiene_parentesis = '(' in expr and ')' in expr

    if tiene_operadores and not tiene_parentesis:
        return True

    return False
