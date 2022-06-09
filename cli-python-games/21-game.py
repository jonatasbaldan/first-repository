import random

continue_game = 1

while continue_game == 1:

    list_of_cards = list()

    for i in range(1, 14):
        for j in range(0, 4):
            list_of_cards.append(i)

    random.shuffle(list_of_cards)

    print('=' * 20)
    player_name = input('Qual o seu nome? ')
    print('=' * 20)

    player_hand = list()

    while True:
        print('=' * 21)
        player_choise = int(input('Descer quantas cartas: '))

        for i in range(0, player_choise):
            player_hand.append(list_of_cards.pop())

        print('A sua mão é: ')
        for card in player_hand:
            print(card, end=', ')

        print('\nSoma das cartas: ', sum(player_hand))

        if sum(player_hand) == 21:
            print('='*21)
            print(f'{player_name}, VOCÊ GANHOU!')
            print('=' * 21)
            break

        elif sum(player_hand) > 21:
            print('=' * 21)
            print(f'{player_name}, VOCÊ PERDEU!')
            print('=' * 21)
            break

    continue_game = int(input('COMEÇAR NOVAMENTE? [1]SIM [0]NÃO: '))
