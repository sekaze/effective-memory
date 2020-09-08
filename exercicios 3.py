from random import randint
from datetime import datetime

# Atividade 1
print("\nOlá tudo bem?" * 30)

# Atividade 2
a = []
for i in range(10):
    x = int(input("Digite um número: "))
    a.append(x)
print(sum(a))

# Atividade 3
b = []
for i in range(15):
    n = int(input("Digite um número: "))
    b.append(n)
print(min(b), max(b))

# Atividade 4 & 11
for i in range(0, 10):
    print()
    print('*' * 10)
    print(f'Tabuada do {i}')
    print('*' * 10)
    print()
    for m in range(0, 11):
        print(f'{i} * {m} = {i * m}')

# Atividade 5
soma = []
z = 1
for i in range(1, 51):
    x = z / i
    z = z + 2
    soma.append(x)
print(round(sum(soma), 2))

# Atividade 6
w = ()
aux = 1
prod = 1
while w != 0:
    w = float(input('Digite um número ou 0 para terminar: '))
    aux = w
    if aux != 0:
        prod *= aux
print(prod)

# Atividade 7
soma = 0
y = int(input('Digite um número positivo e inteiro: '))

for i in range(1, y):
    if y % i == 0:
        soma += i
if y == soma:
    print(f'{y} é um número perfeito.')
else:
    print(f'{y} não é um número perfeito.')

# Atividade 8
x = 1
z = 1.10
c = 1.50
while z < c:
    z += 0.03
    c += 0.02
    x += 1
print(f'Irá demorar {x} anos para Zé ser maior que Chico')

# Atividade 9
v = []
n = 1
while (n > 0) or (n != 0):
    n = int(input('Digite um número: '))
    if (n != 0) and (n > 0):
        v.append(n)
    else:
        break
print(f'O menor número digitado foi {min(v)} e o maior número digitado foi {max(v)}')

# Atividade 10
n = int(input('Digite um número para ver sua tabuada: '))
print()
print('*' * 30)
print(f'Tabuada do número {n}:'.center(30))
print('*' * 30)
print()
for i in range(0, 11):
    print(f'{n} * {i} = {n * i}')

# Atividade 12
n1 = int(input('Digite um número positivo e inteiro: '))
n2 = int(input('Digite outro número positivo e inteiro: '))
n3 = 1
for i in range(n2):
    n3 *= n1
print(f'O número {n1} elevado a {n2} dá um total de {n3}')

# Atividade 13
num = int
x = 0
tot = 0
while num != 0:
    num = int(input('Digite um número inteiro. Se deseja parar digite 0: '))
    if (num % 2 == 0) and (num != 0):
        tot += num
        x += 1
print(f'Você digitou um total de {x} numeros pares. E a média deles é de {tot / x}')

# Atividade 14
n = float
while True:
    n = float(input('Digite um número real positivo: '))
    if n > 0:
        print('O número digitado é válido')
        break
    else:
        print('Digite novamente o número.')

# Atividade 15
n = int(input('Quantos números randomicos deseja gerar? '))
for i in range(n):
    rn = randint(1000, 1999)
    if rn % 11 == 5:
        print(rn)

# Atividade 16
sec = 50
secatual = 0
min = 0
hr = 0
gratual = float

grinicial = float(input('Digite a massa (em G - Gramas): '))
gr = grinicial
while True:
    if gr > 0.5:
        gr = gr / 2
        secatual += 1
        gratual = gr
    else:
        break
secatual = sec * secatual

while True:
    if secatual >= 60:
        min += 1
        secatual -= 60
    elif min >= 60:
        hr += 1
        min -= 60
    else:
        break
print(f'Um produto com uma massa de {grinicial} demorou {hr} hora(s), {min} minuto(s) e {secatual} segundo(s) para '
      f'ficar com {round(gratual, 2)} gramas')

# Atividade 17
t1 = 0
t2 = 1
cont = 3
n = int(input('Digite um número para a sequência: '))
print(f'{t1} -> {t2}', end=" ")
while cont <= n:
    t3 = t1 + t2
    print(f'-> {t3}', end=" ")
    t1 = t2
    t2 = t3
    cont += 1


# Atividade 18
def operacoes():
    if opcoes == 1:
        soma = n1 + n2
        print(f'A soma dos números é: {soma}')
    elif opcoes == 2:
        divisao = n1 / n2
        print(f'A divisão dos números é: {divisao}')
    elif opcoes == 3:
        multiplicacao = n1 * n2
        print(f'A multiplicação dos números é: {multiplicacao}')
    elif opcoes == 4:
        subtracao = n1 - n2
        print(f'A subtração dos números é: {subtracao}')


opcoes = ()
while True:
    print()
    print('*' * 30)
    print('Calculadora'.center(30))
    print('*' * 30)
    print()
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro número: '))
    if n1 and n2 != 0:
        while opcoes != 5:
            print()
            print('*' * 30)
            print('Menu'.center(30))
            print('*' * 30)
            print()
            print('''1 - Somar
2 - Dividir
3 - Multiplicar
4 - Subtrair
5 - Digitar outros números (digite em ambos os números para parar)''')
            print()
            opcoes = int(input('Digite a opção desejada: '))
            print()
            operacoes()
    else:
        break

# Atividade 19
d1 = input('Digite o primeiro dia: ')
m1 = input('Digite o primeiro mês: ')
d2 = input('Digite o segundo dia: ')
m2 = input('Digite o segundo mês: ')
data1 = (datetime.strptime(f'1950-{m1}-{d1}', '%Y-%m-%d'))
data2 = (datetime.strptime(f'1996-{m2}-{d2}', '%Y-%m-%d'))

quantidade_dias = abs((data1 - data2).days)
print(quantidade_dias)


# Atividade 20
i = 0
ipar = 0
iimpar = 0
while i <= 999:
    i = int(input('Digite um número: '))
    if (i % 2 == 0) and (i < 1000):
        ipar += i
    else:
        iimpar += i
print(f'A soma dos números pares é de {ipar} e de números impares é de {iimpar}')

# Atividade 21
lista = []
prod = 1
while True:
        lista.clear()
        for i in range(3):
            n = float(input('Digite de forma crescente os números do conjunto: '))
            lista.append(n)
        if lista == sorted(lista):
            for numero in lista:
                prod *= numero
            media = sum(lista)/3
            print(f'A soma do conjunto é {sum(lista)}, o produto do conjunto é {prod} e a média é {media}')
        else:
            break

# Atividade 22

medias = []
while True:
    x = int(input('Deseja digitar quantas médias? '))
    medias.clear()
    for i in range(x):
        m = float(input('Digite a média [Digite número negativo para sair]: '))
        if m > 0:
            medias.append(m)
        else:
            medias.clear()
            break
    if not medias:
        print('A média não pode ser negativa.')
        break
    else:
        print()
        print(f'A maior média é a {max(medias)} e a menor média é a {min(medias)}. E a média das médias é {sum(medias)/x}')
        print()


# Atividade 23
nimpar = []
npar = []
n = int(input('Digite um número: '))
for i in range(n):
    if i % 2 == 0:
        npar.append(i)
    if (i % 3 == 0) and i > 0:
        nimpar.append(i)
print(f'Até o número {n} temos os seguintes números pares: {npar} e os seguintes números impares {nimpar}')

# Atividade 24
tot = 0
n = int(input('Digite um número: '))
for i in range(1, n+1):
    if n % i == 0:
        tot += 1
if tot == 2:
    print(f'O número {n} é primo')
else:
    print('O número não é primo')

# Atividade 26
npar = 0
nimpar = 1

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
for i in range(n1, n2+1):
    if i % 2 == 0:
        npar += i
    else:
        nimpar *= i
print(f'Entre {n1} e {n2} temos uma soma de {npar} dos números pares. E um produto de {nimpar} entre os números impares.')

# Atividade 27
alunos = {}
provas = []
medias = []


def cadastra_aluno():
    for i in range(x):
        provas.clear()
        nome = str(input('Digite o nome do aluno: '))
        for c in range(1, y+1):
            provas.append(float(input(f'Digite a nota da prova {c}: ')))
        media = sum(provas)/y
        medias.append(sum(provas)/y)
        alunos[media] = nome
        print(f'O aluno {nome} teve uma média de {sum(provas)/y}')
        print()


def finalizacao():
    dados = alunos.get(max(medias))
    if dados is not None:
        print(f'O aluno com maior média foi {dados} com a média {max(medias)}')


x = int(input('Quantos alunos tem na sala? '))
y = int(input('Quantas provas esta turma fez? '))
cadastra_aluno()
finalizacao()

# Atividade 28
funcionarios = {}
comissoes = []
total = []
todos = []


def cadastra_funcionario():
    x = int(input('Quantos funcionários tem na empresa? '))
    for i in range(x):
        funcionarios.clear()
        funcionarios['nome'] = str(input('\nDigite o nome do funcionário: '))
        comissao = int(input('Digite o valor das vendas deste funcionário: '))
        total.append(comissao)
        if comissao > 3000:
            funcionarios['comissao'] = comissao * 0.35
            comissoes.append(comissao * 0.35)
        elif (comissao <= 3000) and (comissao >= 1500):
            funcionarios['comissao'] = comissao * 0.20
            comissoes.append(comissao * 0.20)
        elif comissao < 1500:
            funcionarios['comissao'] = comissao * 0.13
            comissoes.append(comissao * 0.13)
        todos.append(funcionarios.copy())


while True:
    print('*' * 15)
    print(f'BEM-VINDO'.center(15))
    print('*' * 15)
    print()
    print('''Digite a opção desejada:
1 - Cadastrar funcionários e suas comissões
2 - Verificar funcionários e suas comissões
3 - Verificar o total de vendas da empresa
4 - Verificar o total de comissões pagas
5 - Sair''')
    print()
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        cadastra_funcionario()
    elif opcao == 2:
        for f in todos:
            print(f'O funcionário {f["nome"]} teve uma comissão de {f["comissao"]} reais.')
        print()
    elif opcao == 3:
        print(f'O total de vendas da empresa foi de: {sum(total)}')
    elif opcao == 4:
        print(f'O total de comissoes foi de: {sum(comissoes)}')
    elif opcao == 5:
        break

# Atividade 29
numinscr = 0
inscritos = dict()
galera = list()
soma = 0
idade = 0
qnthomens = 0
qntmulheres = 0
homensacima = 0
homensabaixo = 0

while True:
    inscritos.clear()
    inscritos['numeroinscricao'] = int(input('Digite o número de inscrição [-1 para terminar o cadastro]: '))
    if inscritos['numeroinscricao'] == -1:
        break
    inscritos['idade'] = int(input('Digite sua idade: '))
    while True:
        inscritos['sexo'] = input('Digite seu sexo [F/M]: ').upper()[0]
        if inscritos['sexo'] in 'MF':
            break
        print('Digite somente F OU M.')
    while True:
        inscritos['experiencia'] = input('Você possui experiência anterior? [S/N] ').upper()[0]
        if inscritos['experiencia'] in 'SN':
            break
        print('Digite somente S OU N')
    galera.append(inscritos.copy())
print()
print('*' * 30)
for f in galera:
    if f['sexo'] in 'Ff':
        soma += 1

for f in galera:
    if (f['sexo'] in 'Mm') and (f['experiencia'] in 'Ss'):
        qnthomens += 1
        idade += f['idade']

for f in galera:
    if (f['sexo'] in 'Mm') and (f['idade'] > 45):
        homensacima += 1
    elif (f['sexo'] in 'Mm') and (f['idade'] <= 45):
        homensabaixo += 1

if homensabaixo != 0:
    percenth = (homensacima / (homensacima + homensabaixo)) * 100
else:
    percenth = 0

print(f'A quantidade de mulheres nesta seletiva foi de {soma}.')
if qnthomens != 0:
    print(f'A idade média dos homens com experiência anterior é de {round((idade / qnthomens), 2)}')
print(f'A porcentagem de homens com idade acima de 45 anos é de {round(percenth, 2)}%')

# Atividade 30
alunos = {}
provas = []
medias = []


def cadastra_aluno():
    for i in range(x):
        provas.clear()
        nome = str(input('Digite o nome do aluno: '))
        for c in range(1, y+1):
            provas.append(float(input(f'Digite a nota da prova {c}: ')))
        media = round(sum(provas)/y, 2)
        medias.append(round(sum(provas)/y, 2))
        alunos[media] = nome
        print(f'O aluno {nome} teve uma média de {round(sum(provas)/y, 2)}')
        print()


def finalizacao():
    dados = alunos.get(max(medias))
    if dados is not None:
        print(f'O aluno com maior média foi {dados} com a média {max(medias)}')

    dados2 = alunos.get(min(medias))
    if dados2 is not None:
        print(f'O aluno com menor média foi {dados2} com a média {min(medias)}')

    print(f'A média de nota dos alunos foi de {round(sum(medias)/(len(medias)), 2)}')


x = int(input('Quantos alunos tem na sala? '))
y = int(input('Quantas notas serão lançadas por aluno? '))
cadastra_aluno()
finalizacao()

