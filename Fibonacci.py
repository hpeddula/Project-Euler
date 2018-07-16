first = 0
second = 1
fibonacci = [1,2]

def fibo(n):
    i = 0
    while (i <= n):
        next = fibonacci[i] + fibonacci[i+1]
        fibonacci.append(next)
        i +=1
    print(fibonacci)

n = int(input("Enter the number"))
fibo(n)