def is_integer(value):

    return isinstance(value, int)

def is_float(value):
  
    return isinstance(value, float)

def is_string(value):
   
    return isinstance(value, str)

def is_non_empty_string(value):
   
    return isinstance(value, str) and bool(value.strip())

def is_in_range(value, min_value, max_value):
    return isinstance(value, (int,float)) and min_value <= value <= max_value
