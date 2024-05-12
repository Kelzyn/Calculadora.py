
def soma(num1, num2): 
    return num1 + num2
def subtracao(num1, num2): 
    return num1 - num2
def multiplicacao(num1, num2): 
    return num1 * num2
def divisao(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro: divisão por zero"
    
def calculadora(num1, num2, operacao):

    if operacao == '+' or operacao.lower() == 'soma':
        resultado = soma(num1 + num2)
    elif operacao == '-' or operacao.lower() == 'subtração':
        resultado = subtracao(num1 - num2)
    elif operacao == '*' or operacao.lower() == 'multiplicação':
        resultado = multiplicacao(num1 * num2)
    elif operacao == '/' or operacao.lower() == 'divisão':
        resultado = divisao(num1, num2)
    else:
        return("Operação inválida")
    
def main ():
    saida = ''
    while saida.flower() != 'n':
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /)")  
    print("Resultado da operação: ", resultado)
    resultado = calculadora(num1, num2, operacao)
    print("Resultado da operação: ", resultado)

    saida = input("Deseja sair? (N/n para sair, qualquer tecla para continuar): ")
    if saida.lower() != 'n' and saida.lower() != 's':
        print("Opção inválida. Por favor, responda S para SIM ou N para NÃO.")
    return resultado

    
    
