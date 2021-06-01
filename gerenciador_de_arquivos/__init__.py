# Gerenciador de arquivos

def verificaArquivo(nome):
    try:
        arq = open(nome, 'rt')
        arq.close
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    arq = open(nome, 'wt+')
    arq.close()

def editarArquivo(arquivo, nome='nome', idade='idade', id='id'):
    arq = open(arquivo, 'at')
    arq.write(f'{nome}|  {idade}  |  {id}\n')
    arq.close()

def lerArquivo(arquivo):
    a = open(arquivo, 'rt')
    print(a.read())

# Elementos de Texto
def criaCabecalho(arquivo):
    arq = open(arquivo, 'at')
    arq.write('------- Registro de Matricula -------\n')
    arq.write(' Nome    | Idade     | ID     \n')

def criaRodape(arquivo):
    arq = open(arquivo, 'at')
    arq.write('')
    arq.write('----- Registro de Matricula.py, Todos os Direitos Reservados -----\n')
