from 


def main():
    vista = VistaTerminal()                
    vista.mostrar_instrucciones()          
    expr = vista.capturar_expresion()      
    resultado = verificar_formula(expr)    
    print(f"\nExpresión ingresada: {expr}") 
    print(f"Resultado: {resultado}")       

if __name__ == "__main__":
    main()
