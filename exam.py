class Exam:
    def __init__(self):
        self.__questions = []

    def add_question(self, question):
        self.__questions.append(question)

    def take(self):
        self.__points = 0
        for question in self.__questions:
            print(question.get_question())
            response = input()
            if question.check_answer(response):
                print("True")
                self.__points += 1
            else:
                print("False")
            print()

    def get_points(self):
        return self.__points

    def get_num_questions(self):
        return len(self.__questions)

    def __repr__(self):
        return '\n'.join([str(question) for question in self.__questions])
