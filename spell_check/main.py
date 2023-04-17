"""
Day 42: Spelling Checker

Write a function called spelling checker.
This code asks the user to input a word,
and if the user inputs the wrong spelling, it should suggest the correct spelling by asking the user if they meant to
type that word.
If the user says no, it should ask the user to enter the word again.
If the user says yes,
it should return the correct word.
If the word entered by the user is correctly spelled, the function should return
the correct word. Use the module textblob.

"""
import logging

from textblob import TextBlob, Word


# log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
# logging.basicConfig(filename="log.log", level=logging.DEBUG, format=log_format)

def get_one_word_from_user():
    """Ask user input util user enters a single word"""
    counter = 2
    while len((user_input := TextBlob(input("Please enter one word to spellcheck: "))).words) > 1:
        counter -= 1
        if counter <= 0:
            print("Oh, come on, just enter a single word, will you?")
    return user_input.words[-1]


def check_yes_no(msg: str) -> bool:
    return input(f"{msg} ([y]es / [n]o) ").lower() in ['y', 'yes']


def do_spell_check(word: Word):
    res = word.spellcheck()
    logging.debug(f"{res}")

    # if we have more than onw result with score 1.0, return them all
    candidates = list(filter(lambda tup: tup[1] >= 1.0, res))
    if candidates:
        return ",".join([word for word, _ in candidates])
    else:
        # return the candidate with the highest score
        best_choice = max(res, key=lambda item: item[1])
        if check_yes_no(f"\nIs \"{best_choice[0]}\" the word?"):
            return best_choice[0]


def spelling_checker() -> str:
    user_input = get_one_word_from_user()
    return do_spell_check(user_input)


if __name__ == '__main__':
    while True:
        if result := spelling_checker():
            print(f"So, you did mean \"{result}\".")

        if not check_yes_no("Want to try again?"):
            break
