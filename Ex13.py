#Programa para determinar o MMC e o MDC de determinado valor:

n1 = int(input('Digite o primeiro número: '))
while n1 < 0:
  n1 = int(input('Os números devem ser positivos! Digite o primeiro número: '))

n2 = int(input('Digite o segundo número: '))
while n2 < 0:
  n2 = int(input('Os números devem ser positivos!Digite o segundo número: '))

if n1 == n2:
    print(f'O MDC dos dois números é {n1}')

if n1 and n2 ==0:
    print(f'O MDC é {n1}')

elif n1 > n2:
    divisor = n1 - 1
    while n1 % divisor != 0 or n2 % divisor != 0:
        divisor = divisor - 1
    print(f'O MDC é: {divisor}')

elif n1 < n2:
    divisor = n2 - 1
    while n1 % divisor != 0 or n2 % divisor != 0:
        divisor = divisor - 1
    print(f'O MDC de {n1} e {n2} é: {divisor}')

contador = 1
restonum1 = contador % n1
restonum2 = contador % n2

while restonum1 != 0 or restonum2 != 0:
    contador = contador + 1
    restonum1 = contador % n1
    restonum2 = contador % n2


print(f'O MMC de {n1} e {n2} é: {contador}')