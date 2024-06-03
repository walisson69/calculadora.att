print('=-=' * 20)
print('                   CALCULADORA   ')
print('=-=' * 20)
print('''ESCOLHA UMA DESSAS OPÇÕES
      [0]Para fechar o programa
      [1]Adição
      [2]Subtração
      [3]Multiplicação
      [4]Divisão
      [5]Potenciação''')
     
while True:
    num = int(input('Opção: '))
    if num == 1:
        print('Você escolheu Adição!')
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro: '))
        nr = n1 + n2
        print(f'{n1} + {n2} = {nr}')
    elif num == 2:
        print('Você escolheu Subtração!')
        sub = int(input('Digite um numero: '))
        sub2 = int(input('Digite outro: '))
        subr = sub -  sub2
        print(f'{sub} - {sub2} = {subr}')
    elif num == 3:
        print('Você escolheu Multiplicação!')
        mult = int(input('Digite um numero: '))
        mult2 = int(input('Digite outro: '))
        multr = mult * mult2
        print(f'{mult} X {mult2} = {multr}')
    elif num == 4:
        print('Você escolheu Divisão!')
        div = float(input('Digite um numero: '))
        div2 = float(input('Digite outro: '))
        divr = div / div2
        print(f'{div} / {div2} = {divr:.1f}')
    elif num == 5:
        print('Você escolheu Potenciação!')
        pot = int(input('Digite a base: '))
        pote = int(input('Digite o expoente: '))
        pottotal = pot ** pote
        print(f'O resulatado da potencia {pot} e {pote} é {pottotal}')
    elif num == 0:
        print('Sessâo finalizada. Volte sempre!')
        break
    else:
        print('Tente novamente. Essa opção não existe!!')
