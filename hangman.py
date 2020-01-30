import os
from random_word import RandomWords
from definer import find


def get_word():
    r = RandomWords()
    word = r.get_random_word(hasDictionaryDef="true", excludePartOfSpeech="verb,adverb,pronoun,preposition,adjective")
    return word.title()


print("loading Game...")

while True:
    try:
        word = get_word()
        definition = find(word).title()
    except IndexError:
        continue
    break

player_word = ["*" for i in word]
miss_list = []


def print_player_word():
    print("Word: " + "".join(player_word))


def print_miss_list():
    print("Misses: " + "".join(miss_list))


os.system('cls' if os.name == 'nt' else 'clear')

while "*" in player_word:
    if len(miss_list) == len(word):
        print("You Lose!\nThe Word was: {}".format(word))
        print("Definition: {}".format(definition))
        print("Defination by The Free Dictionary.com")
        break
    else:
        print_player_word()
        print_miss_list()
        print()

        char = input("Input your guess:\n")
        if char.isnumeric() or char == "" or len(char) > 1:
            while not char.isalpha() or char == "" or len(char) > 1:
                print("Please Enter a Letter!")
                char = input("Input your guess:\n")

        if char.lower() in word.lower():
            for i in range(len(word)):
                if word[i].lower() == char.lower():
                    player_word[i] = word[i]
        else:
            miss_list.append(char)
    os.system('cls' if os.name == 'nt' else 'clear')
else:
    print("Congrats! You Win!")
    print("The Word was: {}".format(word))
    print("Definition: {}".format(definition))
    print("Defination by The Free Dictionary.com")
