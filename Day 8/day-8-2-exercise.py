# prime number
def prime_number(n):
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
    if is_prime:
        print(f"{n} is a prime")
    else:
        print(f"{n} is not a prime number")


prime_number(8)
prime_number(11)