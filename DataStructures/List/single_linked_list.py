def new_list():
    return {"first": None, "last": None, "size": 0}

def is_empty(my_list):
    return my_list["size"] == 0

def size(my_list):
    return my_list["size"]

def add_first(my_list, elemento):
    my_node = {"info": elemento, "next": my_list["first"]}
    if my_list["size"] == 0:
        my_list["last"] = my_node
    my_list["first"] = my_node
    my_list["size"] += 1

def add_last(my_list, elemento):
    my_node = {"info": elemento, "next": None}
    if my_list["size"] == 0:
        my_list["first"] = my_node
    else:
        my_list["last"]["next"] = my_node
    my_list["last"] = my_node
    my_list["size"] += 1

def first_element(my_list):
    if my_list["size"] == 0:
        raise Exception("IndexError: list index out of range")
    return my_list["first"]["info"]

def last_element(my_list):
    if my_list["size"] == 0:
        raise Exception("IndexError: list index out of range")
    return my_list["last"]["info"]

def get_element(my_list, index):
    if index < 0 or index >= my_list["size"]:
        raise Exception("IndexError: list index out of range")
    actual = my_list["first"]
    for _ in range(index):
        actual = actual["next"]
    return actual["info"]

def delete_element(my_list, index):
    if index < 0 or index >= my_list["size"]:
        raise Exception("IndexError: list index out of range")
    if index == 0:
        remove_first(my_list)
        return my_list
    actual = my_list["first"]
    for _ in range(index - 1):
        actual = actual["next"]
    removed = actual["next"]
    actual["next"] = removed["next"]
    if removed == my_list["last"]:
        my_list["last"] = actual
    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    if my_list["size"] == 0:
        raise Exception("IndexError: list index out of range")
    temp = my_list["first"]
    my_list["first"] = temp["next"]
    my_list["size"] -= 1
    return temp["info"]

def remove_last(my_list):
    if my_list["size"] == 0:
        raise Exception("IndexError: list index out of range")
    
    last_info = my_list["last"]["info"]  # Guardamos el valor antes de eliminarlo
    delete_element(my_list, my_list["size"] - 1)  # Eliminamos el último nodo
    return last_info  # Retornamos la información eliminada


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


def default_function(x_1,x_2):
    
    if x_1 > x_2: #caso_1 (mayor que) 
        return 1
    
    elif x_1 < x_2: #caso_2 (menor que)  
        return -1
    
    else: #caso_3 (iguales) 
        return 0
    


def insert_element(my_list, elemento, index):
    if index < 0 or index > my_list["size"]:
        raise Exception("IndexError: list index out of range")
    if index == 0:
        add_first(my_list, elemento)
        return my_list
    elif index == my_list["size"]:
        add_last(my_list, elemento)
        return my_list
    else:
        my_node = {"info": elemento, "next": None}
        actual = my_list["first"]
        for _ in range(index - 1):
            actual = actual["next"]
        my_node["next"] = actual["next"]
        actual["next"] = my_node
        my_list["size"] += 1
        return my_list


def is_present(my_list, elemento, default_function):
    actual = my_list["first"]
    index = 0
    while actual is not None:
        if default_function(actual["info"], elemento) == 0:
            return index
        actual = actual["next"]
        index += 1
    return -1

def change_info(my_list, index, elemento):
    if index < 0 or index >= my_list["size"]:
        raise Exception("IndexError: list index out of range")
    actual = my_list["first"]
    for _ in range(index):
        actual = actual["next"]
    actual["info"] = elemento
    return my_list

def exchange(my_list, index1, index2):
    if index1 < 0 or index1 >= my_list["size"] or index2 < 0 or index2 >= my_list["size"]:
        raise Exception("IndexError: list index out of range")
    if index1 == index2:
        return my_list
    actual1, actual2 = my_list["first"], my_list["first"]
    for _ in range(index1):
        actual1 = actual1["next"]
    for _ in range(index2):
        actual2 = actual2["next"]
    actual1["info"], actual2["info"] = actual2["info"], actual1["info"]
    return my_list

def sub_list(my_list, pos, num_elements):

    if pos == 0 and num_elements == 0:
        return new_list()

    if pos < 0 or num_elements <= 0 or pos >= my_list["size"] or pos + num_elements > my_list["size"]:
        raise Exception("IndexError: list index out of range")
    
    new_sub_list = new_list()
    actual = my_list["first"]
    
    # Avanzar hasta la posición de inicio
    for _ in range(pos):
        actual = actual["next"]
    
    # Copiar los elementos a la nueva lista
    for _ in range(num_elements):
        add_last(new_sub_list, actual["info"])
        actual = actual["next"]
    
    return new_sub_list


def selection_sort(my_list, sort_crit=default_function):
    """
    Ordena una lista enlazada simple utilizando el algoritmo de Selection Sort.
    
    Parameters:
        my_list (dict): Lista enlazada simple (debe contener "first", "last" y "size").
        sort_crit (function): Función de comparación (por defecto, default_function).
    
    Returns:
        dict: Lista ordenada.
    """
    if my_list["size"] <= 1:
        return my_list

    current = my_list["first"]
    while current is not None:
        min_node = current
        next_node = current["next"]
        while next_node is not None:
            if sort_crit(next_node["info"], min_node["info"]) == -1:
                min_node = next_node
            next_node = next_node["next"]
        # Intercambiar los valores de los nodos
        current["info"], min_node["info"] = min_node["info"], current["info"]
        current = current["next"]

    return my_list

def insertion_sort(my_list, sort_crit=default_function):
    """
    Ordena una lista enlazada simple utilizando el algoritmo de Insertion Sort.
    
    Parameters:
        my_list (dict): Lista enlazada simple (debe contener "first", "last" y "size").
        sort_crit (function): Función de comparación (por defecto, default_function).
    
    Returns:
        dict: Lista ordenada.
    """
    if my_list["size"] <= 1:
        return my_list

    sorted_list = new_list()
    current = my_list["first"]

    while current is not None:
        next_node = current["next"]
        if sorted_list["size"] == 0:
            add_first(sorted_list, current["info"])
        else:
            actual = sorted_list["first"]
            prev = None
            while actual is not None and sort_crit(actual["info"], current["info"]) == -1:
                prev = actual
                actual = actual["next"]
            if prev is None:
                add_first(sorted_list, current["info"])
            else:
                new_node = {"info": current["info"], "next": actual}
                prev["next"] = new_node
                sorted_list["size"] += 1
        current = next_node

    my_list["first"] = sorted_list["first"]
    my_list["last"] = sorted_list["last"]
    my_list["size"] = sorted_list["size"]

    return my_list


def shell_sort(my_list, sort_crit=default_function):
    """
    Ordena una lista enlazada simple utilizando el algoritmo de Shell Sort.
    
    Parameters:
        my_list (dict): Lista enlazada simple (debe contener "first", "last" y "size").
        sort_crit (function): Función de comparación (por defecto, default_function).
    
    Returns:
        dict: Lista ordenada.
    """
    if my_list["size"] <= 1:
        return my_list

    # Convertir la lista enlazada en una lista de Python para facilitar el acceso por índices
    elements = []
    current = my_list["first"]
    while current is not None:
        elements.append(current["info"])
        current = current["next"]

    n = len(elements)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = elements[i]
            j = i
            while j >= gap and sort_crit(elements[j - gap], temp) == 1:
                elements[j] = elements[j - gap]
                j -= gap
            elements[j] = temp
        gap //= 2

    # Actualizar la lista enlazada con los elementos ordenados
    current = my_list["first"]
    for element in elements:
        current["info"] = element
        current = current["next"]

    return my_list


def merge_sort(my_list, sort_crit=default_function):
    """
    Ordena una lista enlazada simple utilizando el algoritmo de Merge Sort.
    
    Parameters:
        my_list (dict): Lista enlazada simple (debe contener "first", "last" y "size").
        sort_crit (function): Función de comparación (por defecto, default_function).
    
    Returns:
        dict: Lista ordenada.
    """
    if my_list["size"] <= 1:
        return my_list

    # Función auxiliar para dividir la lista en dos mitades
    def split_list(head):
        slow = head
        fast = head["next"]
        while fast is not None and fast["next"] is not None:
            slow = slow["next"]
            fast = fast["next"]["next"]
        mid = slow["next"]
        slow["next"] = None
        return head, mid

    # Función auxiliar para mezclar dos listas ordenadas
    def merge(left, right):
        dummy = {"info": None, "next": None}
        tail = dummy

        while left is not None and right is not None:
            if sort_crit(left["info"], right["info"]) == -1:
                tail["next"] = left
                left = left["next"]
            else:
                tail["next"] = right
                right = right["next"]
            tail = tail["next"]

        if left is not None:
            tail["next"] = left
        if right is not None:
            tail["next"] = right

        return dummy["next"]

    # Función recursiva para Merge Sort
    def _merge_sort(head):
        if head is None or head["next"] is None:
            return head

        left, right = split_list(head)
        left = _merge_sort(left)
        right = _merge_sort(right)
        return merge(left, right)

    # Ordenar la lista
    my_list["first"] = _merge_sort(my_list["first"])

    # Actualizar el último nodo
    current = my_list["first"]
    while current["next"] is not None:
        current = current["next"]
    my_list["last"] = current

    return my_list


def quick_sort(my_list, sort_crit=default_function):
    """
    Ordena una lista enlazada simple utilizando el algoritmo de Quick Sort.
    
    Parameters:
        my_list (dict): Lista enlazada simple (debe contener "first", "last" y "size").
        sort_crit (function): Función de comparación (por defecto, default_function).
    
    Returns:
        dict: Lista ordenada.
    """
    if my_list["size"] <= 1:
        return my_list

    # Función auxiliar para obtener el último nodo
    def get_tail(head):
        while head is not None and head["next"] is not None:
            head = head["next"]
        return head

    # Función auxiliar para particionar la lista
    def partition(head, tail):
        pivot = tail["info"]
        prev = None
        current = head
        new_head = head

        while current != tail:
            if sort_crit(current["info"], pivot) == -1:
                if new_head == current:
                    new_head = current["next"]
                if prev is not None:
                    prev["next"] = current["next"]
                temp = current["next"]
                current["next"] = None
                tail["next"] = current
                tail = current
                current = temp
            else:
                prev = current
                current = current["next"]

        return new_head, tail

    # Función recursiva para Quick Sort
    def _quick_sort(head, tail):
        if head is None or head == tail:
            return head

        new_head, pivot = partition(head, tail)
        if new_head != pivot:
            temp = new_head
            while temp["next"] != pivot:
                temp = temp["next"]
            temp["next"] = None
            new_head = _quick_sort(new_head, temp)
            temp = get_tail(new_head)
            temp["next"] = pivot

        pivot["next"] = _quick_sort(pivot["next"], tail)
        return new_head

    # Ordenar la lista
    my_list["first"] = _quick_sort(my_list["first"], my_list["last"])

    # Actualizar el último nodo
    current = my_list["first"]
    while current["next"] is not None:
        current = current["next"]
    my_list["last"] = current

    return my_list