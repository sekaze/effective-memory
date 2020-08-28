aluno = list()
dados = dict()
opcoes = ()

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
    print()
    opcoes = int(input('Opção: '))

    if opcoes == 1:
        while True:
            dados.clear()
            dados['nome'] = input('Digite o nome do aluno: ')
            dados['matricula'] = input('Digite a matrícula do aluno: ')
            dados['nota1'] = float(input('Digite a nota 1: '))
            dados['nota2'] = float(input('Digite a nota 2: '))
            dados['nota3'] = float(input('Digite a nota 3: '))
            dados['media'] = (dados['nota1'] + dados['nota2'] + dados['nota3']) / 3
            aluno.append(dados.copy())
            while True:
                resp = str(input('Deseja realizar novo cadastro?[S/N]: ')).upper()[0]
                if resp in 'SN':
                    break
                print('Responda somente S ou N!')
            if resp == 'N':
                break
    elif opcoes == 4:
        print(aluno)

    elif opcoes == 2:
        while True:
            x = int(input('Deseja ver a média de quantos alunos? '))
            for i in range(x):
                vm = float(input('Digite a matrícula do aluno: '))
            for vm in aluno:
                if vm['matricula'] in aluno.__contains__(vm):
                    print(f'{vm["nome"]}, {vm["matricula"]}, {vm["media"]}')
                else:
                    print('Uma ou mais matrículas não encontradas, verifique')
            while True:
                resp = str(input('Deseja verificar alguma outra média?[S/N]: ')).upper()[0]
                if resp in 'SN':
                    break
                print('Responda somente S ou N!')
            if resp == 'N':
                break
