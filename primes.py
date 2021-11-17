
def isPrime(n):
    if n <=1:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def get_primes(n):
    result = []
    for i in range(2, n+1):
        if isPrime(i):
            result.append(i)
    print(result)
    return result

if __name__ == '__main__':
    assert [2, 3, 5, 7, 11] == sorted(get_primes(11))