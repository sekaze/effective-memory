def craps():
    from random import randint
    
    jogada = 0
    ponto = 0
    
    n1 = input("0: Encerrar, 1: Jogar ")
    
    while (n1 != 0):
        jogada += 1         # jogada = jogada + 1
        
        print(f"Jogada: {jogada}")
        
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        
        resultado = d1 + d2
        
        print(f"D1: {d1},D2: {d2},Resultado: {resultado}")

        if (ponto == 0):
            if (resultado == 7) or (resultado == 11):
                print("Você venceu o CRAPS")
                n1 = 0
            elif (resultado == 2) or (resultado == 3) or (resultado == 12):
                print("Você perdeu o CRAPS")
                n1 = 0
            else:
                print(f"Você precisa tirar agora {resultado}")
                ponto = resultado
        else:
            if (resultado == ponto):
                print("Você venceu o CRAPS")
                n1 = 0
            if (resultado == 7):
                print("Você perdeu o CRAPS")
                n1 = 0

def main():
    craps()

if __name__ == "__main__":
    main()
