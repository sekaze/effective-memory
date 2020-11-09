# Escreva uma função que recebe um número n como parâmetro
# e imprime se n é positivo ou negativo.

def numPlusMinus(num):
    
    if num < 0:
        print(f'{num} é negativo!')
    elif num >= 0:
        print(f'{num} é positivo!')
        
def main():
    num = int(input('Insira um número: '))
    
    numPlusMinus(num)
    
if __name__ == "__main__":
    main()