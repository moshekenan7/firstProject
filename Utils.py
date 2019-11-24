import os

ERROR_MESSAGE = "Something went wrong.."
SCORES_FILE_NAME = "Scores.txt"


def clean_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def error_message():
    return ERROR_MESSAGE
