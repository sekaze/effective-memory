# Escreva uma função que, dado um número nota representando a nota de
# um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

def converte_conceito(nota):
    
    if nota >= 0 and nota <= 2:
        print('Média de aproveitamento: F')
    elif nota >= 2.1 and nota <= 4:
        print('Média de aproveitamento: E')
    elif nota >= 4.1 and nota <= 6:
        print('Média de aproveitamento: D')
    elif nota >= 6.1 and nota <= 8:
        print('Média de aproveitamento: C')
    elif nota >= 8.1 and nota <= 9:
        print('Média de aproveitamento: B')
    elif nota >= 9.1 and nota <= 10:
        print('Média de aproveitamento: A')


def main():
    nota = float(input('Insira sua nota para saber o conceito: '))
    
    converte_conceito(nota)

if __name__ =='__main__':
    main()








