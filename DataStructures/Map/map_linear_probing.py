import random
from DataStructures.Map import map_functions as mf
from DataStructures.List import array_list as al
from DataStructures.Map import map_entry as me



def new_map(num_elements, load_factor, prime=109345121):
    prime = prime
    capacity = mf.next_prime(num_elements // load_factor)
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)
    table = {
        'size': 0,
        'elements': []
    }
    for i in range(0,capacity):
        al.add_last(table, me.new_map_entry(None, None))
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


def put(my_map, key, value):
    hash_value = mf.hash_value(my_map, key)
    pos = find_slot(my_map, key, hash_value)
    if pos[0]:
        entry = al.get_element(my_map["table"], pos[1])
        me.set_value(entry, value)
    else:
        entry = me.new_map_entry(key, value)
        al.insert_element(my_map["table"], entry, pos[1])
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        if my_map["current_factor"] > my_map["limit_factor"]:
            my_map = rehash(my_map)
    return my_map


def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
               found = True
      elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail


def is_available(table, pos):
   entry = al.get_element(table, pos)
   if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == me.get_key(entry):
      return 0
   elif key > me.get_key(entry):
      return 1
   return -1

def contains(my_map, key):
   hash_value = mf.hash_value(my_map, key)
   pos = find_slot(my_map, key, hash_value)
   return pos[0]

def remove(my_map, key):
   hash_value = mf.hash_value(my_map, key)
   pos = find_slot(my_map, key, hash_value)
   if pos[0]:
      entry = al.get_element(my_map["table"], pos[1])
      me.set_key(entry, "__EMPTY__")
      me.set_value(entry, None)
      my_map["size"] -= 1
      
   return my_map

def get(my_map, key):
   hash_value = mf.hash_value(my_map, key)
   pos = find_slot(my_map, key, hash_value)
   if pos[0]:
      entry = al.get_element(my_map["table"], pos[1])
      return me.get_value(entry)
   return None


def size(my_map):
   return my_map["size"]

def is_empty(my_map):
   return my_map["size"] == 0

def key_set(my_map):
   key_set = al.new_list()
   for entry in my_map["table"]["elements"]:
      if me.get_key(entry) is not None and me.get_key(entry) != "__EMPTY__":
         al.add_last(key_set, me.get_key(entry))
   return key_set

def value_set(my_map):
   value_set = al.new_list()
   for entry in my_map["table"]["elements"]:
      if me.get_key(entry) is not None and me.get_key(entry) != "__EMPTY__":
         al.add_last(value_set, me.get_value(entry))
   return value_set


def rehash(my_map):
   new_capacity = mf.next_prime(my_map["capacity"] * 2)
   new_table = {
      'size': 0,
      'elements': []
   }
   
   
   
   for i in range(new_capacity):
        al.add_last(new_table, me.new_map_entry(None, None))

   for entry in my_map["table"]["elements"]:
        if me.get_key(entry) is not None and me.get_key(entry) != "__EMPTY__":
             hash_value = mf.hash_value(my_map, me.get_key(entry))
             pos = find_slot(my_map, me.get_key(entry), hash_value)
             new_table["elements"][pos[1]] = entry

   my_map["table"] = new_table
   my_map["capacity"] = new_capacity
   

   return my_map
