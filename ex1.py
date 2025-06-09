def criar_personagem(nome, pv, pe):
    personagem = {"nome": nome, "pv": pv, "pe": pe}
    return personagem

def atacar(personagem):
    personagem['pv'] -= 5
    personagem['pe'] -= 10
    return personagem

def status(personagem):
    print(f'Status de {personagem["nome"]}: \nPV: {personagem["pv"]}\nPE: {personagem["pe"]}')
    
nome = input('Digite o nome do seu personagem: ')
pv = 20
pe = 50

personagem = criar_personagem(nome, pv,pe)

ataque = input('oh não! um monstro está se aproximando! Você irá atacar? (y/n)\n')
stats = 'n'

if ataque == 'y':
    atacar(personagem)
    stats = input('Você foi atacado! Deseja verificar seu status após o ataque? (y/n): \n')
elif ataque == 'n':
    stats = input('Ok! Deseja verificar seu status? (y/n): \n')
else:
    print('Insira uma resposta válida (y/n).')
    stats = input('Deseja verificar seu status? (y/n): \n')

if stats == 'y':
    status(personagem)
else:
    print('Jogo encerrado!')