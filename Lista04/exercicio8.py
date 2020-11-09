def menu_inicial():
    print('=' * 100)
    print('Programa para Conversão de Temperaturas')
    print('1 = Conversão de C° para F°')
    print('2 = Conversão de F° para C°')
    print('<Digite sair para finalizar>')
    print('=' * 100)
    
def conversao_cel_fah():
    celsius = float(input('Entre com a temperatura em graus Celsius: '))
    fahren = celsius * (9 / 5) + 32
    print(f'A temperatura em F° é {round(fahren, 2)}')

def conversao_fah_cel():
    fahren = float(input('Entre com a temperatura em graus Fahrenheit: '))
    celsius = (fahren - 32) * (5 / 9)
    print(f'A temperatura em C° é: {round(celsius, 2)}')

def main():
    while True:
    
        menu_inicial()
    
        args = input('Escolha a opção: ')
    
        if args == '1':
            conversao_cel_fah()
        elif args == '2':
            conversao_fah_cel()
        elif args == 'sair':
            print('===== PROGRAMA FINALIZADO =====')
            break
        else:
            print('==== Argumentos inválidos ====')
    
if __name__ == "__main__":
    main()
