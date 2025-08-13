
def prime_multiples1():
    n, k = map(int, input().split())
    primes = list(map(int, input().split()))
    data = set()

    for i in primes:
        count = i
        while count <= n:
            data.add(count)
            count += i
    print(len(data))