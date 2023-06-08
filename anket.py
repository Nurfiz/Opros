class Anket:
    def __init__(self, config):
        self.config = config
        self.length = len(config)

    def add_answers(self, answers: list):
        scores = 0
        for answer in answers:
            db.insert(answer)
            question_number = answer['questionNumber']
            qtype = self.config[question_number].get('type')
            right_answer = self.config[question_number].get('answer')
            qanswer = answer['answerText']
            print(f"Question: {self.get_question(question_number)}")
            print(f"Type: {qtype}")
            print(f"Right Answer: {right_answer}")
            print(f"User Answer: {qanswer}")
            if qtype == 'closed':
                scores += 1 if qanswer == right_answer else 0
            if qtype == 'multiple_choice':
                pass
            if qtype == 'number':
                pass
        return scores

    def get_question(self, k):
        return self.config[k].get('text')