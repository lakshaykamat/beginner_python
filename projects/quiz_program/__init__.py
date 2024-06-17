from question_set import show_sets, is_quiz_exist
from user import User
from quiz_data import get_question_set


def read_user_name() -> str:
    while True:
        name = input("Enter your name: ")
        if len(name) > 3:
            return name
        print("Name length should be greater than 3")


def choose_question_set() -> str:
    while True:
        set_name = input("Choose a question set: ")
        if is_quiz_exist(set_name):
            return set_name
        print("Invalid question set. Please choose again.")


if __name__ == '__main__':
    user_name = read_user_name()
    user = User(user_name)

    show_sets()

    chosen_question_set_name = choose_question_set()
    quiz = get_question_set(chosen_question_set_name)

    user_result = quiz.take_quiz()

    for ans in user_result:
        if ans:
            user.increment_score()

    user.display_score(user_result)
