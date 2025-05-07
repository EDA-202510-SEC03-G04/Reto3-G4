import time
import csv
from datetime import datetime
from DataStructures import Tree as bst
from DataStructures import List as lt
csv.field_size_limit(2147483647)

def init():
    """
    Crea el catálogo para almacenar las estructuras de datos
    
    """
     
    catalog = {
        'crimes': []  # Acá lo cmabipe por init, para que no nos confundamos cuando llamamos a la función en otros lados 
    } 
    catalog["date_index"] = bst.new_tree() 
    catalog["age_index"] = bst.new_tree() 
    return catalog

# Funciones para la carga de datos
def load_date_tree(catalog):
    
    crimes = catalog["crimes"]
    
    for crime in crimes["elements"]:
        date_index = crime["DATE OCC"][0:10]
        lista = bst.get(catalog["date_index"], date_index)
    
        if lista != None:
            lt.add_last(lista, crime)
        else:
            new_list = lt.new_list()
            lt.add_last(new_list, crime)
            bst.put(catalog["date_index"], date_index, new_list)
        
        
def load_age_tree(catalog):
    
    crimes = catalog["crimes"]
    
    for crime in crimes["elements"]:
        age_index = crime["Vict age"]
        lista = bst.get(catalog["age_index"], age_index)
    
        if lista != None:
            lt.add_last(lista, crime)
        else:
            new_list = lt.new_list()
            lt.add_last(new_list, crime)
            bst.put(catalog["age_index"], age_index, new_list)        
    
    
    
    
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

    # Lo vamos a ordernar de la siguiente manera:
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



def req_2(catalog, fecha_inicial, fecha_final):
    """
    Retorna los crímenes graves (Part 1) resueltos entre dos fechas dadas,
    ordenados del más reciente al más antiguo.
    """
    crimes_in_range = []

    fecha_inicial_dt = datetime.strptime(fecha_inicial, "%Y-%m-%d")
    fecha_final_dt = datetime.strptime(fecha_final, "%Y-%m-%d")

    for crime in catalog['crimes']:
        date_occ_str = crime['DATE OCC']
        try:
            date_only_str = date_occ_str.split(' ')[0]
            date_occ_dt = datetime.strptime(date_only_str, "%m/%d/%Y")
            part = crime.get('Part 1-2', '')
            status = crime.get('Status', '')

            # Aca se verifica que cumpla la condicon
            if (fecha_inicial_dt <= date_occ_dt <= fecha_final_dt and
                part == '1' and
                status not in {"IC", "AO"}):  # Asumimos que IC y AO no son casos resueltos
                crimes_in_range.append(crime)
        except ValueError:
            continue

    def sort_key(crime):
        date_occ = datetime.strptime(crime['DATE OCC'].split(' ')[0], "%m/%d/%Y")
        time_occ = int(crime['TIME OCC'])
        area_name = crime['AREA NAME']
        return (-date_occ.timestamp(), -time_occ, area_name)

    crimes_in_range.sort(key=sort_key)

    result = []
    for crime in crimes_in_range:
        result.append({
            "DR_NO": crime["DR_NO"],
            "DATE OCC": crime["DATE OCC"].split(' ')[0],
            "TIME OCC": crime["TIME OCC"],
            "AREA": crime["AREA"],
            "Rpt Dist No": crime["Rpt Dist No"],
            "Part 1-2": crime["Part 1-2"],
            "Crm Cd": crime["Crm Cd"],
            "Status": crime["Status"]
        })

    return result


def req_3(catalog, area_name, n):
    """
    Retorna los N crímenes más recientes en un área dada.
    """
    crimes_in_area = []

    for crime in catalog['crimes']:
        area = crime.get('AREA NAME', '').strip().lower()
        if area == area_name.strip().lower():
            crimes_in_area.append(crime)

    # Acá lo vamos a Ordenar más recientes primero
    def sort_key(crime):
        date_occ = datetime.strptime(crime['DATE OCC'].split(' ')[0], "%m/%d/%Y")
        time_occ = int(crime['TIME OCC'])
        return (-date_occ.timestamp(), -time_occ)

    crimes_in_area.sort(key=sort_key)

    # Construimos la respuesta
    result = []
    for crime in crimes_in_area[:n]:  # Solo los N primeros ( los que diga el usuario )
        result.append({
            "DR_NO": crime["DR_NO"],
            "DATE OCC": crime["DATE OCC"].split(' ')[0],
            "TIME OCC": crime["TIME OCC"],
            "AREA": crime["AREA"],
            "Rpt Dist No": crime["Rpt Dist No"],
            "Part 1-2": crime["Part 1-2"],
            "Crm Cd": crime["Crm Cd"],
            "Status": crime["Status"],
            "LOCATION": crime["LOCATION"]
        })

    return result

def sort_req4(data_1,data_2):
    
    if int(data_1["part 1-2"]) < int(data_2["part 1-2"]):
        if int(data_1["Vict age"]) > int(data_2["Vict age"]):
            return True
        elif int(data_1["Vict age"]) == int(data_2["Vict age"]):
            if data_1["DATE OCC"][0:10] < data_2["DATE_OCC"][0:10]:
                return True

    return False
    


def req_4(catalog,N, min_age, max_age):
    """
    Retorna el resultado del requerimiento 4
    """
    
    tree_by_age = catalog["age_index"]
    
    list_filtered = lt.new_list()
    
    list_values_range = bst.values(tree_by_age, min_age, max_age)
    
    for internal_list in list_values_range:
        for crime in internal_list["elements"]:
        
            lt.add_last(list_filtered, crime)
    list_sorted = lt.merge_sort(list_filtered, sort_req4)
            
            
    if lt.size(list_sorted) > N:
        return lt.sub_list(list_sorted, 0, N)
    else:
        return list_sorted
            
 
    
def sort_req5(data_1,data_2):
    
    if data_1["Not_resolved"] < data_2["Not_resolved"]:
        return True
    elif data_1["Not_resolved"] == data_2["Not_resolved"]:
         
         if data_1["AREA NAME"] < data_2["AREA NAME"]:
             return True
         
    return False       


def req_5(catalog,N , date_min, date_max):
    """
    Retorna el resultado del requerimiento 5
    """
    tree_by_date = catalog["date_index"]
    
    list_areas_control = lt.new_list()
    list_areas = lt.new_list()
    list_values_range = bst.values(tree_by_date, date_min, date_max)
    
    for list_value in list_values_range:
        for crime in list_value["elements"]:
            crime_area = crime["AREA"]
            index = lt.is_present(list_areas_control, crime_area)
            if index == -1:
                lt.add_last(list_areas_control, crime_area)
                dict_area = {"AREA": crime_area,
                "AREA NAME": crime["AREA NAME"],
                "Not_resolved": 0, 
                "first":crime,
                "last": crime}
                
                if crime["Status"]  == "IC":
                    
                    dict_area["Not_resolved"] += 1
                    lt.add_last(list_areas, dict_area)
            else:
                dict_area = lt.get_element(list_areas, index)
                
                if crime["Status"] == "IC":
                    dict_area["Not_resolved"] += 1
                    
                if dict_area["first"]["DATE OCC"][0:10] > crime["DATE OCC"][0:10]:
                       dict_area["first"] = crime
                
                if dict_area["last"]["DATE OCC"][0:10] < crime["DATE OCC"][0:10]:
                    dict_area["last"] = crime           
    
    sorted_list = lt.merge_sort(list_areas, sort_req5)
    
    if lt.size(sorted_list) > N:
        return lt.sub_list(sorted_list, 0, N)
    else:
        return sorted_list        
                
def req_6(catalog, sexo, mes, n):
    """
    Retorna las N áreas más seguras para un sexo en un mes específico.
    """
    areas = {}

    for crime in catalog['crimes']:
        victim_sex = crime.get('Vict Sex', '').strip().upper()
        if victim_sex != sexo.upper():
            continue

        date_occ_str = crime.get('DATE OCC', '')
        try:
            date_only_str = date_occ_str.split(' ')[0]
            date_occ_dt = datetime.strptime(date_only_str, "%m/%d/%Y")
            if date_occ_dt.month != mes:
                continue
        except:
            continue

        area = crime.get('AREA', '')
        area_name = crime.get('AREA NAME', '').strip()
        year = date_occ_dt.year

        if area not in areas:
            areas[area] = {
                "AREA": area,
                "AREA NAME": area_name,
                "total_crimes": 0,
                "crimes_per_year": {}
            }

        areas[area]["total_crimes"] += 1
        areas[area]["crimes_per_year"][year] = areas[area]["crimes_per_year"].get(year, 0) + 1

    # Convertimos a lista
    areas_list = list(areas.values())

    # Lo ordemaos de la siguiente forma: 
    # - Menor cantidad de crímenes
    # - Luego por menor cantidad de años
    # - Luego alfabéticamente por nombre
    areas_list.sort(key=lambda x: (x["total_crimes"], len(x["crimes_per_year"]), x["AREA NAME"]))

    # Preparamos la respuesta
    result = []
    for area in areas_list[:n]:
        result.append({
            "AREA": area["AREA"],
            "AREA NAME": area["AREA NAME"],
            "Total Crímenes": area["total_crimes"],
            "Crímenes por Año": [(cantidad, año) for año, cantidad in sorted(area["crimes_per_year"].items())]
        })

    return result


def req_7(catalog, sexo, edad_inicial, edad_final, n):
    """
    Retorna los N crímenes más comunes para un sexo en un rango de edad dado.
    """
    crimes_by_type = {}

    for crime in catalog['crimes']:
        victim_sex = crime.get('Vict Sex', '').strip().upper()
        if victim_sex != sexo.upper():
            continue

        try:
            victim_age = int(crime.get('Vict Age', -1))
        except:
            continue

        if not (edad_inicial <= victim_age <= edad_final):
            continue

        crime_code = crime.get('Crm Cd', '')
        date_occ_str = crime.get('DATE OCC', '')
        try:
            year = datetime.strptime(date_occ_str.split(' ')[0], "%m/%d/%Y").year
        except:
            continue

        if crime_code not in crimes_by_type:
            crimes_by_type[crime_code] = {
                "Crm Cd": crime_code,
                "Total Crímenes": 0,
                "Crímenes por Edad": {},
                "Crímenes por Año": {}
            }

        crimes_by_type[crime_code]["Total Crímenes"] += 1
        crimes_by_type[crime_code]["Crímenes por Edad"][victim_age] = crimes_by_type[crime_code]["Crímenes por Edad"].get(victim_age, 0) + 1
        crimes_by_type[crime_code]["Crímenes por Año"][year] = crimes_by_type[crime_code]["Crímenes por Año"].get(year, 0) + 1

    # Convertimos a lista
    crimes_list = list(crimes_by_type.values())

    # Definimos una función para ordenar
    def criterio_ordenamiento(crime):
        return crime["Total Crímenes"]

    # Ordenamos usando la función para ponerlo en orden descendente
    crimes_list.sort(key=criterio_ordenamiento, reverse=True)

    # Preparamos la respuesta
    result = []
    for crime in crimes_list[:n]:
        crimen_por_edad = []
        for edad, cantidad in sorted(crime["Crímenes por Edad"].items()):
            crimen_por_edad.append((cantidad, edad))

        crimen_por_anio = []
        for anio, cantidad in sorted(crime["Crímenes por Año"].items()):
            crimen_por_anio.append((cantidad, anio))

        result.append({
            "Crm Cd": crime["Crm Cd"],
            "Total Crímenes": crime["Total Crímenes"],
            "Crímenes por Edad": crimen_por_edad,
            "Crímenes por Año": crimen_por_anio
        })

    return result


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
