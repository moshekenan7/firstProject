import Utils
import MemoryGame
import GuessGame
from Score import add_score


# the welcome method displays the World of Games headline
def welcome(name):
    str = "Hello " + name
    str += " and welcome to the World of Games (WoG)."
    str += "\nHere you can find many cool games to play."
    return str


# the load_game method displays the optional games to the user and run the chosen game
def load_game():
    str = "\nPlease choose a game to play: \n"
    str += "    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
    str += "    2. Guess Game - guess a number and see if you chose like the computer\n"

    game = input(str)
    if (game != "1") and (game != "2"):
        print(Utils.error_message())
        return
    #print(game)

    difficulty = int(input("\nPlease choose game difficulty from 1 to 5:\n"))
    if (difficulty < 1) or (difficulty > 5):
        print(Utils.error_message())
        return
    #print(difficulty)

    if game == "1":
        #print("chose memory")
        answer = MemoryGame.play(difficulty)
        #print(answer)
        if answer:
            print("you won {} points".format(difficulty))
            add_score(difficulty)
            load_game()
        else:
            print("you lost")
            load_game()
    elif game == "2":
        #print("chose guess")
        answer = GuessGame.play(difficulty)
        #print(answer)
        if answer:
            print("you won {} points".format(difficulty))
            add_score(difficulty)
            load_game()
        else:
            print("you lost")
            load_game()


def main():
    name = input("Please enter your name:")
    print(welcome(name))
    load_game()

if __name__=="__main__":
    main()

