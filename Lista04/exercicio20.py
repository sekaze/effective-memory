# Escreva uma função que recebe como entrada um número inteiro positivo
# n e imprime a representação binária desse número.

def menu_inicial():
    print('||Bem-vindo ao programa de conversao de decimal para binario||'.upper())
    
def conversaoBin():
    print('=' * 60)
    n = int(input('Digite um número inteiro: '))
    print('=' * 60)
    print(f'O número {n} em binário é {bin(n)}')
    print('=' * 60)
    
if __name__ =='__main__':
    menu_inicial()
    conversaoBin()