# Faça uma função que informe a quantidade de dígitos de um determinado
# número inteiro informado.

def quant_digit(inp):
    print('=' * 80)
    print(f'Número: {str(inp)}')
    print(f'Quantidade de digitos: {str(len(inp))}')
    print('=' * 80)
    
def main():
    inp = int(input('Insira um número: '))
    inp = str(inp)
    
    quant_digit(inp)
    
if __name__ == '__main__':
    main()
    