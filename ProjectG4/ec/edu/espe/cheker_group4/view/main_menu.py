from controller import table_generator

def main_menu():
    
    print("""
                                  
                                    
""")
    print("1. Empezar a evaluar")
    print("2. Salir")

    while True:
        choice = input("Selecciona la opción 1 o 2: ")
        if choice == '1':
            print("1. Definir numero de variables")
            print("2. Definir contradiccion de la primera proposicion")
            print("3. Ingresar proposiciones")
            print("4. Seleccionar operadores Logicos")
            print("5. ¿Desea continuar con el análisis de datos?")
            print("6. Atras")
            while True:
                choice = input("Selecciona la opción 1 o 2: ")
                if choice == '1':
                    print("Definir numero de variables")
                    pass
                elif choice == '2':
                    print("Definir contradiccion de la primera proposicion")
                    pass
                elif choice == '3':
                    print("Ingresar proposiciones")
                    pass
                elif choice == '4':
                    print("Seleccionar operadores Logicos")
                    pass
                elif choice == '5':
                    print("¿Desea continuar con el análisis de datos?")
                    pass
                elif choice == '6':
                    break
                else:
                    print("Seleccione una opción válida (1 o 2)")
            pass
        elif choice == '2':
            print("Saliendo del programa...")
            break
        else:
            print("Seleccione una opción válida (1 o 2)")
            if __name__ == "__main__":
                main_menu()