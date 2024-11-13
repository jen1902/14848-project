

# Example 3: Function with high complexity (Code Smell)
def process_data(data):
    if data == 1:
        result = "Data is one"
    elif data == 2:
        result = "Data is two"
    elif data == 3:
        result = "Data is three"
    elif data == 4:
        result = "Data is four"
    elif data == 5:
        result = "Data is five"
    elif data == 6:
        result = "Data is six"
    elif data == 7:
        result = "Data is seven"
    else:
        result = "Unknown data"
    print(result)

# Example 4: Resource leak (Security/Resource management issue)
def read_file():
    file = open("example.txt", "r")  # No 'with' statement; file might not close if an error occurs
    content = file.read()
    print(content)
    # File not closed explicitly

# Example 5: Empty exception block (Bad practice)
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        pass  # Swallowing the exception
    return result

