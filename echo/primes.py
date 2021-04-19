def is_prime(n):
    if n <= 1:
        return False
    elif n == 2: return True
    else:
        for div in range(2, n):
            if n % div == 0:
                return False
        else:
            return True

def primes_up_to(n):
    results = []
    for i in range(n+1):
        if is_prime(i):
            results.append(i)
    return results

if __name__ == "__main__":
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert primes_up_to(11) == [2, 3, 5, 7, 11]

