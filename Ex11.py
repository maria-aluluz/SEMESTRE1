#Programa que mostra o fatorial de determinado valor:

n = int(input('Digite um número inteiro: '))
while n < 0:
  n = int(input('Digite um número inteiro positivo: '))

x = (n - 1)
fatorial = n * x

while x > 1:
  x = (x - 1)
  fatorial = fatorial * x

else: print(f'O fatorial de {n} = {fatorial}')