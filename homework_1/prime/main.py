def prime_count(number: int) -> int:
    if number <=2:
        return 0

    primes = [2]
    for candidate in range(3, number, 2):
        for devider in primes:
            if candidate%devider==0:
                break
        else:
            primes.append(candidate)
            
    return len(primes)


if __name__ == '__main__':
    from custom_tests import test
    
    test(prime_count)

