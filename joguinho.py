palavras = 'Ola Mundo'
inserida = []
chances = 15

while True:

    if chances == 0:
        print('\nAcabaram suas chances, GAME OVER!!!')
        print(f'Chances = {chances}\n')
        print(f'A(s) Palavra(s) era(m) "{palavras}"\n')
        break

    print(f'Chances = {chances}')
    letra = input('Informe uma letra: ')

    if len(letra) > 1:
        print('Eu disse UMA letra! >:( \n')
        continue

    inserida.append(letra)

    if letra in palavras:
        print(f'\nBoa acertou a letra! "{letra}" está na palavra! ;-) ')
        chances -= 1
        print(f'Chances = {chances}\n')
    else:
        print(f'\nPuuuts a letra "{letra}" não esta na palavra! :-( ')
        chances -= 1
        print(f'Chances = {chances}\n')
        inserida.pop()

    palavrasTemp = ''

    for letraPalavra in palavras:
        if letraPalavra in inserida:
            palavrasTemp += letraPalavra
        else:
            palavrasTemp += '_'

    print(f'Palavra = {palavrasTemp}\n')

    if palavrasTemp == palavras:
        print(f'Parabens Voce Acertou a Palavra!! \nPalavra = {palavras}\n')
        break
