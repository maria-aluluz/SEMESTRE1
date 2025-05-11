#Programa que conta quantos números positivos e negativos foram digitados pelo usuário até que ele digite zero:

positivo = 0
negativo = 0
num = int(input("insira um número inteiro: "))

while num != 0:

    if num >0:
        positivo = positivo + 1

    elif num <0:
        negativo = negativo + 1

    num = int(input("insira um numero inteiro: "))

print(f'você digitou {positivo} números positivos e {negativo} negativos')