m = 1
soma = 0
n = int(input("Entre com o valor de N: "))


print("S = ", end = "")

for i in range(n):
    print(i+1, end = "/")
    print(m,"." if(i+1 == n) else("+ "), end = "")
    soma += (i+1)/m
    m += 2
print("\nSoma:%.2f" %soma)