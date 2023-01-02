# defs - main.py #

def createLists():
    options = title = 'null'

    print('Seja bem-vindo ao Criador de Listas.', end='\n')
    print('Para começar digite uma palavra maior de de (2)', end=' ')
    print('caractéres e menor de (15) caractéres para o título da Lista:')
    title = str(input(''))
    ok = True
    while ok:  # title
        ok
        if len(title) > 2 and len(title) <= 15:
            break
        else:
            print('[ERRO] Por favor digite uma palavra maior de', end=' ')
            print('de (2) caractéres e menor de (15) caractéres:')
            title = str(input(""))
            ok

    '''##'''

    print('Agora digite a quantidade de opções', end=' ')
    print('que seu menu terá(entre [2] e [7]):')
    options = int(input(''))
    while ok:  # options
        ok
        if options <= 7 and options >= 2:
            break
        else:
            print('[ERRO] Por favor digite a quantidade de', end=' ')
            print('opções entre [2] e [7]: ')
            options = int(input(""))
            ok

    opt = list(range(options))
    x = 0
    while ok:
        if x < len(opt):
            opt[x] = input(f'Digite um valor para o indice {x}: ')
            print('Lista atualmente está: ', opt)
            x += 1
        else:
            break
    print(f'\n\n\nResultado final:\n: {title}{opt} :')
    exit()

# #