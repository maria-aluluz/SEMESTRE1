#Programa para mostrar a tabuada de determinado número:

tab = int(input("qual tabuada quer visualizar?"))

for i in range(11):
  print(f'{tab} x {i:2d} = {tab * i:3d}')