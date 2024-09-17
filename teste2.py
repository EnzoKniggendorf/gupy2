def pertence_fibonacci(numero):
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    return a == numero

numero_informado = 21
if pertence_fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")
