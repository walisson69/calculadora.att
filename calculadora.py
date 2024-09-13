import os
import time

while True:
    try:
        numero1 = int(input('Digite um numero: '))
        numero2 = int(input('Digite outro numero: '))
        print('''Opções aritméticas:
[+]Soma
[-]Subtração
[x]Multiplicação
[/]Divisão
[F]Para fechar''')
        escolha_user = input('Escolha uma das opções listadas acima: ').upper()
    except:
        os.system('cls')
        print('Por favos digite apenas numeros inteiros')
        continue
    
    if escolha_user == '+':
        os.system('cls')
        soma_total = numero1 + numero2
        print(f'A soma entre {numero1} e {numero2} é {soma_total}')

    elif escolha_user == '-':
        os.system('cls')
        soma_total = numero1 - numero2
        print(f'A subtração entre {numero1} e {numero2} é {soma_total}')

    elif escolha_user == 'X':
        os.system('cls')
        soma_total = numero1 * numero2
        print(f'A multiplicação entre {numero1} e {numero2} é {soma_total}')
    
    elif escolha_user == '/':
        os.system('cls')
        soma_total = numero1 / numero2
        print(f'A divisão entre {numero1} e {numero2} é {soma_total:.2f}')
    elif escolha_user == 'F':
        os.system('cls')
        print('ENCERRANDO CALCULADORA!!....')
        time.sleep(3)
        print('PROGRAMA ENCERRADO!!')
        break
