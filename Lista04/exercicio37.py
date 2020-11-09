def entradaPl(frase):

    palavras = frase.split()
    junto = ''.join(palavras)

def palindromo(junto):

    inverso = ''

    for letra in range(len(junto) -1, -1, -1):
        inverso += junto[ĺetra]

    if inverso == junto:
        print('Temos um palindromo')
    else:
        print('Não temos um palidromo')

def main():
    frase = str(input('Digite uma frase: ')).strip().upper()
    entradaPl(frase)

if __name__ == "__name__":
    main()