import random
from re import T



#declaring a word to guess
def get_word():
    file = (r"C:\Users\Alex\Documents\Repositories\guess-games-pre\words.txt")
    with open(file, "r") as word_file:
        return random.choice(word_file.readlines()).strip()

word = get_word()
word_list =[]

def runGame(word,word_list):

    attempts = 7
    word_solved = False

    for character in get_word():
        word_list.append("_")

    # initiating loop for game check
    #checking if the attempts are more than 0 and word has not been solved
    while attempts > 0 and not word_solved:

        check_input = False
    
        #checking if alphanumeric
        while not check_input:

            #gets user input
            user_input = input("Guess a letter: ")
            
            check_input = user_input.isalpha()

            if user_input.isalpha():

                if len(user_input) == 1:
                    if user_input in word:

                        for position in range(len(word)):
                            if word[position] == user_input: 
                                word_list[position] = user_input

                    else:
                        attempts = attempts -1
                        print("Incorrect value, -1 guess...")

                    print(word_list)


                    if "_" in word_list:
                        word_solved = False
                    else:
                        word_solved = True
                        print("YAY! You got the word:", word)
                        print("CONGRADULATIONS YOU WIN!!")


                #not one letter and is an alphabetical word ; guessing word
                else: 

                    if word == user_input:
                        word_solved = True
                        print("YAY! You got the word:", word)
                        print("CONGRADULATIONS YOU WIN!!")

                    else:
                        attempts = attempts -1 
                        print("Incorrect guess for the word! Please try again.")
                        print("You will lose a guess if word is repeated")



            #counter to the alpha check
            else:
                print("Enter a valid character or word... ")
                print("You will lose a guess if invalid characters are inputted")
    if attempts == 0:
        word_solved = False
        print("You Lose!")
runGame(word, word_list)
