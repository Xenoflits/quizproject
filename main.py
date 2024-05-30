from question_model import Question
from data import question_data

new_question_list = []
for questions in question_data:
    nq = Question(questions["text"],questions["answer"])
    new_question_list.append({"text":nq.text,"answer":nq.answer})

for questions in new_question_list:
    print(questions["answer"])