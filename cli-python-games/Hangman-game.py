class HangmanGame:
    """
    Simple terminal game of hang man.
    """
    def __init__(self):

        self.empty_space_to_fill = list()
        self.empty_space = list()
        self.word_choosed = list()
        self.word_choosed_string = str()
        self.attempts_error = int()
        self.attempts_score = int()
        self.human_parts_to_fill = [' ', ' ', ' ', ' ', ' ', ' ']
        self.human_parts = ['o', '|', '/', '\\', '/', '\\']
        self.scenery = None

    def choose_word(self, word: str):
        """
        Method to convert the chose word string to a list of characters and fill the display space
        """
        for letter in word:
            self.word_choosed_string = word
            self.word_choosed.append(letter)

            if letter != ' ':
                self.empty_space_to_fill.append(' ')
                self.empty_space.append('_')
            else:
                self.empty_space_to_fill.append(' ')
                self.empty_space.append(' ')

    def choose_letter(self, letter: str):
        """
        Method to verify if the letter is in word, if it is true, the display space will be filled with the letter.
        """
        if letter in self.word_choosed and letter not in self.empty_space_to_fill:
            for occurence in range(0, self.word_choosed.count(letter)):
                self.empty_space_to_fill[self.word_choosed.index(letter)] = letter
                self.word_choosed[self.word_choosed.index(letter)] = ' '

    def display_word_to_fill(self):
        """
        Method to display the words and empty space
        """
        for letter in self.empty_space_to_fill:
            if letter != None:
                print(letter, end=' ')

        print()
        for space in self.empty_space:
            if space != None:
                print(space, end=' ')

    def display_scenery(self) -> str:
        """
        Method to return the scenery.
        """
        return (f'----------------------------------\n'
                        f'                |----------------| \n'
                        f'                |                | \n'
                        f'                {self.human_parts_to_fill[0]}                | \n'
                        f'               {self.human_parts_to_fill[2]}{self.human_parts_to_fill[1]}{self.human_parts_to_fill[3]}               | \n'
                        f'               {self.human_parts_to_fill[4]}{self.human_parts_to_fill[5]}                |\n'
                        f'                                 | \n'
                        f'________________________________/-\\\n')


JogoDaForca = HangmanGame()

print('-+-'*20)
print(' ' * 20 + 'JOGO DA FORCA')
print('-+-'*20)
print(JogoDaForca.display_scenery())
print('='*20)
JogoDaForca.choose_word(str(input('ESCOLHA UMA PALAVRA: ')))
for i in range(0, 20):
    print('.')

while JogoDaForca.attempts_error != 6:
    print('=' * 20)
    print(JogoDaForca.display_scenery())
    JogoDaForca.display_word_to_fill()
    print('\n' + '=' * 20)
    letra_escolhida = str(input('ESCOLHA UMA LETRA: '))

    if letra_escolhida in JogoDaForca.word_choosed and letra_escolhida not in JogoDaForca.empty_space_to_fill:
        JogoDaForca.choose_letter(letra_escolhida)
        JogoDaForca.attempts_score += 1

    else:
        JogoDaForca.human_parts_to_fill[JogoDaForca.attempts_error] = JogoDaForca.human_parts[JogoDaForca.attempts_error]
        JogoDaForca.attempts_error += 1

    if len(JogoDaForca.word_choosed_string) == JogoDaForca.attempts_score:
        print(JogoDaForca.display_scenery())
        print(JogoDaForca.display_word_to_fill())
        print('=' * 30)
        print(' ' * 8 + 'VOCÊ GANHOU!')
        print('=' * 30)
        break

if JogoDaForca.attempts_error == 6:
    print(JogoDaForca.display_scenery())
    print(JogoDaForca.display_word_to_fill())
    print('=' * 30)
    print(' ' * 8 + 'VOCÊ PERDEU!')
    print('=' * 30)
