"""
A demonstration of how variables work in Python.
Shows storing different data types, performing operations,
reading user input, and understanding variable reassignment.
"""

def main():
    # Storing a simple string in a variable
    variable_name = "Value"
    print(variable_name)

    # You can store integers and perform arithmetic operations
    a = 3
    b = 5
    print(a + b)  # Adding two integers

    # You can store strings and print them together
    string1 = "Hello"
    string2 = "World"
    print(string1, string2)  # Print two strings with a space between

    # Reading user input and storing it in a variable
    inp = input("Write something: ")
    print(inp)

    # --- Additional basic examples ---

    # Storing a floating-point number
    pi_value = 3.14
    print("Pi value:", pi_value)

    # Storing a boolean
    is_active = True
    print("Active status:", is_active)

    # Using a list to store multiple values
    numbers = [1, 2, 3, 4]
    print("List of numbers:", numbers)

    # Using a dictionary to store key–value pairs
    student = {"name": "Alice", "age": 20}
    print("Student data:", student)

    # Variables hold temporary values and can be reassigned at any time
    x = "I am the first value of x"
    x = "I am the second value of x"  # Overwriting the previous value
    print(x)

if __name__ == "__main__":
    main()
