import keyboard

from view.entrada_teclado import VistaTerminal
from model.logica_proposicional import verificar_formula

def main():
    vista = VistaTerminal()
    vista.mostrar_instrucciones()

    while True:
        expr = vista.capturar_expresion()
        resultado = verificar_formula(expr)
        print(f"\nExpresión ingresada: {expr}")
        print(f"Resultado: {resultado}")

        

        respuesta = input("\n¿Deseas ingresar otra expresión? (s/n): ").strip().lower()
        if respuesta not in ['s', 'si', 'sí', 'y', 'yes']:
            print("Gracias por usar el verificador lógico. ")
            break

if __name__ == "__main__":
    main()
