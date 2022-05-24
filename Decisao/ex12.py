valorHr = float(input('Entre com o valor que você recebe por hora: '))
horasTrab = float(input("'Entre com o valor de horas que você trabalhou esse mês: '"))

salarioB = valorHr * horasTrab

if salarioB <= 900: descontoIr = 0.0
elif salarioB <= 1500: descontoIr = 5
elif salarioB <= 2500: descontoIr = 10
else: descontoIr = 20

IR = salarioB * (descontoIr / 100)
INSS = salarioB * (10 / 100)
FGTS = salarioB * (11 / 100)
totalDesconto = IR + INSS
salarioLiquido = salarioB - totalDesconto

print(
    f"\nSalário Bruto     : R${salarioB:.2f}",
    f"\n(-) IR (5%)       : R${IR:.2f}",
    f"\n(-) INSS ( 10%)   : R${INSS:.2f}",
    f"\nFGTS (11%)        : R${FGTS:.2f}",
    f"\nTotal de descontos: R${totalDesconto:.2f}",
    f"\nSalário Liquido   : R${salarioLiquido:.2f}",
)