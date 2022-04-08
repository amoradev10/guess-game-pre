import random


file = (r"C:\Users\Alex\Documents\Repositories\guess-games-pre\words.txt")

#declaring a word to guess


def get_word():
    word_test = "test"
    return word_test
    # word_file = open(file)
    # word_choice = random.choice(word_file.read().split())
    # word_file.close()
    # return word_choice



stored_words = []

def runGame():

    word = get_word() 
    word_list =[]
    attempts = 7
    word_solved = False
    continue_play = True
    won = 0
    loss = 0
    print(word)
    

    for character in get_word():
        word_list.append("_")

    while continue_play == True:

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
                            won = won + 1
                            print("YAY! You got the word:", word)
                            print("CONGRADULATIONS YOU WIN!!")
                            print ("Games played:",won, "win(s)", "and" , loss, "loss(es)")
                            play_again = str(input("Would you like to play again? (Y/N)"))
                            print(play_again)
                            if play_again == 'Y':
                                continue_play = True
                                runGame()
                            elif play_again == 'N':
                                continue_play = False
                                print("Thanks for playing!")

                    #not one letter and is an alphabetical word ; guessing word
                    else: 

                        if word == user_input:
                            word_solved = True
                            won = won + 1
                            print("YAY! You got the word:", word)
                            print("CONGRADULATIONS YOU WIN!!")
                            print ("Games played:",won, "win(s)", "and" , loss, "loss(es)")
                            play_again = str(input("Would you like to play again? (Y/N)"))
                            print(play_again)
                            if play_again == 'Y':
                                continue_play = True
                                runGame()
                            elif play_again == 'N':
                                continue_play = False
                                print("Thanks for playing!")


                        else:
                            attempts = attempts -1 
                            print("Incorrect guess for the word! Please try again.")
                            print("You lose a guess if word is repeated")


                #counter to the alpha check
                else:
                    attempts = attempts -1
                    print("Enter a valid character or word... ")
                    print("You lose a guess if invalid characters are inputted")     

        if attempts == 0:
            word_solved = False
            print("You Lose!")
            loss = loss + 1
            print("The word was:", word)

            print ("Games played:",won, "win(s)", "and" , loss, "loss(es)")
           
            play_again = str(input("Would you like to play again? (Y/N)"))
            print(play_again)
            if play_again == 'Y':
                continue_play = True
                runGame()
            elif play_again == 'N':
                continue_play = False
                print("Thanks for playing!")

                
runGame()
