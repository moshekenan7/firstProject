import random
import time
import Utils


# the generate_sequence method generates sequence of random numbers and displays it for 0.7 seconds
def generate_sequence(difficulty):
    arr = []
    for i in range(1,difficulty+1):
        rand_num = random.randint(1, 101)
        arr.append(rand_num)

    print(arr)
    time.sleep(700/1000)
#    time.sleep(700/1000*difficulty)

    Utils.clean_screen()
    return arr


# the get_list_from_user method returns a list of numbers from the user input
def get_list_from_user(difficulty):
    print("After seeing the numbers enter the numbers you saw, each one separated with Enter.\n")
    arr = []
    for i in range(1,difficulty+1):
        in_num = int(input())
        arr.append(in_num)

    #print(arr)
    return arr


# the is_list_equal method returns if the user answer was correct
def is_list_equal(list_a, list_b):
    if list_a == list_b:
        return True
    else:
        return False


# the play method runs the Memory game
def play(difficulty):
    generated_list = generate_sequence(difficulty)
    guessed_list = get_list_from_user(difficulty)

    return is_list_equal(generated_list, guessed_list)
