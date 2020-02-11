import os
import definer


def get_word():
    word = definer.get_word()
    return word.title()


def end_game(end=True):

    if end:
        print("Congrats! You Win!")
    else:
        print("You Lose!")

    print("The Word was: {}".format(word))
    print("Definition:")
    for item in definition:
        print(item.title())
    print("\nDefinition by ldoceonline.com".center(10))


try:
    f = open("words.txt")
except IOError:
    definer.write_word_file()


game_state = True

while game_state:
    print("loading Game...")

    while True:

        word = get_word()
        definition = definer.definer(word)
        if not definition:
            continue
        else:
            break

    player_word = ["*" for i in word]
    miss_list = []


    def print_player_word():
        print("Word:\t" + "".join(player_word))


    def print_miss_list():
        print("Misses:\t" + "".join(miss_list))


    def print_rem_chances():
        print("Remaining Chances:", (len(word) + 1) - len(miss_list))


    os.system('cls' if os.name == 'nt' else 'clear')

    while "*" in player_word:
        if len(miss_list) == len(word) + 1:
            end_game(False)
            break
        else:
            print_player_word()
            print_miss_list()
            print_rem_chances()
            print()

            char = input("Input your guess:\n")
            if char.isnumeric() or char == "" or len(char) > 1:
                while not char.isalpha() or char == "" or len(char) > 1 or char in miss_list:
                    print("Please Enter a Letter!")
                    char = input("Input your guess:\n")

            if char.lower() in word.lower():
                for i in range(len(word)):
                    if word[i].lower() == char.lower():
                        player_word[i] = word[i]
            elif char.lower() in miss_list:
                pass
            else:
                miss_list.append(char)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        end_game()

    replay = input("\nreplay? (y/n)\n")
    if replay.lower() == 'n':
        game_state = False
