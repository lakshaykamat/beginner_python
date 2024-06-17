import csv
from typing import List, Tuple


from quiz import Quiz


def load_questions(file_name: str) -> List[Tuple[str, Tuple[str, ...], int]]:
    """
    Convert questions .csv file into a list of tuple in the format

    [question_name, [option1, option2, option3, option4], correct_option_index]
    :param file_name: .csv file name
    :return: List of questions
    """
    questions = []

    try:

        with open(f"QuizProgram/questions/{file_name}", 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header
            for row in csv_reader:
                question = (row[0], tuple(row[1:5]), int(row[5]))
                questions.append(question)

    except FileNotFoundError:
        print(f"{file_name} doesn't exist")
    return questions


def get_question_set(prompt: str) -> Quiz:
    """
    Fetches questions list based on the given prompt (QuestionSet) and returns a Quizs instance.

    :param prompt: The QuestionSet for which questions are requested.
    :return: Quiz instance with questions for the specified QuestionSet.
    """

    # Create a Quiz instance with the questions for the specified QuestionSet
    quiz_instance = Quiz(
        questions=load_questions(prompt)
    )
    return quiz_instance
