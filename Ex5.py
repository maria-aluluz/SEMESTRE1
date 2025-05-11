#Programa que ordena 3 strings em ordem alfabética:

valor1 = str(input('insira a primeira palavra:'))

valor2 = str(input('insira a segunda palavra:'))

valor3 = str(input('insira a terceira palavra:'))


if valor1 > valor2 and valor2 > valor3:
  print('a sequência de plavras em ordem alfabética é:', valor3, valor2, valor1)
if valor1 > valor3 and valor3 > valor2:
  print('a sequência de plavras em ordem alfabética é:', valor2, valor3, valor1)
if valor2 > valor3 and valor3 > valor1:
  print('a sequência de plavras em ordem alfabética é:', valor1, valor3, valor2)
if valor2 > valor1 and valor1 > valor3:
  print('a sequência de plavras em ordem alfabética é:', valor3, valor1, valor2)
if valor3 > valor2 and valor2 > valor1:
  print('a sequência de plavras em ordem alfabética é:', valor1, valor2, valor3)
if valor3 > valor1 and valor1 > valor2:
  print('a sequência de plavras em ordem alfabética é:', valor2, valor1, valor3)