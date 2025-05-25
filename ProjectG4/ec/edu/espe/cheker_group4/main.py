import keyboard
from model.tabla_verdad import TablaVerdad
from model.logica_proposicional import verificar_formula
from view.entrada_teclado import VistaTerminal

def main():
    vista = VistaTerminal()
    vista.mostrar_instrucciones()

    while True:
        expr = vista.capturar_expresion()
        resultado = verificar_formula(expr)
        print(f"\nExpresión ingresada: {expr}")

        # Generar y mostrar tabla de verdad
        tabla = TablaVerdad(expr)
        tabla.generar()
        tabla.mostrar()

        print(f"Resultado: {resultado}")

        respuesta = input("\n¿Deseas ingresar otra expresión? (s/n): ").strip().lower()
        if respuesta not in ['s', 'si', 'sí', 'y', 'yes']:
            print("Gracias por usar el verificador lógico.")
            break

if __name__ == "__main__":
    main()