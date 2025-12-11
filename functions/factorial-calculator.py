def factorial_iterative(n: int) -> int:
    """
    Calculate the factorial of a given non-negative integer using an iterative approach.

    Parameters:
        n (int): The number to compute the factorial of. Must be >= 0.

    Returns:
        int: The factorial of n.
    """
    result = 1

    # Multiply result by each integer from 2 up to n.
    for i in range(2, n + 1):
        result *= i
    
    return result


def main():
    """
    Main loop of the program.
    Continuously asks the user for a number and prints its factorial.
    Typing 'exit' stops the program.
    """

    print("Factorial Calculator — type 'exit' to stop.\n")

    while True:
        inp = input("Enter a number: ").strip()

        # Allow user to quit the program
        if inp.lower() == "exit":
            print("Program stopped. Thank you for using Factorial Calculator.")
            break

        # Validate input: ensure it's made of digits only
        # .isdigit() prevents converting invalid input (like letters) to int
        if not inp.isdigit():
            print("Invalid input. Please enter a valid non-negative number.\n")
            continue

        num = int(inp)

        print(f"Factorial of {num} is: {factorial_iterative(num)}\n")


# Standard Python execution guard:
# Ensures main() runs only when the file is executed directly.
if __name__ == "__main__":
    main()
