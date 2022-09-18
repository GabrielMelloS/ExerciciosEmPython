def devedor(dev):
        print(f'Pagamento diponivel somente a vista, valor: {dev} reais: ')
        print('=====================================')

def adimplente(adp):
    print('Insira a opção que deseja realizar o pagamento :')
    print('1: a vista, 2: a prazo: ')
    pagamento = int(input()) 
    if pagamento == 1:
            print('Insira a opção de pagamento :')
            print('1: dinheiro, 2: cheque: ')
            pagamento1 = int(input())
            if pagamento1 == 1:
                    vn = adp * 20/100
                    vf= adp - vn
                    print(f'Pagamento a dinheiro, valor: {vf} reais: ')

            elif pagamento1 == 2:
                    vn = adp * 15/100
                    vf = adp- vn
                    print(f'Pagamento a cheque, valor: {vf} reais: ')
            else:
                    print('Opção Invalida!!')

    if pagamento == 2:
            print('Insira a opção de pagamento :')
            print('1: duas parcelas, 2: três parecelas, 3:quatro parcelas ou mais: ')
            pagamento1 = int(input())
            if pagamento1 == 1:
                    vn = adp * 5/100
                    vf= adp - vn
                    print(f'Duas parecelas, valor: {vf} reais: ')

            elif pagamento1 == 2:
                    print(f'Três Parcelas, valor: {adp} reais: ')

            elif pagamento1 == 3:
                    vn = adp * 5/100
                    vf= adp + vn
                    print(f'4 Parcelas ou mais, valor: {vf} reais: ')
            else:
                    print('Opção Invalida!!')



c = 1
print('Insira a opção que se aplica ao comprador :')
print('1: Devedor, 2:Adimplente ')
escolha = int(input())

while c ==1:

        if escolha == 1:
                dev=float(input('Insira o valor do produto: '))
                devedor(dev)
        
        elif escolha == 2:
                adp=float(input('Insira o valor do produto:\n'))
                adimplente(adp)

        else:
                print('Opção invalida.')
                
        c=int(input('Deseja continuar? Digite 1 para sim e 2 para não:\n'))
        if c == 2:
                print('FIM!')
                print('=====================================')
        else:
                print('Insira a opção que se aplica ao comprador :')
                print('1: Devedor, 2:Adimplente ')
                escolha = int(input())
