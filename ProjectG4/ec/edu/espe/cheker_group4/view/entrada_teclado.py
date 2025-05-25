import keyboard

class VistaTerminal:
    def __init__(self):
        self.mapa_teclas = {
            '1': '∨',
            '2': '∧',
            '3': '¬',
            '4': '→',
            '5': '↔',
            '6': '(',
            '7': ')',
            '0': ' '
        }
        self.expresion = ""

    def mostrar_instrucciones(self):
        print("╔══════════════════════════════════════════════════════╗")
        print("║  CONSTRUCTOR DE EXPRESIONES LÓGICAS (TERMINAL)       ║")
        print("╠══════════════════════════════════════════════════════╣")
        print("║ Usa las teclas para escribir una expresión:          ║")
        print("║ Letras (p, q, r...) para proposiciones               ║")
        print("║ Teclas especiales:                                   ║")
        print("║  1 = ∨   2 = ∧   3 = ¬   4 = →   5 = ↔                ║")
        print("║  6 = (   7 = )   0 = espacio                         ║")
        print("║ Pulsa ENTER para evaluar.                            ║")
        print("╚══════════════════════════════════════════════════════╝\n")

    def capturar_expresion(self):
        self.expresion = ""
        print("Expresión: ", end='', flush=True)

        while True:
            evento = keyboard.read_event()
            if evento.event_type == keyboard.KEY_DOWN:
                tecla = evento.name

                if tecla == 'enter':
                    break

               
                elif tecla in self.mapa_teclas:
                    simbolo = self.mapa_teclas[tecla]
                    self.expresion += simbolo
                    print(simbolo, end='', flush=True)

             
                elif tecla is not None and len(tecla) == 1 and tecla.isalpha():
                    self.expresion += tecla
                    print(tecla, end='', flush=True)

                
                elif tecla == 'backspace' and self.expresion:
                    self.expresion = self.expresion[:-1]
                    print('\rExpresión: ' + ' ' * 80, end='\r')  
                    print('Expresión: ' + self.expresion, end='', flush=True)

            
                else:
                    pass

        print()  
        return self.expresion


        print()
        return self.expresion
