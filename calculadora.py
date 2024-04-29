a = 0
b = 0
resultado = 0
operacao = ''


while True:
    a = int(input('Digite um número: '))
    operacao = input('Digite a operação: ')
    b = int(input('Digite outro numero: '))

    if operacao == '+':
        resultado = a + b
    elif operacao == '-':
        resultado = a - b
    elif operacao == '/':       
        resultado = a / b
    elif operacao == '*': 
        resultado = a * b
    else:
        resultado = 'Operação inválida'

    print(str(a) + ' ' + str(operacao) + ' ' + str(b) + ' = ' + str(resultado))
