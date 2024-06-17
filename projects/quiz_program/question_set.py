import os


def show_sets() -> None:
    """
    Display available question sets
    """
    file_names = os.listdir('questions')
    print("Available question sets:")
    # Iterate over each enum member and print its name
    for question_set in file_names:
        print(question_set)


def is_quiz_exist(file_name: str) -> bool:
    file_names = os.listdir('questions')
    return file_name in file_names
