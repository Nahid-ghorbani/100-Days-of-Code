from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.nex_question()

print("You've completed the quiz.")
print(f"You're final score is : {quiz.score}/{quiz.question_number} ")