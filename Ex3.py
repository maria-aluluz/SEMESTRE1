#Programa que indica qual valor é maior entre três valores:

valor1 = float(input('insira o primeiro valor:'))

valor2 = float(input('insira o segundo valor:'))

valor3 = float(input('insira o terceiro valor:'))


if valor1 == valor2 and valor2 < valor3:
  print("os valores", valor1,'e', valor2, 'são iguais e menores que', valor3)

elif valor1 == valor2 and valor2 > valor3:
  print("os valores", valor1,'e', valor2, 'são iguais e maiores que', valor3)


elif valor1 == valor3 and valor3 < valor2:
  print("os valores", valor1,'e', valor3, 'são iguais e menores que', valor2)

elif valor1 == valor3 and valor3 > valor2:
  print("os valores", valor1,'e', valor3, 'são iguais e maiores que', valor2)


elif valor3 == valor2 and valor2 < valor1:
  print("os valores", valor3,'e', valor2, 'são iguais e menores que', valor1)

elif valor3 == valor2 and valor2 > valor1:
  print("os valores", valor3,'e', valor2, 'são iguais e maiores que', valor1)



elif valor1 > valor2 and valor1 > valor3:
  print('o', valor1, 'é o maior!')

elif valor2 > valor1 and valor2 > valor3:
  print('o', valor2, 'é o maior!')

elif valor3 > valor1 and valor3 > valor2:
  print('o', valor3, 'é o maior!')


elif valor1 == valor2 == valor3:
  print('todos os valores são iguais!')