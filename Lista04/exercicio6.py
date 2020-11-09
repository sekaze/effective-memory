# Faça uma função que determina se um número é par ou ímpar. 
# Use o % para determinar o resto de uma divisão. 
# Por exemplo: 3 % 2 = 1 e 4 % 2 = 0

def parImpar(entrada):
    
    if entrada % 2 == 0:
        print(f'{entrada} é par!')
    else:
        print(f'{entrada} é ímpar!')
        
def main():
    entrada = int(input('Insira um número: '))
    
    parImpar(entrada)
    
if __name__ == '__main__':
    main()