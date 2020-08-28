opcoes = [1, 2, 3]
while opcoes != 3:
    print('===================')
    print('===  BEM VINDO  ===')
    print('===================')
    print()
    print()
    print()
    print('''Selecione a opção:
    
    1 - Cadastrar novo aluno: 
    2 - Verificar média de alunos:
    3 - Sair''')
    opcoes = int(input('Opção: '))

    if opcoes == 1:
        resp = [1, 2]
        while resp != 2:
            nome = []
            matricula = []
            nota1 = []
            nota2 = []
            nota3 = []
            media = []
            novo_usu = input('Digite o nome do aluno: ')
            nome.append(novo_usu)
            nova_matri = input('Digite a matrícula do aluno: ')
            matricula.append(nova_matri)
            nova_nota1 = float(input('Digite a nota 1: '))
            nota1.append(nova_nota1)
            nova_nota2 = float(input('Digite a nota 2: '))
            nota1.append(nova_nota2)
            nova_nota3 = float(input('Digite a nota 3: '))
            nota3.append(nova_nota3)
            media_nov = (nova_nota1 + nova_nota2 + nova_nota3) / 3
            media.append(media_nov)
            resp = int(input('Deseja realizar novo cadastro? [1 - S / 2 - N]: '))

    elif opcoes == 2:
        resp = []
        while resp != 2:
            verif_matr = []
            x = int(input('Deseja ver a média de quantos alunos? '))
            for i in range(x):
                ins_matri = int(input('Digite a matrícula do aluno: '))
                verif_matr.append(ins_matri)
        if set(verif_matr) & set(matricula):
            print('As médias são: ',set(verif_matr) & set(matricula))
        resp = int(input('Deseja ver mais alguma média? '))
