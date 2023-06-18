from cs50 import get_int

# Accepting the appropriate value
while True:
    height = get_int("Height: ")
    if height > 0 and height <= 8:
        break

j = height
for i in range(height):
    print(" "*(j-1) + "#"*(i+1))
    j -= 1   # Decrementing j on every iteration
