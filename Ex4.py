#Programa que ordena três valores em ordem crescente:

valor1 = float(input('insira o primeiro valor:'))

valor2 = float(input('insira o segundo valor:'))

valor3 = float(input('insira o terceiro valor:'))


if valor1 > valor2 and valor2 > valor3:
  print('a sequencia de números de forma crescente é:', valor3, valor2, valor1)
elif valor1 > valor3 and valor3 > valor2:
  print('a sequência de números de forma crescente é:', valor2, valor3, valor1)
elif valor2 > valor3 and valor3 > valor1:
  print('a sequência de números de forma crescente é:', valor1, valor3, valor2)
elif valor2 > valor1 and valor1 > valor3:
  print('a sequência de números de forma crescente é:', valor3, valor1, valor2)
elif valor3 > valor2 and valor2 > valor1:
  print('a sequência de números de forma crescente é:', valor1, valor2, valor3)
elif valor3 > valor1 and valor1 > valor2:
  print('a sequência de números de forma crescente é:', valor2, valor1, valor3)