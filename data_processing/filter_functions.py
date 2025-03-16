def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 ==0]

def filter_odd_numbers(numbers):
    return [num for num in numbers if num % 2 !=0]

def filter_by_condition(data, condition):
    return [item for item in data if condition(item)]

def filter_unique_values(data):
    return list(set(data))

def filter_str_by_length(strings,min_length):
    return [s for s in strings if len(s) >= min_length]

