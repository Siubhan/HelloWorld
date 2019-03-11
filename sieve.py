def sieveMeth(n):
    sieveList = [i for i in range(2, n + 1)]
    listPrime = []
    for i in range(n - 2):
        if sieveList[i]:
            for candidate in range(sieveList[i] * sieveList[i], n, sieveList[i]):
                sieveList[candidate - 2] = 0
    for i in range(n - 2):
        if sieveList[i]:
            listPrime.append(sieveList[i])
    del sieveList
    return listPrime


def primeDivisors(n, listPrimes):
    if not primeDivisors.list:
        primeDivisors.list = [0] * primeDivisors.N
    buffer = []
    for i in range(len(listPrimes)):
        if n % listPrimes[i] == 0 and listPrimes[i] <= n:
            primeDivisors.list[i] = 1
    for i, elem in enumerate(primeDivisors.list):
        if elem:
            buffer.append(listPrimes[i])
    for i in range(primeDivisors.N):
        if primeDivisors.list[i]:
            primeDivisors.list[i] = 0
    return buffer


primeDivisors.list = []
primeDivisors.N = 10000
