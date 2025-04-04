class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def nex_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ").lower()
        self.check_answer(user_answer, question)

    def check_answer(self, u_answer, question):
        if u_answer == question.answer.lower() :
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was {question.answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

