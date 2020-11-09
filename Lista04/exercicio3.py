def absoluteValue(n1):
    calculo = abs(n1)
    return calculo


def absoluteValueCalculation(n1):
    if (n1 < 0):
        calculo = n1 * (-1)
    else:
        calculo = n1
    return calculo


def main():
    n1 = float(input("Digite um número: "))
    n2 = int(input("Escolha a função : "))

    if (n2 == 1):
        print(absoluteValueCalculation(n1))
    elif (n2 == 2):
        print(absoluteValue(n1))
    else:
        print ("Digite 1 ou 2")

if __name__ == "__main__":
    main()
