def logica_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def checar_numero():
    n = int(input("Digite um número inteiro: "))
    if logica_fibonacci(n):
        print("O número é um número da sequencia de Fibonacci")
    else:
        print("O número não é um número da sequencia de Fibonacci")

checar_numero()

