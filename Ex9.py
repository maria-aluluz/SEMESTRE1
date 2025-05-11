#Um program que aceita apenas notas digitadas entre 0 e 10:

n = float(input("insira uma nota entre 0 e 10: "))

while n <0 or n >10:
    n = float(input('insira uma nota valida: '))