def new_list():
    
    my_list = {"elements":[],"size":0}
    
    return my_list

def add_last(my_list,elemento):
    
    my_list["elements"].append(elemento)
    
    my_list["size"] += 1
    
    return my_list

def add_first(my_list,elemento):
    
    nueva_lista = [elemento]
    
    for x in my_list["elements"]:
        
        nueva_lista.append(x)
        
    my_list["elements"] = nueva_lista
    
    return my_list


def size(my_list): 

    return my_list["size"]


def is_empty(my_list):
    
    if my_list["size"] == 0:
        
        return True
    
    return False


def is_present(my_list,elemento_a_buscar,default_function):
    
    if my_list["size"] == 0:
       
       return -1
   
    else:
        
        encontro = False
        
        i = 0
        
        while i < my_list["size"] and encontro == False:
            
            elemento_en_posicion_i_de_lista = my_list["elements"][i]
            
            comparador = default_function(elemento_a_buscar,elemento_en_posicion_i_de_lista)
            
            if comparador == 0:
                
                encontro = True

                return i
                
            i += 1
        
        return -1
            
            
def get_element(my_list,pos):
    
    if pos < 0 or pos >= my_list["size"]:
        
        raise Exception('IndexError: list index out of range')
    
    return my_list["elements"][pos]

def first_element(my_list):
    
    if my_list["size"] == 0:
        
        raise Exception('IndexError: list index out of range')
    
    return my_list["elements"][0]

def last_element(my_list):
    
    if my_list["size"] == 0:
        
        raise Exception('IndexError: list index out of range')
    
    return my_list["elements"][my_list["size"] - 1]


def delete_element(my_list,pos):
    
    if pos < 0 or pos >= my_list["size"]:
        
        raise Exception('IndexError: list index out of range')
    
    nueva_lista = []
    
    for i in range(my_list["size"]):
        
        if i != pos:
            
            nueva_lista.append(my_list["elements"][i])
            
    my_list["elements"] = nueva_lista
    
    my_list["size"] -= 1
    
    return my_list



def remove_first(my_list):
    
    if my_list["size"] == 0:
        
        raise Exception('IndexError: list index out of range')
    
    nueva_lista = []

    temp = my_list["elements"][0]
    
    for i in range(1,my_list["size"]):
        
        nueva_lista.append(my_list["elements"][i])
        
    my_list["elements"] = nueva_lista
    
    my_list["size"] -= 1
    
    return temp


def remove_last(my_list):
    
    if my_list["size"] == 0:
        
        raise Exception('IndexError: list index out of range')
    
    nueva_lista = []

    temp = my_list["elements"][my_list["size"] - 1]
    
    for i in range(my_list["size"] - 1):
        
        nueva_lista.append(my_list["elements"][i])
        
    my_list["elements"] = nueva_lista
    
    my_list["size"] -= 1
    
    return temp
                
   
def insert_element(my_list,elemento,pos):
    
    if pos < 0 or pos > my_list["size"]:
        
        raise Exception('IndexError: list index out of range')
    
    nueva_lista = []
    
    for i in range(0,my_list["size"]):
        
        if i == pos:
            
            nueva_lista.append(elemento)
            
        nueva_lista.append(my_list["elements"][i])
        
    my_list["elements"] = nueva_lista
    
    my_list["size"] += 1
    
    return my_list

def change_info(my_list,pos,nueva_info):
    
    if pos < 0 or pos >= my_list["size"]:
        
        raise Exception('IndexError: list index out of range')
    
    my_list["elements"][pos] = nueva_info
    
    return my_list


def default_function(x_1,x_2):
    
    if x_1 > x_2: 
        
        return 1
    
    elif x_1 < x_2: 
        
        return -1
    
    else: 
        
        return 0
    
def exchange(my_list, pos_1, pos_2):
    
    if pos_1 < 0 or pos_1 >= my_list["size"] or pos_2 < 0 or pos_2 >= my_list["size"]:
        
        raise Exception('IndexError: list index out of range')
    
    temp = my_list["elements"][pos_1]
    
    my_list["elements"][pos_1] = my_list["elements"][pos_2]
    
    my_list["elements"][pos_2] = temp
    
    return my_list

def sub_list(my_list, pos_i, num_elements):

    if pos_i < 0 or pos_i >= my_list["size"] or num_elements < 0 or pos_i + num_elements > my_list["size"]:
        
        raise Exception('IndexError: list index out of range')
    
    nueva_lista = []
    
    for i in range(pos_i, pos_i + num_elements):
        
        nueva_lista.append(my_list["elements"][i])
        
    return {"elements":nueva_lista,"size":num_elements}


def default_sort_criteria(element_1, element_2):
    """
    Función de comparación por defecto para ordenar elementos.
    
    Parameters:
        element_1 (any): Primer elemento a comparar.
        element_2 (any): Segundo elemento a comparar.
    
    Returns:
        bool: True si el primer elemento es menor que el segundo, False en caso contrario.
    """
    return element_1 < element_2


        
def selection_sort(my_list, sort_crit=default_sort_criteria):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento Selection Sort.
    
    Parameters:
        my_list (dict): Lista a ordenar (debe contener las claves "elements" y "size").
        sort_crit (function): Función de comparación.
    
    Returns:
        dict: Lista ordenada.
    """
    my_list_copy = my_list["elements"]

    n = len(my_list_copy)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if sort_crit(my_list_copy[j], my_list_copy[min_idx]):
                min_idx = j
        my_list_copy[i], my_list_copy[min_idx] = my_list_copy[min_idx], my_list_copy[i]

    
    my_list["elements"] = my_list_copy
    my_list["size"] = len(my_list_copy)  

    return my_list

def insertion_sort(my_list, sort_crit=default_sort_criteria):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento Insertion Sort.
    
    Parameters:
        my_list (dict): Lista a ordenar (debe contener las claves "elements" y "size").
        sort_crit (function): Función de comparación.
    
    Returns:
        dict: Lista ordenada.
    """
    my_list_copy = my_list["elements"]

    for i in range(1, len(my_list_copy)):
        key = my_list_copy[i]
        j = i - 1
        while j >= 0 and sort_crit(key, my_list_copy[j]):
            my_list_copy[j + 1] = my_list_copy[j]
            j -= 1
        my_list_copy[j + 1] = key

    
    my_list["elements"] = my_list_copy
    my_list["size"] = len(my_list_copy)  

    return my_list


def shell_sort(my_list, sort_crit=default_sort_criteria):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento Shell Sort.
    
    Parameters:
        my_list (dict): Lista a ordenar (debe contener las claves "elements" y "size").
        sort_crit (function): Función de comparación.
    
    Returns:
        dict: Lista ordenada.
    """
    my_list_copy = my_list["elements"]

    n = len(my_list_copy)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = my_list_copy[i]
            j = i
            while j >= gap and sort_crit(temp, my_list_copy[j - gap]):
                my_list_copy[j] = my_list_copy[j - gap]
                j -= gap
            my_list_copy[j] = temp
        gap //= 2

    
    my_list["elements"] = my_list_copy
    my_list["size"] = len(my_list_copy)  

    return my_list

def merge_sort(my_list, sort_crit=default_sort_criteria):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento Merge Sort.
    
    Parameters:
        my_list (dict): Lista a ordenar (debe contener las claves "elements" y "size").
        sort_crit (function): Función de comparación.
    
    Returns:
        dict: Lista ordenada.
    """
    my_list_copy = my_list["elements"]

    def _merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = _merge_sort(arr[:mid])
        right_half = _merge_sort(arr[mid:])

        return _merge(left_half, right_half, sort_crit)

    def _merge(left, right, sort_crit):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if sort_crit(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    
    my_list["elements"] = _merge_sort(my_list_copy)
    my_list["size"] = len(my_list["elements"]) 

    return my_list


def quick_sort(my_list, sort_crit=default_sort_criteria):
    """
    Ordena una lista utilizando el algoritmo de ordenamiento Quick Sort.
    
    Parameters:
        my_list (dict): Lista a ordenar (debe contener las claves "elements" y "size").
        sort_crit (function): Función de comparación.
    
    Returns:
        dict: Lista ordenada.
    """
    my_list_copy = my_list["elements"]

    def _quick_sort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if sort_crit(x, pivot)]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if not sort_crit(x, pivot) and x != pivot]

        return _quick_sort(left) + middle + _quick_sort(right)

    # Ordenar y actualizar la lista
    my_list["elements"] = _quick_sort(my_list_copy)
    my_list["size"] = len(my_list["elements"])  # Actualizar el tamaño

    return my_list