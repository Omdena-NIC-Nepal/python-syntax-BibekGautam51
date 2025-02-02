def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    formatted_string = f"my name is {name} and i am {age} years old."
    return formatted_string

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return f"the number {number} is greater than 10"
    elif number < 10:
        return f"The number {number} is less than 10"
    else:
        return f"The number {number} is equal to 10"

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum=0
    for i in range(n+1):
        sum = sum + i
    return f"The sum of numbers from 1 to {n} is: {sum}"

def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    sum1= sum(numbers)
    max1 = max(numbers)
    min1 = min(numbers)
    tuple =(sum1, max1, min1)
    return tuple


def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    #list comprehension technique
    list =[key for key,value in students_dict.items() if value > 80] 
    return list

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    common_elements = list1.intersection(list2)
    return common_elements

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
        "quotient": a / b if b != 0 else "cannot calculate"
    }

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    return {
        "and": x and y,
        "or": x or y,
        "not_x": not x
    }

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {
        "and": a & b,
        "or": a | b,
        "xor": a ^ b
    }