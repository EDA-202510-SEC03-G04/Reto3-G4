import sys
from App import logic

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos basado en la densidad de datos que desea el usuario
    """
    print("¿Qué densidad de datos deseas cargar?")
    print("Opciones: 20, 40, 60, 80, 100")
    porcentaje = input("Escribe solo el número (por ejemplo 20):\n").strip()

    # Verificamos que esté entre las opciones válidas
    if porcentaje not in {"20", "40", "60", "80", "100"}:
        print("Opción inválida. Se cargará Crime_in_LA_20.csv por defecto.")
        porcentaje = "20"

    filename = f"Crime_in_LA_{porcentaje}.csv"
    total_crimes = logic.load_data(control, filename)
    print(f"\nSe cargaron {total_crimes} crímenes desde {filename}.\n")

def print_data(control, id):
    """
    Función que imprime un dato dado su ID
    """
    crime = logic.get_data(control, id)
    if crime:
        print(crime)
    else:
        print("No se encontró el crimen con el ID dado.")

def print_req_1(control):
    """
    Función que imprime la solución del Requerimiento 1 en consola
    """
    fecha_inicial = input("Ingrese la fecha inicial (formato YYYY-MM-DD):\n")
    fecha_final = input("Ingrese la fecha final (formato YYYY-MM-DD):\n")
    resultados = logic.req_1(control, fecha_inicial, fecha_final)

    if resultados:
        print(f"\nSe encontraron {len(resultados)} crímenes en el rango dado.\n")
        
        print("Mostrando los primeros 5 resultados:\n")
        print("DR_NO\t\tDATE OCC\tTIME OCC\tAREA NAME\t\tCrm Cd\tLOCATION")
        print("-" * 80)

        for crimen in resultados[:5]:
            print(f"{crimen['DR_NO']}\t{crimen['DATE OCC']}\t{crimen['TIME OCC']}\t\t{crimen['AREA NAME']}\t{crimen['Crm Cd']}\t{crimen['LOCATION']}")
    else:
        print("\nNo se encontraron crímenes en el rango de fechas dado.\n")

# Todo este view es temporal, solo era para guiarme mejor
def print_req_2(control):
    print("\nEjecutando Requerimiento 2:")
    resultado = logic.req_2(control)
    print(resultado)

def print_req_3(control):
    print("\nEjecutando Requerimiento 3:")
    resultado = logic.req_3(control)
    print(resultado)

def print_req_4(control):
    print("\nEjecutando Requerimiento 4:")
    resultado = logic.req_4(control)
    print(resultado)

def print_req_5(control):
    print("\nEjecutando Requerimiento 5:")
    resultado = logic.req_5(control)
    print(resultado)

def print_req_6(control):
    print("\nEjecutando Requerimiento 6:")
    resultado = logic.req_6(control)
    print(resultado)

def print_req_7(control):
    print("\nEjecutando Requerimiento 7:")
    resultado = logic.req_7(control)
    print(resultado)

def print_req_8(control):
    print("\nEjecutando Requerimiento 8 (BONO):")
    resultado = logic.req_8(control)
    print(resultado)

def main():
    """
    Menu principal
    """
    control = logic.init()  # Ahora creamos el catálogo aquí
    working = True
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if inputs.isdigit():
            inputs = int(inputs)
            if inputs == 1:
                load_data(control)
            elif inputs == 2:
                print_req_1(control)
            elif inputs == 3:
                print_req_2(control)
            elif inputs == 4:
                print_req_3(control)
            elif inputs == 5:
                print_req_4(control)
            elif inputs == 6:
                print_req_5(control)
            elif inputs == 7:
                print_req_6(control)
            elif inputs == 8:
                print_req_7(control)
            elif inputs == 9:
                print_req_8(control)
            elif inputs == 0:
                working = False
                print("\nGracias por utilizar el programa.")
            else:
                print("Opción errónea, vuelva a elegir.\n")
        else:
            print("Por favor ingrese un número válido.\n")
    sys.exit(0)

if __name__ == "__main__":
    default_limit = 1000
    sys.setrecursionlimit(default_limit * 10)
    main()
