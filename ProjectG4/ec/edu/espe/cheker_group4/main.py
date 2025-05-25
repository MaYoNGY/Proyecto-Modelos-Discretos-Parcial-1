<<<<<<< HEAD
from model.tabla_verdad import TablaVerdad
from model.logica_proposicional import verificar_formula
=======
import keyboard

>>>>>>> 047d37f6171f63f0750fe16eaee50537a596d5ab
from view.entrada_teclado import VistaTerminal
from model.logica_proposicional import verificar_formula

def main():
<<<<<<< HEAD
    vista = VistaTerminal()                
    vista.mostrar_instrucciones()          
    expr = vista.capturar_expresion()      
    resultado = verificar_formula(expr)    
    print(f"\nExpresión ingresada: {expr}")
    tabla = TablaVerdad(expr)
    tabla.generar()
    tabla.mostrar() 
    print(f"Resultado: {resultado}")       
=======
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
>>>>>>> 047d37f6171f63f0750fe16eaee50537a596d5ab

if __name__ == "__main__":
    main()
