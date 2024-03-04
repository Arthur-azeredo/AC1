a = float(input("insira o valor de a: "))
b = float(input("insira o valor de b: "))
c = float(input("insira o valor de c: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("A equação não tem solção real")
else:
    x = (- b + delta ** 1/2) / (2 * a)
    x2 = (- b - delta ** 1/2) / (2 * a)

    print("A primeira raiz da equação é: ", x)
    print("A segunda raiz da equação é: ", x2)