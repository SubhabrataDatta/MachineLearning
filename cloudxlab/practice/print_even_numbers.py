def print_even(n):
    for number in range(0,n):
        if(number%2==0):
            print("{0}".format(number))
    return None

print_even(10)