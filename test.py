import random

def get_word():
    file = (r"C:\Users\Alex\Documents\Repositories\guess-games-pre\words.txt")
    with open(file, "r") as word_file:
        return random.choice(word_file.readlines()).strip()

correct_word = get_word()

print (correct_word)