#Programa para calcular o TMB de uma pessoa:

genero = str(input('qual seu gênero?'))
while genero != 'homem' and genero != 'mulher':
  genero = str(input('Insira um gênero válido:'))

idade = int(input('Digite sua idade:'))

altura = float(input('Qual sua altura?(em centímetros)'))

peso = float(input('Qual seu peso?(Em quilogramas)'))


if genero == 'mulher':
  tmb = 655.09 + (9.563 * peso) + (1.85 * altura) - (4.676 * idade)
  print('Seu TMB É:', tmb)

elif genero == 'homem':
  tmb = 66.47 + (13.75 * peso) + (5.003 * altura) - (6.755 * idade)
  print('seu TMB é:', tmb)