import random

words = [

    "apple",
    "brave",
    "chair",
    "dream",
    "eagle",
    "flame",
    "grape",
    "house",
    "light",
    "stone"
]

#get random word
todays_word = random.choice(words)
list(todays_word)


#start Play
def start_play():
    print("///////////////////////////")
    global guess
    guess = input("Guess what the world is:").lower()
    print("///////////////////////////")

    list(guess)
    global guess_letters
    guess_letters = []

    if len(guess) > 5:
        print("invalid word")
        print("please start again")
        start_play()

    if len(guess) < 5:
        print("invalid word")
        print("please start again")
        start_play()

    if any(number in guess for number in "0123456789"):
        print("invalid word")
        print("please start again")
        start_play()

    if len(guess) == 5:
        play_game()

 
def play_game():
#first letter
        if str(guess[0]) in todays_word:
            print(f"the letter: {guess[0]} is in todays word")
            if str(guess[0]) == str(todays_word[0]):
                print(f'\033[32m{guess[0]} is in the right place\033[0m')
                
                #add the letter to guess word
                guess_letters.append(guess[0])

            else:
                print(f'\033[33m{guess[0]} is in the wrong place\033[0m')
        else:
            print(f'\033[31mthere is no {guess[0]} in todays word\033[0m') 

    #second letter
        if str(guess[1]) in todays_word:
            print("the letter:", guess[1], 'is in todays word')
            if str(guess[1]) == str(todays_word[1]):
                print(f'\033[32m{guess[1]} is in the right place\033[0m')

                #add the letter to guess word
                guess_letters.append(guess[1])

            else:
                print(f'\033[33m{guess[1]} is in the wrong place\033[0m')
        else:
            print(f'\033[31mthere is no {guess[1]} in todays word\033[0m') 

    #third letter
        if str(guess[2]) in todays_word:
            print("the letter:", guess[2], 'is in todays word')
            if str(guess[2]) == str(todays_word[2]):
                print(f'\033[32m{guess[2]} is in the right place\033[0m')

                #add the letter to guess word
                guess_letters.append(guess[2])

            else:
                print(f'\033[33m{guess[2]} is in the wrong place\033[0m')
        else:
            print(f'\033[31mthere is no {guess[2]} in todays word\033[0m') 

    #fourth letter
        if str(guess[3]) in todays_word:
            print("the letter:", guess[3], 'is in todays word')
            if str(guess[3]) == str(todays_word[3]):
                print(f'\033[32m{guess[3]} is in the right place\033[0m')

                #add the letter to guess word
                guess_letters.append(guess[3])

            else:
                print(f'\033[33m{guess[3]} is in the wrong place\033[0m')
        else:
            print(f'\033[31mthere is no {guess[3]} in todays word\033[0m') 

    #fith letter
        if str(guess[4]) in todays_word:
            print("the letter:", guess[4], 'is in todays word')
            if str(guess[4]) == str(todays_word[4]):
                print(f'\033[32m{guess[4]} is in the right place\033[0m')

                #add the letter to guess word
                guess_letters.append(guess[4])

            else:
                print(f'\033[33m{guess[4]} is in the wrong place\033[0m')
        else:
            print(f'\033[31mthere is no {guess[4]} in todays word\033[0m')    

                
        if guess_letters == list(todays_word):
            print('WONNNNNNNNNNN')
            print('///////////////////////////')
        

            

tries = 0
while tries < 3:
    start_play() 
    tries += 1
    if tries == 3:
        print("LOSEEEEEEEEEE")



