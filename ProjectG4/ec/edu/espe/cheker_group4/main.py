import keyboard
import time
import msvcrt  
from model.validacion_parentesis import validar_parentesis
from model.tabla_verdad import TablaVerdad
from model.logica_proposicional import verificar_formula
from view.entrada_teclado import VistaTerminal

'''
Este es el punto de entrada principal del programa.
Permite al usuario ingresar expresiones lógicas
'''
def main():
    vista = VistaTerminal()
    

    while True:
        print()
        vista.mostrar_instrucciones()
        expr = vista.capturar_expresion()
        #Validar la expresión ingresada, parentesis y letras
        if validar_parentesis(expr):
            print("\nError: La expresión ingresada parece ambigua. Utiliza p,r,s... y paréntesis por jeraruía operacional .\n")
            print("Ejemplo: (p ∨ q) ∧ r")
            continue

        resultado = verificar_formula(expr)
        print(f"\nExpresión ingresada: {expr}")

        # Generar y mostrar tabla de verdad
        tabla = TablaVerdad(expr)
        tabla.generar()
        tabla.mostrar()

        print(f"Resultado: {resultado}")

        print("\n¿Deseas ingresar otra expresión? (s = sí / cualquier otra = no): ", end='', flush=True)
        while True:
            evento = keyboard.read_event()
            if evento.event_type == keyboard.KEY_DOWN:
                tecla = evento.name.lower()
                if tecla == 's':
                    break
                else:
                    print("\nGracias por usar el verificador lógico.")
                    time.sleep(0.5)
                    keyboard.clear_all_hotkeys()
                    keyboard.unhook_all()

                    
                    while msvcrt.kbhit():
                        msvcrt.getch()

                    print("Presiona Enter para cerrar...")
                    while True:
                        if msvcrt.getch() == b'\r':  
                            return
        
if __name__ == "__main__":
    main()

