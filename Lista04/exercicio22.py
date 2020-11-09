# Faça um programa com uma função que necessite de três argumentos, e
# que forneça a soma desses três argumentos.

def soma(x, y, z):
    res = x + y + z
    return res
    
def main():
    x = int(input('Primeiro numero: '))
    y = int(input('Segundo numero: '))
    z = int(input('Terceiro numero: '))

    soma(x, y, z)
    print(soma(x, y, z))
    

if __name__ == '__main__':
    main()