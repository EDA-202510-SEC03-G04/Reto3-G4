def new_map():
    return {"root": None}


def put(my_bst, key, value):
    if "root" not in my_bst:  
        my_bst["root"] = None
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst 
 
        
def insert_node(root, key, value):
    
    
    if root is None:
            return {
                "key": key,
                "value": value,
                "size": 1,
                "left": None,
                "right": None
            }
            
    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
        root["size"] = 1 + size(root["left"]) + size(root["right"]) 

    return root  


def size_node(node):
    
    if node is None:
        return 0
    
    return node["size"]  
        
def size(my_bst):
   
    return size_node(my_bst["root"])      



def get(my_bst, key):
    
    node = get_node(my_bst["root"], key)   
    if node is None:
        return None
    return node["value"]     



def get_node(root, key):
    
    if root is None:
        return None
    
    if key < root["key"]:
        return get_node(root["left"], key)
    elif key > root["key"]:
        return get_node(root["right"], key)
    else:
        return root
    
    
def remove(my_bst, key):
    
    my_bst["root"] = remove_node(my_bst["root"], key)
    return my_bst

def remove_node(root, key):
    if root is None:
        return None
    
    if key < root["key"]:
        root["left"] = remove_node(root["left"], key)
    elif key > root["key"]:
        root["right"] = remove_node(root["right"], key)
    else:
        if root["left"] is None:
            return root["right"]
        elif root["right"] is None:
            return root["left"]
        
        min_node = get_min_node(root["right"])
        root["key"] = min_node["key"]
        root["value"] = min_node["value"]
        root["right"] = remove_node(root["right"], min_node["key"])
    
    return root

def get_min(my_bst):
    min_node = get_min_node(my_bst["root"])
    return min_node["value"] if min_node else None


def get_min_node(root):
    if root is None:
        return None
    
    while root["left"] is not None:
        root = root["left"]
    
    return root    


def contains(my_bst, key):
    
    return get_node(my_bst["root"], key) is not None

def size_tree(root):
    return size_node(root)
    

def is_empty(my_bst):
    
    return my_bst["root"] is None


def key_set(my_bst):
    keys_list = []
    collect_keys(my_bst["root"], keys_list)
    return set(keys_list)

def collect_keys(root, keys_list):
    if root is not None:
        collect_keys(root["left"], keys_list)
        keys_list.append(root["key"])
        collect_keys(root["right"], keys_list)


def value_set(my_bst):
    values_list = []
    collect_values(my_bst["root"], values_list)
    return set(values_list)

def collect_values(root, values_list):
    if root is not None:
        collect_values(root["left"], values_list)
        values_list.append(root["value"])
        collect_values(root["right"], values_list)

def get_max(my_bst):
    max_node = get_max_node(my_bst["root"])
    return max_node["value"] if max_node else None

def get_max_node(root):
    if root is None:
        return None
    while root["right"] is not None:
        root = root["right"]
    return root



def delete_min(my_bst):
    my_bst["root"] = delete_min_tree(my_bst["root"])
    return my_bst

def delete_min_tree(root):
    if root is None:
        return None
    if root["left"] is None:  
        return root["right"]  
    root["left"] = delete_min_tree(root["left"])  
    root["size"] = 1 + size_node(root["left"]) + size_node(root["right"])
    return root

def delete_max(my_bst):
    my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst

def delete_max_tree(root):
    if root is None:
        return None
    
    if root["right"] is None:  
        return root["left"]  
    
    root["right"] = delete_max_tree(root["right"])  
    root["size"] = 1 + size_node(root["left"]) + size_node(root["right"])  
    
    return root

def floor(my_bst, key):
    node = floor_key(my_bst["root"], key)
    return node["value"] if node else None

def floor_key(root, key):
    if root is None:
        return None
    
    if root["key"] == key:  
        return root
    elif root["key"] > key:  
        return floor_key(root["left"], key)
    
    derecha = floor_key(root["right"], key)  
    return derecha if derecha else root  


def ceiling(my_bst, key):
    node = ceiling_key(my_bst["root"], key)
    return node["value"] if node else None

def ceiling_key(root, key):
    if root is None:
        return None
    
    if root["key"] == key:  
        return root
    elif root["key"] < key:  
        return ceiling_key(root["right"], key)
    
    izq = ceiling_key(root["left"], key)  
    return izq if izq else root  


def select(my_bst, pos):
    node = select_key(my_bst["root"], pos)
    return node["value"] if node else None

def select_key(root, key):
    if root is None:
        return None

    left_size = size_node(root["left"]) 

    if left_size > k:  
        return select_key(root["left"], key)
    elif left_size < k:  # Si k está en la derech entonces la idea es que ajustamos k y buscamos
        return select_key(root["right"], key - left_size - 1)
    else:  
        return root


def rank(my_bst, key):
    return rank_keys(my_bst["root"], key)

def rank_keys(root, key):
    if root is None:
        return 0

    if key < root["key"]:  
        return rank_keys(root["left"], key)
    elif key > root["key"]:  
        return 1 + size_node(root["left"]) + rank_keys(root["right"], key)
    else:  
        return size_node(root["left"])


def height(my_bst):
    return height_tree(my_bst["root"])

def height_tree(root):
    if root is None:
        return -1  
    return 1 + max(height_tree(root["left"]), height_tree(root["right"]))


def keys(my_bst, key_initial, key_final):
    keys_list = []
    keys_range(my_bst["root"], keys_list, key_initial, key_final)
    return keys_list

def keys_range(root, key_initial, key_final, list_key):
    if root is None:
        return
    
    if key_initial < root["key"]:  
        keys_range(root["left"], key_initial, key_final, list_key)
    
    if key_initial <= root["key"] <= key_final:  
        list_key.append(root["key"])
    
    if key_final > root["key"]:  
        keys_range(root["right"], key_initial, key_final, list_key)



def values(my_bst, key_initial, key_final):
    values_list = []
    values_range(my_bst["root"], values_list, key_initial, key_final)
    return values_list

def values_range(root, key_initial, key_final, list_value):
    if root is None:
        return
    
    if key_initial < root["key"]: 
        values_range(root["left"], key_initial, key_final, list_value)
    
    if key_initial <= root["key"] <= key_final:  
        list_value.append(root["value"])
    
    if key_final > root["key"]:  
        values_range(root["right"], key_initial, key_final, list_value)


def default_compare(key, element):
    if key < element:
        return -1
    elif key > element:
        return 1
    else:
        return 0

