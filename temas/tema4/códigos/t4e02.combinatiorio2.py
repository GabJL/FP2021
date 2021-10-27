m = int(input("Dime el valor de m: "))
n = int(input("Dime el valor de n: "))

def factorial(N):
    res = 1
    for i in range(2, N+1):
        res *= i
    return res

factorial_m = factorial(m)
factorial_n = factorial(n)
factorial_m_n = factorial(m-n)

combinatorio = factorial_m / (factorial_n * factorial_m_n)

print("El resultado es", combinatorio)
