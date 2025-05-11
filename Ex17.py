#Programa que nao utiliza da funçao bin(), mas calcula um número em binário:

x = int(input('Insira o número positivo: '))
while x < 0:
  x = int(input('O número precisa ser positivo:'))

numero = x
binario = str()

if x == 0:
  print(f'O número {x} em binário é O!!!!!!!!!!')
else:
  while numero > 0:
    resto = numero % 2
    numero = numero // 2
    binario = str(resto) + binario
  print(f'O número {numero} em binário é {binario}')