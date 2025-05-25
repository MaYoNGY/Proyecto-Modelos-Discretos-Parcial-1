from ec.edu.espe.cheker_group4.model.tabla_verdad import TablaVerdad
class TableGenerator:
    @staticmethod
    def crear_tabla_verdad(cantidad_proposiciones):
        tabla = TablaVerdad(cantidad_proposiciones)
        main_menu = tabla.generar_tabla()