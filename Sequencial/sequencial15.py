valorHr = float(input("Entre com o valor q vc ganha por Hr: "))
horasTrab = float(input("Entre com o total de horas trabalhadas no mes: "))
salarioBruto = valorHr*horasTrab

ir = salarioBruto*0.11
inss = salarioBruto*0.08
sindicato = salarioBruto*0.05
descontos = ir+inss+sindicato
salarioLiquido = salarioBruto - descontos

print("Salario bruto: ", salarioBruto)
print("Valor pago ao Imposto de renda: ", ir)
print("Valor pago ao INSS: ", inss)
print("Valor pago ao sindicato: ", sindicato)
print("Valor so salario liquido: ", salarioLiquido)


