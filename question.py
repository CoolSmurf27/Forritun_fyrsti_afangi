class Question:
    def __init__(self, question_str, answer_str):
        self.__question_str = question_str
        self.__answer_str = answer_str

    def get_question(self):
        return self.__question_str

    def check_answer(self, response):
        return response.lower() == self.__answer_str.lower()

