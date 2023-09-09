# Print the 10 first square number, one per line.
# Start at 0, so the first square number is 02, followed by 12, 22, and so on up to 92.

def print_square_numbers(limit):
    for i in range(0, limit):
        print(i ** 2)
    
print_square_numbers(10)