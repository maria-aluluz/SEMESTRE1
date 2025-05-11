#Programa que pede o valor que será depositado todos o meses, o valor da taxa de juros mensal e o total de meses depois mostra o valor do montante e o valor dos juros em cada um dos n meses:

depositado = float(input('Insira o valor a ser depositado todos os meses: '))
while depositado <= 0:
  depositado = float(input('Insira o valor a ser depositado todos os meses que seja maior que zero: '))

j = float(input('Insira a taxa de juros: '))
while j <=0:
  j = float(input('Insira a taxa de juros maior que zero: '))

meses = int(input('Insira o período (em meses): '))
while meses <=0:
  meses = int(input('Insira o período (em meses) maior que zero: '))


j = j / 100
final = 0
i = 0


for i in range(meses):
  final = final + depositado
  final = final * (j + 1)
  print(f'O valor final no mês {i + 1} é {final:.2f}')