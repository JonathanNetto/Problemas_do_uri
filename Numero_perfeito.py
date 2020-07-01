
a = int(input())
soma = 0
contador = 0
while contador < a:
    b = int(input())

    for x in range(1, b):
        if b % x == 0:
            soma += x
    if soma == b:
        print("{numero} eh perfeito".format(numero = b))
    else:
        print("{numero} nao eh perfeito".format(numero = b))
    a -= 1
    soma = 0