#Programa que coloque um valor x na sequência de Fibonacci x vezes:

num = int(input('Insira um número inteiro: '))

while num < 0:
  num = int(input('Os números devem ser positivos! Digite o número: '))
x1 = 0
x2 = 1
num = num // 2
for i in range(num + 1):
    print(f'{x1}')
    x1 = x1 + x2
    print(f'{x2}')
    x2 = x2 + x1