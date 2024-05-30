class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def next_question(self):
      
        max_questions = len(self.question_list)
        while self.question_number < max_questions:
            current_question = self.question_list[self.question_number]['text']
            current_number = self.question_number
            answer = input(f'Q. {current_number+1}: {current_question}? True/False \n')
            self.question_number += 1