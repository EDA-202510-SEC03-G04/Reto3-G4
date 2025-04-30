import sys
from App import logic
from tabulate import tabulate 

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


def print_req_2(control):
    """
    Función que imprime la solución del Requerimiento 2 en consola
    """
    fecha_inicial = input("Ingrese la fecha inicial (formato YYYY-MM-DD):\n")
    fecha_final = input("Ingrese la fecha final (formato YYYY-MM-DD):\n")
    resultados = logic.req_2(control, fecha_inicial, fecha_final)

    if resultados:
        print(f"\nSe encontraron {len(resultados)} crímenes graves resueltos en el rango dado.\n")
        
        print("Mostrando los primeros 5 resultados:\n")
        print("DR_NO\t\tDATE OCC\tTIME OCC\tAREA\tRpt Dist No\tPart 1-2\tCrm Cd\tStatus")
        print("-" * 100)

        for crimen in resultados[:5]:
            print(f"{crimen['DR_NO']}\t{crimen['DATE OCC']}\t{crimen['TIME OCC']}\t{crimen['AREA']}\t{crimen['Rpt Dist No']}\t\t{crimen['Part 1-2']}\t\t{crimen['Crm Cd']}\t{crimen['Status']}")
    else:
        print("\nNo se encontraron crímenes graves resueltos en el rango de fechas dado.\n")

def print_req_3(control):
    """
    Función que imprime la solución del Requerimiento 3 en consola
    """
    area_name = input("Ingrese el nombre del área (tal como aparece en los datos, por ejemplo 'Hollywood'):\n")
    n = int(input("Ingrese el número de crímenes más recientes que desea listar:\n"))
    resultados = logic.req_3(control, area_name, n)

    if resultados:
        print(f"\nSe encontraron {len(resultados)} crímenes en el área {area_name.title()}.\n")
        
        print("Mostrando los crímenes más recientes:\n")
        print("DR_NO\t\tDATE OCC\tTIME OCC\tAREA\tRpt Dist No\tPart 1-2\tCrm Cd\tStatus\tLOCATION")
        print("-" * 120)

        for crimen in resultados:
            print(f"{crimen['DR_NO']}\t{crimen['DATE OCC']}\t{crimen['TIME OCC']}\t{crimen['AREA']}\t{crimen['Rpt Dist No']}\t\t{crimen['Part 1-2']}\t\t{crimen['Crm Cd']}\t{crimen['Status']}\t{crimen['LOCATION']}")
    else:
        print(f"\nNo se encontraron crímenes en el área {area_name.title()}.\n")


def print_req_4(control):
    print("\nEjecutando Requerimiento 4:")
    N = int(input("Ingrese el número de crímenes a listar:\n"))
    min_age = int(input("Ingrese la edad mínima:\n"))
    max_age = int(input("Ingrese la edad máxima:\n"))
    resultado = control.req_4(control, N, min_age, max_age)
    crimenes = resultado["elements"]
    
    print(f"\nNúmero total de crímenes que cumplen el criterio: {len(crimenes)}\n")

    tabla = []
    for crimen in crimenes:
        fila = [
            crimen.get("DR_NO", ""),          # ID del reporte
            crimen.get("DATE OCC", ""),       # Fecha en que ocurrió
            crimen.get("TIME OCC", ""),       # Hora del crimen
            crimen.get("AREA NAME", ""),      # Área
            crimen.get("Rpt Dist No", ""),    # Subárea
            crimen.get("Part 1-2", ""),       # Gravedad (Part 1 o Part 2)
            crimen.get("Crm Cd", ""),         # Código del crimen
            crimen.get("Vict Age", ""),       # Edad de la víctima
            crimen.get("Status", ""),         # Estado del caso
            crimen.get("LOCATION", "")        # Dirección del crimen
        ]
        tabla.append(fila)

    headers = [
        "ID Reporte", "Fecha", "Hora", "Área", "Subárea", "Gravedad",
        "Código", "Edad Víctima", "Estado del Caso", "Dirección"
    ]

    print(tabulate(tabla, headers=headers, tablefmt="grid"))

def print_req_5(control):
    print("\nEjecutando Requerimiento 5:")
    N = int(input("Ingrese el número de áreas a listar:\n"))
    date_min = input("Ingrese la fecha mínima (formato YYYY-MM-DD):\n")
    date_max = input("Ingrese la fecha máxima (formato YYYY-MM-DD):\n")
    resultado = control.req_5(control, N, date_min, date_max)
    areas = resultado["elements"]

    print(f"\nSe encontraron {len(areas)} áreas en el rango de fechas dado.\n")

    tabla = []
    for area in areas:
        fila = [
            area.get("AREA", ""),
            area.get("AREA NAME", ""),
            area.get("Not_resolved", 0),
            area["first"].get("DATE OCC", "")[:10],
            area["last"].get("DATE OCC", "")[:10]
        ]
        tabla.append(fila)

    headers = [
        "Área", "Nombre del Área", "Crímenes No Resueltos",
        "Fecha del Primer Crimen", "Fecha del Último Crimen"
    ]

    print(tabulate(tabla, headers=headers, tablefmt="grid"))

def print_req_6(control):
    """
    Función que imprime la solución del Requerimiento 6 en consola
    """
    sexo = input("Ingrese el sexo a consultar (M o F):\n")
    mes = int(input("Ingrese el número del mes (1-12):\n"))
    n = int(input("Ingrese el número de áreas a listar:\n"))

    resultados = logic.req_6(control, sexo, mes, n)

    if resultados:
        print(f"\nSe encontraron {len(resultados)} áreas más seguras para sexo {sexo.upper()} en el mes {mes}.\n")
        
        print("AREA\tAREA NAME\t\tTotal Crímenes\tCrímenes por Año")
        print("-" * 100)

        for area in resultados:
            print(f"{area['AREA']}\t{area['AREA NAME']}\t{area['Total Crímenes']}\t{area['Crímenes por Año']}")
    else:
        print("\nNo se encontraron áreas que cumplan con los criterios dados.\n")


def print_req_7(control):
    """
    Función que imprime la solución del Requerimiento 7 en consola
    """
    sexo = input("Ingrese el sexo de la víctima (M o F):\n")
    edad_inicial = int(input("Ingrese la edad mínima:\n"))
    edad_final = int(input("Ingrese la edad máxima:\n"))
    n = int(input("Ingrese el número de tipos de crimen más comunes que desea listar:\n"))

    resultados = logic.req_7(control, sexo, edad_inicial, edad_final, n)

    if resultados:
        print(f"\nSe encontraron {len(resultados)} tipos de crímenes más comunes para víctimas {sexo.upper()} entre {edad_inicial} y {edad_final} años.\n")
        
        print("Crm Cd\tTotal Crímenes\tCrímenes por Edad\tCrímenes por Año")
        print("-" * 100)

        for crimen in resultados:
            print(f"{crimen['Crm Cd']}\t{crimen['Total Crímenes']}\t{crimen['Crímenes por Edad']}\t{crimen['Crímenes por Año']}")
    else:
        print("\nNo se encontraron crímenes que cumplan con los criterios dados.\n")


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
