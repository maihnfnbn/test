def welcome():
    player_name = input('Hi! What is your name? ')
    need_explanation = input('Welcome {}! Do you know how to play hangman? Y/N '.format(player_name))
    while ['Y','N'].count(need_explanation.upper()) == 0:
        need_explanation = input('Please choose Y or N ')
    if need_explanation.upper() == 'N':
        print('Computer will generate a hidden word, you have to guess what the word is letter by letter.')
        print('You may get some letters wrong, but if it is more than 5 times, it is game over.')
        print('Good luck!')
    else: print("Let's start!")
welcome()

word_list = ['word', 'useless', 'appliance', 'trot', 'stain', 'blushing', 'immense', 'lip', 'file', 'festive', 'attractive', 'sign']

from random import randint
def generate_word():
    word_index = randint(0, len(word_list))
    generated_word = word_list[word_index]
    list_of_characters = list(generated_word)
    return list_of_characters

play_word = generate_word()
shown = []
for letter in play_word:
    shown.append('_')

print('Your first word is {}'.format(shown))

alphabet = 'ABCDEFGHIJKLMNOQRSTUVW'
guess = input('Make your guess (1 letter only) ')
wrong_count = 0

while len(guess) > 1 or guess.upper() not in alphabet:
    guess = input('Your guess is not valid, please try again! ')

while guess in alphabet and guess not in play_word and wrong_count < 5:
    guess = input('Letter {} is not in the word, please try again '.format(guess.upper()))
    wrong_count += 1

while guess in play_word and wrong_count < 5:
    for i in range(0,len(play_word)):
        if play_word[i] == guess:
            shown[i] = guess

if wrong_count == 5 and shown.count('_') > 0:
    print('Game over')
    print('You lose')
