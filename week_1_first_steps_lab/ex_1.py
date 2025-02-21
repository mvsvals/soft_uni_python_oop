n = int(input())

def print_row(spaces, stars):
    print(" " * spaces + '* ' * stars)

def print_upper_part(n):
    for row in range(1, n + 1):
        print_row(n-row, row)

def print_bottom_part(n):
    for row in range(1, n):
        print_row(row, n- row)


def print_rhombus(size: int):
    print_upper_part(size)
    print_bottom_part(size)

print_rhombus(n)

