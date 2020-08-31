'''Lista de exercícios 18/08'''
#Atividade um e dois
a = 30
b = 40
c = 20
print(a+b)
print(a*b*c)

#Atividade três
a = 40
b = 40
print(a/b)

#Atividade quatro
a = 50
b = 25
print(a-b)


#Atividade cinco
nome = input('Digite seu nome: ')
print('Como você está,',nome, '?')

#Atividade sete
num_str = input('Digite 123456: ')
num_int = int(num_str)
print( type(num_int),num_int)

#Atividade oito
a = 3
b = 2
print(int(a/b))

#Atividade nove
a = 5.9874
print(round(a,2))

'''=============================================================================='''
''' Lista de exercícios 25/08 '''
'''=============================================================================='''

#Atividade um - L2
print('Comparando os números e os somando!')
a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite o número de comparação: '))

if a + b < c:
    print(float(a+b))
else:
    print('A soma dos números não é menor que', c)

#Atividade dois - L2
print('Pesquisa IBGE - Margens de 55% para cima ou para baixo')
nome = input('Digite seu nome:')
sexo = input('Qual seu gênero [ Somente F ou M ]:')
sexo = sexo.lower()
civil = input('Qual seu estado civil:')
civil = civil.lower()

if sexo == 'f' and civil == 'casada':
    anos = input('Casada à quantos anos:')
else:
    print('Obrigado!')

#Atividade três - L2
num_duvidoso = float(input('Digite um número:'))

if (num_duvidoso%2) == 0:
    print('Par')
else:
    print('Impar')

#Atividade quatro - L2
num_a = int(input('Digite um número:'))
num_b = int(input('Digite outro número:'))

if num_a == num_b:
    num_c = num_a + num_b
    print('A soma dos números é:', num_c)
else:
    num_c = num_a * num_b
    print('A multiplicação dos números é', num_c)

#Atividade cinco - L2
num = float(input('Digite um número: '))

if num >= 0:
    print('O dobro deste número é: ', num*2)
else:
    print('O triplo deste número é: ', num*3)

#Atividade seis - L2
val = input('Digite algo: ')
val2 = input('Digite outra coisa: ')

print(bool(val == val2))
print(bool(val))
print(bool(val2))

# Atividade sete - L2
num = float(input('Digite um número: '))

if (num%2) == 0:
    print(num+5)
else:
    print(num+8)

#Atividade oito - L2
lista = []
for i in range(3):
   novo_num = int(input('Digite um número:'))
   lista.append(novo_num)
print(sorted(lista, reverse=True))

#Atividade nove - L2
lista = []
for i in range(4)
    numeros = int(input('Digite um número: '))
    lista.append(numeros)
print(min(lista), max(lista))

#Atividade dez - L2
nome = input('Qual seu nome? ')
altura = float(input('Qual sua altura? '))
sexo = input('Qual seu sexo [ Somente F/M ]? ')
sexo = sexo.lower()

if sexo == 'm':
    print('Seu peso ideal é', round((72.7 * altura) - 58, 1), 'kg.')
else:
    print('Seu peso ideal é,', round((62.1 * altura) - 44.7, 1), 'kg.')

#Atividade onze - L2
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
print('Seu IMC é de', round(peso/(altura*2), 1))

#Atividade doze - L2
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = float(peso/(altura*2))

if  imc > 30:
    print('Deu ruim pra boné.')
elif imc > 25 and imc <= 30:
    print('Deu ruim.')
elif imc > 18.5 and imc <= 25:
    print('Tá de boa magrão.')
elif imc <= 18.5 and imc >= 0:
    print('Suplementação seria uma boa hein..')
else:
   print('fim do programa')

#Atividade treze - L2
valor = float(input('Digite o valor do produto: '))
n = int(input('Digite a opção de pagamento [1-4]: '))
desc_um = valor*0.10
desc_dois = valor*0.15
valor = round(valor, 2)

if n == 1:
    print('O Valor a ser pago será de', round(valor-desc_um, 2), 'reais.')
elif n == 2:
    print('O valor a ser pago será de', round((valor-desc_dois, 2)), 'reais.')
elif 3 == n:
    print('O valor a ser pago será de', round(valor), 'em duas vezes de', round((valor/2), 2), 'reais.')
elif n == 4:
    print('O valor a ser pago será de', round((valor+desc_um), 2), 'em duas vezes de', ((valor+desc_um)/2),'reais')

#Atividade quatorze - L2
ident = int(input('Escreva o número de matricula do aluno: '))
notas = []
for i in range (3):
   n = float(input("Digite a nota " + str(i+1) + ": "))
   notas.append(n)

me = float(input('Digite a média dos exercícios: '))
ma = (notas[0] + notas[1]*2 + notas[2]*3 + me)/7

print("A média de aproveitamento do aluno de matrícula "+ str(ident) + " foi de:", round(ma, 1))

#Atividade quinze - L2
ident_nome = input('Nome do aluno: ')
ident_num = int(input('Escreva o número de matricula do aluno: '))
notas = []
for i in range(3):
    n = float(input("Digite a nota " + str(i + 1) + ": "))
    notas.append(n)

me = float(input('Digite a média dos exercícios: '))
ma = float((notas[0] + notas[1] * 2 + notas[2] * 3 + me) / 7)

conceito = ()

if ma >= float(90):
    conceito = 'A'
elif float(75) <= ma < float(90):
    conceito = 'B'
elif float(60) <= ma < float(75):
    conceito = 'C'
elif float(40) <= ma < float(60):
    conceito = 'D'
elif ma < float(40):
    conceito = 'E'

if ma >= float(60):
    print("O aluno " + ident_nome + " de matrícula " + str(ident_num) + " com as notas", notas, ",e média de exerícios",
          round(me, 1), " ,teve uma média de aproveitamento de:", round(ma, 1),
          " sendo assim ele está APROVADO com conceito", conceito)

elif ma < float(60):
    print("O aluno " + ident_nome + " de matrícula " + str(ident_num) + " com as notas", notas, ",e média de exerícios",
          round(me, 1), " ,teve uma média de aproveitamento de:", round(ma, 1),
          " sendo assim ele está REPROVADO com conceito", conceito)

#Atividade dezesseis - L2
x = float(input('Digite o valor de X: '))
y = float(input('Digite o valor de Y: '))
z = float(input('Digite o valor de Z: '))

if x == y == z != 0:
   print('Com os valores passados, o triângulo é equilátero')
elif x == y != z != 0 or x == z != y != 0 or z == y != x != 0:
   print('Triângulo isósceles')
elif x != y != z != 0:
   print('Triângulo Escaleno')
else:
   print('Algum número zerado ou negativo. Não é possível montar triângulo')

#Atividade dezessete - L2
valor = float(300.00)
tax1 = float(20.00)
tax2 = float(14.00)
tax3 = float(12.00)

nome = input('Nome do cliente: ')
diaria = int(input('Diárias: '))
if 0 <= diaria < 15:
   print('O cliente:', nome, 'terá de pagar:', (valor*diaria)+tax1)
if 15 == diaria:
   print('O cliente: ', nome, 'Terá de pagar: ', (valor*diaria)+tax2)
if diaria > 15:
   print('O cliente: ', nome, 'Terá de pagar: ', (valor*diaria)+tax3)

#Atividade dezoito - L2
sal = float(input('Valor do salário: '))
prest = float(input('Valor da prestação: '))

emprest_max = sal * 0.30

if prest > emprest_max:
   print('Empréstimo não pode ser concedido')
else:
   print('Empréstimo liberado')

#Atividade Dezenove - L2
a = int(input('digite valor de A: '))
b = int(input('Digite valor de B: '))
c = int(input('Digite valor de C: '))

d = int((b**2) - 4*a*c)
x1 = int(((-b - d**(1/2)) / (2*a)))
x2 = int(((-b + d**(1/2)) / (2*a)))

print('O valor de x 1 é:', x1, 'e o valor de x 2 é:', x2)

#Atividade vinte - L2
dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

n = int(input('Digite um número de 1-7: '))
i = n-1

if 7 < n < 0:
   print('Não é um número válido.')
else:
   print(dias[i])
