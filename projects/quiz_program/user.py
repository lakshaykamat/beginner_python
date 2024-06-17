from quiz import Quiz


class User:
    score = 0

    def __init__(self, name):
        self.name = name

    def increment_score(self):
        self.score += Quiz.get_answer_point()

    def decrement_score(self):
        if self.score > 0:
            self.score -= Quiz.get_answer_point()

    def display_score(self, user_result: tuple[bool, ...]):
        total_questions = len(user_result)
        total_score = total_questions * Quiz.get_answer_point()
        score_user_got = self.score
        print(f"{self.name} has {score_user_got} out of {total_score}")
