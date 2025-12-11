"""
A simple counter script that prints numbers from 1 to 100.
"""

def main():
    i = 0  # Initialize the counter
    
    # Loop indefinitely until we manually break out
    while True:
        i += 1  # Increment counter
        print(i)
        
        # Stop the loop when the counter reaches 100
        if i == 100:
            break

if __name__ == "__main__":
    main()
