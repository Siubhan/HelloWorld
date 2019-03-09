def fib(n):
    a=b=1
    for i in range(n):
        yield a
        a,b=b,a+b

if __name__=='__main__':
    g=fib(int(input('Input fib №')))
    for i in g:
        print(i,end=' ')