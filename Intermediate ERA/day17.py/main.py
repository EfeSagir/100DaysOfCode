from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
point = 0
QuestionNumber = 0

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_object = Question(question_text, question_answer)
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    user_answer, correct_answer = quiz.next_question()
    quiz.next_question()
    QuestionNumber += 1
    if user_answer == correct_answer.lower():
        point += 1
        print("Correct! You have +1 point.")
    else:
        print(f"Incorrect! The correct answer was: {correct_answer}")
print("Your total point is", point)