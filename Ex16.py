#Um programa que pede o número n de provas e as n notas e calcula a média e o desvio padrão dessas notas: (Atenção: a utilização de determinadas funções do python, como criação de listas e bibliotecas, que até então não foram passadas pelo professor, não receberam autorização para a utilização)

soma = 0
desvio = 0
somaquadrado = 0
provas = int(input('Digite a quantidade de provas que você teve: '))
while provas < 1:
  provas = int(input('Digite pelo menos uma prova: '))

for nota in range(provas):
  nota = float(input("Digite a nota que você obteve: "))
  soma = soma + nota
  somaquadrado = nota ** 2 + somaquadrado

media = soma / provas
mediaquadrado = somaquadrado / provas
x = media ** 2

desvio = (mediaquadrado - x) ** 0.5

print(f'A média das suas notas foi: {media}')
print(f'O desvio das suas notas foi: {desvio}')