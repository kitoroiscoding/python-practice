"""
Prints a 3×3 grid of stars using three different loop structures.
Demonstrates variations of nested loops for educational purposes.
"""

print("Case 1: Simple nested loops with string literals")
for a in "***":         # Loop 3 times through the characters of this string
    for b in "*":       # Always a single '*', so this loops once
        for c in "*":   # Same as above
            print(a, b, c)


print("\nCase 2: Using predefined variables for clarity")
stars_x = "***"         # Three iterations
stars_y = "*"           # One iteration
stars_z = "*"           # One iteration

for a in stars_x:
    for b in stars_y:
        for c in stars_z:
            print(a, b, c)


print("\nCase 3: Using string multiplication to control repetition")
single_star = "*"

for a in single_star * 3:   # Equivalent to "***"
    for b in single_star:   # One iteration
        for c in single_star:
            print(a, b, c)
