from question import Question

class ChoiceQuestion(Question):
    def __init__(self, question_str):
        super().__init__(question_str, '')
        self.__choices = []
        self.__correct_choice = -1

    def add_choice(self, choice, is_correct=False):
        self.__choices.append(choice)
        if is_correct:
            self.__correct_choice = len(self.__choices)

    def check_answer(self, response):
        return response == str(self.__correct_choice)

    def get_question(self):
        question_str = super().get_question()
        for i, choice in enumerate(self.__choices):
            question_str += f"\n{i + 1}. {choice}"
        return question_str