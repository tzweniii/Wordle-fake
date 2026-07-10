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
    global guess
    guess = input("Guess what the world is:")

    if len(guess) > 5:
        print("invalid word")
        print("please start again")
        start_play()

    if len(guess) < 5:
        print("invalid word")
        print("please start again")
        start_play()

        
    if len(guess) == 5:
        list(guess)
        global guess_letters
        guess_letters = []
        play_game()
 
def play_game():
#first letter

        if str(guess[0]) in todays_word:
            print("the letter:", guess[0], 'is in todays word')
            if str(guess[0]) == str(todays_word[0]):
                print(guess[0], 'is in the right place')
                
                #add the letter to guess word
                guess_letters.append(guess[0])

            else:
                print(guess[0], 'is in the wrong place')
        else:
            print('there is no', guess[0], 'in todays word')

    #second letter
        if str(guess[1]) in todays_word:
            print("the letter:", guess[1], 'is in todays word')
            if str(guess[1]) == str(todays_word[1]):
                print(guess[1], 'is in the right place')

                #add the letter to guess word
                guess_letters.append(guess[1])

            else:
                print(guess[1], 'is in the wrong place')
        else:
            print('there is no', guess[1], 'in todays word')

    #third letter
        if str(guess[2]) in todays_word:
            print("the letter:", guess[2], 'is in todays word')
            if str(guess[2]) == str(todays_word[2]):
                print(guess[2], 'is in the right place')

                #add the letter to guess word
                guess_letters.append(guess[2])

            else:
                print(guess[2], 'is in the wrong place')
        else:
            print('there is no', guess[2], 'in todays word')

    #fourth letter
        if str(guess[3]) in todays_word:
            print("the letter:", guess[3], 'is in todays word')
            if str(guess[3]) == str(todays_word[3]):
                print(guess[3], 'is in the right place')

                #add the letter to guess word
                guess_letters.append(guess[3])

            else:
                print(guess[3], 'is in the wrong place')
        else:
            print('there is no', guess[3], 'in todays word')

    #fith letter
        if str(guess[4]) in todays_word:
            print("the letter:", guess[4], 'is in todays word')
            if str(guess[4]) == str(todays_word[4]):
                print(guess[4], 'is in the right place')

                #add the letter to guess word
                guess_letters.append(guess[4])

            else:
                print(guess[4], 'is in the wrong place')
        else:
            print('there is no', guess[4], 'in todays word')    

                
        if guess_letters == list(todays_word):
            print('WONNNNNNNNNNN')
        else:
             start_play()


start_play() 


