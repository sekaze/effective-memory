# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. 
# Se eles forem iguais, imprima que eles sao iguais.
                
def menor(n1, n2):
  if n1 < n2:
    print(n1)
  else: 
    print(n2)

def igual(n1, n2):
    if n1 == n2:
        print(f'{n1} e {n2} são iguais!')

def main():
    n1 = int(input('Insira um número: '))
    n2 = int(input('Insira um número: '))
    
    if n1 == n2:
        igual(n1, n2)
    else:
        menor(n1, n2)
    
    
if __name__ == '__main__':
    main()