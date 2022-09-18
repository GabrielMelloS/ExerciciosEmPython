def funcaoDistancia(km):
    milhas = km/1.61
    metros = km*1000
    centimetros = metros*100
    print(km,"km em milhas: %.2f" %milhas)
    print(km,"km em metros: ", metros)
    print(km,"km em centimetros: ", centimetros)


def funcaoLitros(litros):
    ml = litros*1000
    m3 = litros/1000
    galao = litros/3.785
    print(litros,"litros em mL: ", ml)
    print(litros,"litros em metros cúbicos: ", m3)
    print(litros,"litros em galões americanos: %.2f" %galao)


def funcaoPeso(kg):
    gr = kg*1000
    mg = gr*1000
    ton = kg/1000
    print(kg,"kg em gramas: ", gr)
    print(kg,"kg em miligramas: ", mg)
    print(kg,"kg em toneladas: ", ton)


def funcaoBytes(bytes):
    gb = bytes/1024
    kb = bytes*1024
    b = kb*1024
    print(bytes,"megabytes em gigabytes: %.2f" %gb)
    print(bytes,"megabytes em kilobytes: %.2f" %kb)
    print(bytes,"megabytes em bytes: %.2f" %b)


resp = 1

print("Escolha uma das opções para verificar as conversões:")
print("1- Medida de distância (km)  2-Capacidade (Litros)  3-Peso (kg)  4-Bytes (MB)")
opcao = int(input())

while(resp==1):
    if(opcao==1):
        km = float(input("Digite o valor em km para ser convertido: "))
        funcaoDistancia(km)

    elif(opcao==2):
        litros = float(input("Digite o valorem litros para ser convertido: "))
        funcaoLitros(litros)

    elif(opcao==3):
        kg = float(input("Digite o valor em kg para ser convertido: "))
        funcaoPeso(kg)

    elif(opcao==4):
        bytes = float(input("Digite o valor em MB para ser convertido: "))
        funcaoBytes(bytes)

    else:
        print("Opção inválida!")
    
    print("Deseja continuar? 1-Sim  2-Não")
    resp=int(input())

    if(resp==1):
        print("\nEscolha uma das opções para verificar as conversões:")
        print("1- Medida de distância (km)  2-Capacidade (Litros)  3-Peso (kg)  4-Bytes")
        opcao = int(input())
    else:
        print("=======FIM=======")