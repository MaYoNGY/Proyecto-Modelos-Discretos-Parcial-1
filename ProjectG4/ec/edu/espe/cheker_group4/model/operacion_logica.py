class OperacionLogica:
    def __init__(self, operador, operandos):
        self.operador = operador.upper()  # 'AND', 'OR', 'NOT', 'IMPL', 'BIIMPL'
        self.operandos = operandos        # Lista de valores booleanos

    def evaluar(self):
        if self.operador == 'AND':
            return all(self.operandos)
        elif self.operador == 'OR':
            return any(self.operandos)
        elif self.operador == 'NOT':
            return not self.operandos[0]
        elif self.operador == 'IMPL':
            if len(self.operandos) == 2:
                return (not self.operandos[0]) or self.operandos[1]
            else:
                raise ValueError("La implicación requiere dos operandos")
        elif self.operador == 'BIIMPL':
            if len(self.operandos) == 2:
                return self.operandos[0] == self.operandos[1]
            else:
                raise ValueError("El bicondicional requiere dos operandos")
        else:
            raise ValueError(f"Operador lógico no soportado: {self.operador}")