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
total = 0
for i in range(fibonacci.__len__()):
    if( fibonacci[i] %2 == 0):
        # print(fibonacci[i])
        total += fibonacci[i]
print(total)