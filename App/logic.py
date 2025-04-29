import time
import csv
from datetime import datetime

csv.field_size_limit(2147483647)

def init():
    """
    Crea el catálogo para almacenar las estructuras de datos
    """
    catalog = {
        'crimes': []  # Acá lo cmabipe por init, para que no nos confundamos cuando llamamos a la función en otros lados 
    }
    return catalog

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del archivo CSV dado y los almacena en el catálogo
    """
    filepath = f"Data/Crime_in_LA/{filename}"  # como el  nombre del archivo es solo uno, se maneja la cantidad de los datos desde el view
    with open(filepath, encoding="utf-8-sig") as csvfile:
        input_file = csv.DictReader(csvfile)
        for crime in input_file:
            catalog['crimes'].append(crime)
    return len(catalog['crimes'])  # Retorna la cantidad de crímenes cargados

def get_data(catalog, id):
    """
    Retorna un dato por su ID (DR_NO).
    """
    for crime in catalog['crimes']:
        if crime['DR_NO'] == id:
            return crime
    return None


def req_1(catalog, fecha_inicial, fecha_final):
    """
    Retorna los crímenes ocurridos entre dos fechas dadas, ordenados del más reciente al más antiguo.
    Muestra los primeros 5 crímenes encontrados.
    """
    crimes_in_range = []

    # Convertimos las fechas de entrada a objetos con el datetime
    fecha_inicial_dt = datetime.strptime(fecha_inicial, "%Y-%m-%d")
    fecha_final_dt = datetime.strptime(fecha_final, "%Y-%m-%d")

    for crime in catalog['crimes']:
        date_occ_str = crime['DATE OCC']
        try:
            # TOMAMOS SOLO LA FECHA (sin la hora para que no salgan errores) 
            date_only_str = date_occ_str.split(' ')[0]
            date_occ_dt = datetime.strptime(date_only_str, "%m/%d/%Y")
            if fecha_inicial_dt <= date_occ_dt <= fecha_final_dt:
                crimes_in_range.append(crime)
        except ValueError:
            # Si hay error de formato de fecha, ignoramos ese registro
            continue

    # Ordenar:
    #  Primero por fecha más reciente
    #  Luego por TIME OCC más alto (hora más reciente)
    #  Luego por AREA NAME en orden descendente
    def sort_key(crime):
        date_occ = datetime.strptime(crime['DATE OCC'].split(' ')[0], "%m/%d/%Y")
        time_occ = int(crime['TIME OCC'])  # TIME OCC es un entero de formato HHMM
        area_name = crime['AREA NAME']
        return (-date_occ.timestamp(), -time_occ, area_name)

    crimes_in_range.sort(key=sort_key)

    # Construimos la respuesta final
    result = []
    for crime in crimes_in_range:
        result.append({
        "DR_NO": crime["DR_NO"],
        "DATE OCC": crime["DATE OCC"].split(' ')[0],  
        "TIME OCC": crime["TIME OCC"],
        "AREA NAME": crime["AREA NAME"],
        "Crm Cd": crime["Crm Cd"],
        "LOCATION": crime["LOCATION"]
    })

    return result

16,657

def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass




def get_time():
    
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    
    elapsed = float(end - start)
    return elapsed
