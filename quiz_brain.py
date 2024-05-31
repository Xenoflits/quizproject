class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def still_has_questions(self):
        print(f'{self.question_number < len(self.question_list)}')
        return self.question_number < len(self.question_list)
    
    def next_question(self):
            
        while self.still_has_questions() == True:
            current_question = self.question_list[self.question_number]['text']
            current_number = self.question_number
            answer = input(f'Q. {current_number+1}: {current_question}? True/False Current score: {self.score} \n')
            if self.check_answer(answer, self.question_list[self.question_number]["answer"]):
               self.question_number += 1
               self.score += 1
               self.winner()
            else:
                print("wrong answer, start again")
                break
    
    def check_answer(self, answer, real_answer):
    
        return answer == real_answer
    
    def winner(self):
        print('You have won: Score 12 points') 
    