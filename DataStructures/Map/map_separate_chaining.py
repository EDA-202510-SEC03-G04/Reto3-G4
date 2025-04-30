import random
from DataStructures.List import array_list as al
import map_entry as me
import map_functions as mf
from DataStructures.List import single_linked_list as sl

"""
new_map(num_elements, load_factor, prime=109345121)
Crea una nueva tabla de simbolos (map) sin elementos.

La tabla de simbolos es creada con los siguientes atributos:

prime: Número primo usado para calcular el hash. Inicializado con el valor de prime y en caso de no ser dado, con el valor por defecto de 109345121.

capacity: Tamaño de la tabla. Inicializado con el siguiente primo mayor a num_elements/ load_factor.

scale: Número entero aleatorio entre 1 y prime- 1.

shift: Número entero aleatorio entre 0 y prime- 1.

table: array_list de tamaño capacity inicializada con una single_linked_list en cada uno de elementos.

current_factor: Factor de carga actual de la tabla. Inicializado en 0.

limit_factor: Factor de carga límite de la tabla antes de hacer un rehash. Inicializado con el valor de load_factor.

size: Número de elementos en la tabla. Inicializado en 0.

Parameters
:
num_elements (int) – Número de elementos que se espera almacenar en la tabla.

load_factor (float) – Factor de carga límite de la tabla antes de hacer un rehash.

prime (int) – Número primo usado para calcular el hash. Por defecto es 109345121.

Returns
:
Tabla recien creada.

Return type
:
map_separate_chaining

"""

def new_map(num_elements, load_factor, prime=109345121):
    prime = prime
    capacity = mf.next_prime(num_elements // load_factor)
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)
    table = {
        'size': capacity,
        'elements': al.new_list()
    }
    for i in range(capacity):
        al.add_last(table, sl.new_list())
    current_factor = 0
    limit_factor = load_factor
    size = 0
    return {
        'prime': prime,
        'capacity': capacity,
        'scale': scale,
        'shift': shift,
        'table': table,
        'current_factor': current_factor,
        'limit_factor': limit_factor,
        'size': size
    }



def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1


"""
put(my_map, key, value)
Agrega una nueva entrada llave-valor a la tabla. Si la llave ya existe en la tabla, se actualiza el value de la entrada.

Para agregar una nueva entrada se debe seguir los siguientes pasos:

Calcular el hash de la llave, usando la función hash_value.

Se busca la lista en la posición del hash en la tabla.

Si la llave ya existe en la lista, se actualiza el valor de la entrada.

Si la llave no existe en la lista, se agrega una nueva entrada al final de la lista.

Se actualiza el current_factor de la tabla si se agrega una nueva entrada.

Si el current_factor supera el limit_factor, se realiza un rehash de la tabla.

Se retorna la tabla con la nueva entrada.

Parameters
:
my_map (map_separate_chaining) – Tabla de simbolos a la cual se desea agregar un nuevo elemento.

key (any) – Llave del nuevo elemento.

value (any) – Valor del nuevo elemento.

Returns
:
Tabla de simbolos con el nuevo elemento agregado.

Return type
:
map_separate_chaining

"""


"""

Realiza un rehashing de la tabla de simbolos.

Para realizar un rehash se debe seguir los siguientes pasos:

Crear una nueva tabla map_separate_chaining con capacity que sea el siguiente primo al doble del capacity actual.

Recorrer la tabla actual y reinsertar cada elemento en la nueva tabla.

Asignar la nueva tabla como la tabla actual.

Retornar la tabla nueva.

Parameters
:
my_map (map_separate_chaining) – Tabla de simbolos a la cual se le desea realizar un rehashing.

Returns
:
Tabla de simbolos con un nuevo tamaño.

Return type
:
map_separate_chaining

"""

def rehash(my_map):
    new_capacity = mf.next_prime(my_map["capacity"] * 2)
    new_table = {
        'size': new_capacity,
        'elements': []
    }
    for i in range(new_capacity):
        al.add_last(new_table, sl.new_list())

    for i in range(my_map["capacity"]):
        actual = al.get_element(my_map["table"], i)
        while sl.size(actual) > 0:
            entry = sl.remove_first(actual)
            hash_value = mf.hash_value(my_map, me.get_key(entry))
            al.add_last(al.get_element(new_table, hash_value), entry)

    my_map["table"] = new_table
    my_map["capacity"] = new_capacity
    my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    return my_map