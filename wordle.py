import random

with open("spiele/wordle_words.json", "r") as list_words:
    words = json.load(list_words)

#get random word
todays_word = random.choice(words)
list(todays_word)


#start Play
def start_play():
    print("///////////////////////////")
    global guess
    guess = input("Guess what the word is:").lower()
    print("///////////////////////////")

    list(guess)
    global guess_letters
    guess_letters = []

    if len(guess) > 5 or len(guess) < 5 or any(number in guess for number in "0123456789"):
        print("invalid word")
        print("please start again")
        start_play()

    if len(guess) == 5:
        play_game()
 
def play_game():

    for letters in range(5):
#first letter
        if str(guess[letters]) in todays_word:
            print(f"the letter: {guess[letters]} is in todays word")
            if str(guess[letters]) == str(todays_word[letters]):
                print(f'\033[32m{guess[letters]} is in the right place\033[0m')
                
                #add the letter to guess word
                guess_letters.append(guess[letters])

            else:
                print(f'\033[33m{guess[letters]} is in the wrong place\033[0m')
        else:
            print(f'\033[31mthere is no {guess[letters]} in todays word\033[0m') 
                
        if guess_letters == list(todays_word):
            print('WONNNNNNNNNNN')
            print('///////////////////////////')

tries = 0
while tries < 6:
    start_play() 
    tries += 1
    if tries == 6:
        print("LOSEEEEEEEEEE")



