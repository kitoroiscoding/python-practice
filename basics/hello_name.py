"""
A simple input/output demonstration showing three ways to display
a user's name in a greeting message.
"""

def main():
    # Ask the user for their name
    name = input("Enter your name: ")

    print("Case 1:")
    # Using comma separation in print (adds a space automatically)
    print("Hello,", name)

    print("Case 2:")
    # Using string concatenation
    print("Hello, " + name)

    print("Case 3:")
    # Using an f-string (recommended modern approach)
    print(f"Hello, {name}")

if __name__ == "__main__":
    main()
