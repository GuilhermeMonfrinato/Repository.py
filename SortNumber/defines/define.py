# defines for main.py #

# imports #
import random
import time

##


def default():
    print('Caso queira sortear um número, digite (SORTEAR)!')
    print('Para sair em qualquer hora do código, por favor digite (EXIT)')
    ans = input('Insira: ')

    ok = True
    while ok:
        ans = ans.lower()
        if ans == 'exit':
            print('[BOT] Fechando...')
            exit()

        if ans == '' or ans != 'sortear':
            ok
            print('[ERROR] Parece que você digitou algo ilegível.')
            ans = input('Insira: ')

        if ans == 'sortear':
            ok = False
            pass

        # commands #

        if ans == 'sortear':
            print('[BOT] Ok, precisamos de um intervalo de números.', end=" ")
            print('\nDigite o número menor para sortearmos.')
            inp = input('Digite: ')
            ok = True
            while ok:
                if inp.isnumeric() is not True:
                    inp = inp.lower()
                    if inp == 'exit':
                        print('[BOT] Fechando...')
                        exit()
                    else:
                        ok
                        print('[ERROR] Parece que você digitou um', end=" ")
                        print('valor não-numérico, por favor', end=" ")
                        print('digite novamente.')
                        inp = input('Insira: ')

                if inp.isnumeric() is True:
                    ok = False
                    pass

            num_init = inp

            print('[BOT] Ok, coletamos seu número inicial,', end=" ")
            print('agora digite um número limite para o sorteador.')
            inp2 = input('Insira: ')

            ok = True
            while ok:
                if inp2.isnumeric() is not True:
                    inp2 = inp2.lower()
                    if inp2 == 'exit':
                        print('[BOT] Fechando...')
                        exit()
                    else:
                        ok
                        print('[ERROR] Parece que você digitou um', end=" ")
                        print('valor não-numérico, por favor', end=" ")
                        print('digite novamente.')
                        inp2 = input('Insira: ')

                if inp2.isnumeric() is True:
                    ok = False
                    pass

            num_limit = inp2
            print('[BOT] Estamos sorteando seu número, por favor aguarde...\n')
            time.sleep(3.0)
            num_limit = int(num_limit)
            num_init = int(num_init)
            num_sorted = random.randint(num_init, num_limit)
            print('[BOT | Finished] Sorteamos um número de acordo', end=" ")
            print('com suas escolhas, veja o resultado abaixo.')
            print(f'\nNúmero mínimo: {num_init}')
            print(f'Número máximo: {num_limit}')
            print(f'\n\nNúmero sorteado pelo BOT: {num_sorted}')

            print('[BOT] Você deseja sortear novamente?')
            response = input('Insira: ')
            response = response.lower()
            if response == 'sim':
                return default()
            else:
                print('[BOT] Ok, obrigado por utilizar.')
                print('[BOT] Fechando.')
                exit()

# end #
