import random

def is_probable_prime(n, k=5):
    """
    Determines whether a number is probably prime using Fermat's primality test.

    Parameters:
    n (int): The number to test.
    k (int): Number of test rounds. More rounds = higher accuracy.

    Returns:
    str: A message indicating whether n is probably prime or not.
    """

    # Handle very small numbers separately
    if n == 2 or n == 3:
        return f"{n} is a prime number"

    # Any number less than or equal to 1 is not prime
    if n <= 1:
        return f"{n} is not a prime number"

    # Repeat Fermat's test k times for better reliability
    for _ in range(k):
        # Choose a random base 'a' between 2 and n-2
        # This 'a' will be used in Fermat's primality test
        a = random.randint(2, n - 2) # For n >= 4, this range is valid.

        # Fermat's Little Theorem states:
        # If n is prime, then (a^(n-1) % n) should equal 1.
        # If it does NOT equal 1 even once, n is definitely NOT prime.
        if pow(a, n - 1, n) != 1:
            return f"{n} is not a prime number"

    # If the number passed all k tests,
    # it is *probably* prime (not guaranteed, but very likely)
    return f"{n} is probably a prime number"


def main():
    # Introduction text printed once at program start
    print("Prime Checker — type 'exit' to stop.\n")

    while True:
        # Ask user for input
        inp = input("Enter a number: ").strip()

        # If the user types 'exit', end the program gracefully
        if inp.lower() == "exit":
            print("Program stopped. Thank you for using Prime Checker.")
            break

        # Check if the input contains only digits
        # .isdigit() prevents errors that would crash the program
        if not inp.isdigit():
            print("Invalid input. Please enter a valid number.\n")
            continue

        # Convert valid user input into an integer
        num = int(inp)

        # Call the primality test function and display the result
        print(is_probable_prime(num), "\n")


# Standard Python boilerplate:
# This ensures main() only runs when the file is executed directly
if __name__ == "__main__":
    main()


"""
----------------------------------------------
 Explanation of Fermat's Primality Test
----------------------------------------------

Fermat's Little Theorem:
------------------------
If 'n' is a prime number and 'a' is any number such that:
    1 < a < n

Then the following must be true:
    a^(n - 1) % n == 1

What this means:
----------------
For prime numbers, raising 'a' to the (n - 1) power and 
taking the remainder when divided by n will always give 1.

So we test this:
1. Pick a random 'a' between 2 and n-2
2. Compute a^(n-1) % n
3. If the result is NOT 1 → n is definitely NOT prime
4. If the result IS 1 → n *might* be prime

Why "probably" prime?
---------------------
Some rare composite numbers (called *Carmichael numbers*)
can pass Fermat's test even though they are not prime.

Repeating the test multiple times with different 'a' values
reduces the chance of being fooled.

Summary:
--------
- If Fermat's test fails → n is definitely not prime
- If Fermat's test passes multiple times → n is probably prime

This script repeats the test several times (k = 5 by default)
to increase the accuracy and reliability.
"""
