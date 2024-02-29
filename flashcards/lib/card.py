

class Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return f"Q: {self.question}\nA: {self.answer}"
    
    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self.answer.strip().lower()