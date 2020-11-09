# Escreva uma função que recebe dois números (a e b) como parâmetro e
# retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.

def numPlus(a, b, limite):
    
    if (a + b) > limite:
        print(f'{a} + {b} é maior que {limite}')
        return True
    elif (a + b) < limite:
        print(f'{a} + {b} é menor que {limite}')
    elif (a + b) == limite:
        print(f'{a} + {b} é igual a {limite}')
    
def main():
    
    a = int(input('Insira um número: '))
    b = int(input('Insira um número: '))
    limite = int(input('Defina o limite do resultado: '))
    
    numPlus(a, b, limite)
    
if __name__ == '__main__':
    main()
    
    