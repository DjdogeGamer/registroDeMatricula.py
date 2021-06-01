# Pacotes
import time
from gerenciador_de_arquivos import *

# Var
arqMatricula = 'matricula_alunos.txt'
aluno = []
dadosAluno = []
c = 1
nome = ''
idade = ''
id = ''
sair = ''

# Inicio
print('-' * 30)
print('[ Matricula dos Alunos v1.0]')
print('-' * 30)

verificaArquivo(arqMatricula)
criarArquivo(arqMatricula)
criaCabecalho(arqMatricula)

# Registro / Input
while sair != 'S' and 'S':
    nome = input(f'Digite o nome do aluno [{c}]: ')
    idade = input(f'Digite a idade do aluno [{c}]: ')
    id = input(f'Digite o ID do aluno: [{c}] ')

    dadosAluno.clear()
    dadosAluno.append(nome)
    dadosAluno.append(idade)
    dadosAluno.append(id)
    aluno.append(dadosAluno[:])
    editarArquivo(arqMatricula, nome, idade, id)
    c = c + 1
    sair = input('Deseja terminar o registro? (S/N): ')

# OutPut
criaRodape(arqMatricula)

print('-----Matricula dos Alunos-----')
for i, v in enumerate(aluno):
    time.sleep(0.5)
    print(i, v)

print('\nRegistrando a matricula...')
time.sleep(3)

print('\nA matricula foi registrada com sucesso!\n'
      'verifique a saida, o arquivo de texto provavelmente foi criado.\n')

while True:
    ler = input('Deseja ler o arquivo criado? (S/N) ')

    if ler == 'S':
        print('\nnome do arquivo: '+arqMatricula)
        lerArquivo(arqMatricula)
    if ler == 'N':
        break

print('\nFechando o Programa...\n')
time.sleep(5)
print('-'*15)
print('FIM DO PROGRAMA')
print('-'*15)
