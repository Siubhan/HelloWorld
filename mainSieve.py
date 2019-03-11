from sieve import sieveMeth, primeDivisors

if __name__ == '__main__':
    l = sieveMeth(10000)
    val = 1
    itVal=0
    masMas=[]
    valMas=[]
    while val:
        try:
            val = int(input('Input an int val(Zero for Exit): '))
            if val:
                masMas.append([val,primeDivisors(val, l)])
                valMas=[]
        except ValueError:
            print('Isn\'t int value!')
    print(masMas)
