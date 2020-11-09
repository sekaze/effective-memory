# Escreva uma função que recebe como entrada um número ano e retorna
# True caso ano seja bissexto. Caso contrário, retorne False.

def verifBissexto(ano):
    
    if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
        print(f'{ano} é Bissexto')
        return True
    else:
        print(f'{ano} não é bissexto')
        return False
        
def main():
    ano = int(input('Insira o ano: '))
    
    verifBissexto(ano)
      
if __name__ == '__main__':
    main()