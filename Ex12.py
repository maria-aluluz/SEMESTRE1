#Programa para indicar se determinado número é primo ou não:

n = int(input('Digite um número inteiro: '))
while n <= 1:
  n = int(input('Todos os números iguais ou menores que 1 não são primos! '))

x = n - 1
primo = True

while x > 1:
    resto = n % x
    x = x - 1
    if resto == 0:
      primo = False
      break

if primo == False:
  print(f'O número {n} não é primo ')
else:
  print(f'O número {n} é primo!')