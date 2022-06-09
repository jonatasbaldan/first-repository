player_option = list()
player_name = list()

player_name.append(input('Player 1 Nome: '))
player_name.append(input('Player 2 Nome: '))

player_option.append(int(input(f'{player_name[0]}. Escolha Pedra[1], Tesoura[2] ou Papel[3]: ')))
player_option.append(int(input(f'{player_name[1]}. Escolha Pedra[1], Tesoura[2] ou Papel[3]: ')))

player_one_chose = player_option[0]
player_two_chose = player_option[1]

# Verifica se o player 2 é maior que o player 1, se for, o player 1 vence, porque, por exemplo, pedra[1]
# é maior que Tesoura[2], caso contrário, o player 2 vence.

if (player_two_chose > player_one_chose) and (player_two_chose == player_one_chose + 1):
    print(f'{player_name[0]} Ganhou!')

elif player_one_chose == player_two_chose:
    print('Empate!')

else:
    print(f'{player_name[1]} Ganhou!')
