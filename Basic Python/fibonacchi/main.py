def fibo(num1, num2, n):
    if n == 0: return num1

    return fibo(num2, num1 + num2, n - 1)


print(fibo(0, 1, 40-1))

def fibo2(num):
    startNum = 1
    tempNum = 0

    for i in range(num):
        oldNum = startNum

        startNum += tempNum
        tempNum = oldNum
    return startNum

print(fibo2(40-2))
