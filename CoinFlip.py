import random
keep_playing = True
correct_guesses = 0
wrong_guesses = 0
type = True
def game_type(): #ask if they want to play coin or dice game. returns type. coin makes type = True, dice makes type = false
    global type
    game = input('would you like to guess the coin flip or dice roll?\n')
    game = game.lower()
    if game == 'coin' or game == 'coin flip':
        type = True
    elif game == 'dice' or game == 'dice roll':
        type = False
    else:
        print('invalid response!')
        game_type()
    return type
def coin_flip(): #if playing coin then returns heads or tails. if dice then return num 1-6
    random_num = random.randint(1,6)
    if type == True:
        if random_num <= 3:
            return 'heads'
        else:
            return 'tails'
    else:
        return random_num
def get_guess(): #asks for guess based on gametype. returns valid guess.
    if type == True:
        guess = input('Will the coin flip land on heads or tails?\n')
        guess = guess.lower()
        if guess == 'head' or guess == 'heads':
            guess = 'heads'
        elif guess == 'tail' or guess == 'tails':
            guess = 'tails'
        else:
            print('invalid response!')
            get_guess()
    else:
        guess = input('What number will the 6 sided dice land on?\n')
        valid_guesses = [1, 2, 3, 4, 5, 6]
        if int(guess) not in valid_guesses:
            print('invalid response!')
            get_guess()
    return guess
def game(): #gets the guess and answer. Checks if guess was right or wrong and updates history.
    global correct_guesses
    global wrong_guesses
    guess = get_guess()
    answer = coin_flip()
    if type == True:
        print('The coin landed on ' + answer + '!')
    else:
        print('The dice rolled ' + str(answer) + '!')
    if guess == str(answer):
        correct_guesses += 1
        print('You were right!')
    else:
        wrong_guesses += 1
        print('You were wrong!')
    print('Total correct guesses = ' + str(correct_guesses) + '\nTotal wrong guess = ' + str(wrong_guesses))
def play_again(): #After the game this function asks if you would like to play again and return true if yes or false if no
    again = input('Would you like to play again? (Y/N)\n')
    again = again.lower()
    play = False
    if again == 'y' or again == 'yes':
        play = True
    elif again == 'n' or again == 'no':
        play = False
    else:
        print('invalid response!')
        play_again()
    return play

game_type()
while keep_playing == True:
    game()
    keep_playing = play_again()
print('Goodbye!')