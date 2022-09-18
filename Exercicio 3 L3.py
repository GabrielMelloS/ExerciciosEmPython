def funcaoPJ(horasTrabalhadas, valorHora, deslocamento, dias):
    totalDeslocamento = deslocamento*0.51*dias
    totalHoras = horasTrabalhadas*1.30
    salario = totalHoras*valorHora
    bruto = salario + totalDeslocamento
    descontos = "INSS a ser recolhido pelo funcionário"
    liquido = bruto
    return (totalDeslocamento, salario, bruto, descontos, liquido)


def funcaoPF(horasTrabalhadas, valorHora, deslocamento, dias):
    totalDeslocamento = deslocamento*0.51*dias
    salario = horasTrabalhadas*valorHora
    bruto = salario + totalDeslocamento
    descontos = (valorHora*0.06)*horasTrabalhadas
    liquido = bruto-descontos
    return (totalDeslocamento, salario, bruto, descontos, liquido)


def funcaoCLT(horasTrabalhadas, valorHora, deslocamento, dias):
    totalDeslocamento = deslocamento*0.51*dias

    salario = horasTrabalhadas*valorHora
    periculosidade = salario*0.08
    #Como não está especificado, o adicional periculosidade foi feito sobre o total horas trabalhadas x valor hora
    bruto = salario + totalDeslocamento + periculosidade
    descontos = bruto*0.05
    liquido = bruto-descontos
    return (totalDeslocamento, salario, bruto, descontos, liquido)


nome = str(input("Digite o nome do funcionário: "))

valorHora = float(input("Informe o valor/hora: R$ "))

horasTrabalhadas = float(input("Informe a qtd. de horas trabalhadas: "))

dias = float(input("Informe a qtd. de dias trabalhados: "))
    #Dias pedidos apenas para realizar o cálculo correto do total de deslocamento
deslocamento = float(input("Informe quantos km são percorridos para chegar ao trabalho (ida e volta): "))

contrato = int(input("Selecione o tipo de contrato: 1-PJ  2-PF  3-CLT\n"))

if(contrato == 1):
    km, salarioHora, bruto, descontos, liquido = funcaoPJ(horasTrabalhadas, valorHora, deslocamento, dias)
elif(contrato == 2):
    km, salarioHora, bruto, descontos, liquido = funcaoPF(horasTrabalhadas, valorHora, deslocamento, dias)
elif(contrato == 3):
    km, salarioHora, bruto, descontos, liquido = funcaoCLT(horasTrabalhadas, valorHora, deslocamento, dias)
else:
    print("Preencha os dados novamente e digite uma opção válida!")
    exit()

print()
print("Funcionário: %s" %nome)
print("Total deslocamento: R$ %.2f" %km)
print("Total salario x valor hora: R$ %.2f" %salarioHora)
    #Como não está especificado, o adicional periculosidade (CLT) foi feito sobre o total horas trabalhadas x valor hora e inserido no total bruto
print("Total salario bruto: R$ %.2f" %bruto)
if(contrato==1):
    print(descontos)
else:
    print("Total descontos: R$ %.2f" %descontos)
    #Para CLT, INSS incide sobre o valor total bruto, já com periculosidade adicionado.
print("Total salario líquido: R$ %.2f" %liquido)