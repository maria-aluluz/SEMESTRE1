#Programa que pede o valor presente (capital inicial), a taxa de juros mensais e o período em meses para calcular e mostrar a evolução do valor futuro (montante) a cada um dos n meses:

inicial = float(input('Insira seu capital inicial: '))
while inicial <= 0:
  inicial = float(input('Insira um capital maior que zero: '))

j = float(input('Insira a taxa de juros: '))
while j <=0:
  j = float(input('Insira a taxa de juros maior que zero: '))

meses = int(input('Insira o período (em meses): '))
while meses <=0:
  meses = int(input('Insira o período (em meses) maior que zero: '))

j = j / 100
final = inicial
i = 0

for i in range(meses):
  final = final * j + final
  print(f'O valor final no mês {i + 1} é {final:.2f}')