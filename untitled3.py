def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    if pow(sq, 0.5) % 1 == 0:
        a = pow(sq, 0.5)
        x = a+1
        return x**2
    else:
        return -1


print(find_next_square(121))