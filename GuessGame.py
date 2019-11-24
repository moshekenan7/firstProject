import random


# the generate_number returns a random number between 1 and difficulty
def generate_number(difficulty):
    return random.randint(1, difficulty)


# the get_guess_from_user method returns the number guessed by the user
def get_guess_from_user(difficulty):
    str1 = "Please guess a number between 1 and {}\n".format(str(difficulty))
    guess = int(input(str1))
    #print(guess)
    return guess


# the compare_results method returns if the user guess was correct
def compare_results(secret_number, guess_number):
    if secret_number == guess_number:
        return True
    else:
        return False


# the play method runs the Guess game
def play(difficulty):
    answer = False
    rand_num = generate_number(difficulty)
    #print("rand_num" + str(rand_num))
    guess_num = get_guess_from_user(difficulty)
    return compare_results(rand_num, guess_num)


