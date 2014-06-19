import random
import time

'''
takes a list of tuple pairs for questions
example [('what is my name?','azuriah'),('what is my favorite color?','blue')]

call
if __name__ == '__main__':
    test.Test(questions, #howmanyquestions)
from another file
'''

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


class gTest:

    def __init__(self, questions, choices):
        self.questions_dict = dict(questions)
        self.x = random.choice(questions)[0]
        self.choices = int(choices)
        self.answers = list()
        self.question = dict()
        self.answer = self.questions_dict[self.x]
        self.answer_letter = None
        self.get_answers()

    def get_answers(self):
        new_set = list(self.questions_dict.items())
        while len(self.answers) < self.choices:
            random.shuffle(new_set)
            y = random.choice([b for a, b in dict(new_set).items() if a != self.x])
            self.answers.append(y)
            self.answers = list(set(self.answers))
        self.make_list()

    def make_list(self):
        self.answers.append(self.answer)
        values = self.answers
        random.shuffle(values)
        values = [{letters[i]: values[i]} for i in range(len(values))]
        for x in values:
            for i in x.keys():
                if x[i] == self.answer:
                    self.answer_letter = i
                    break
        self.question[self.x] = values

class Test:
    
    def __init__(self, questions, choices, language = False, reading = False):
        self.initialize = questions
        self.choices = choices
        self.language = language
        self.reading = reading
        self.key = gTest(self.initialize, self.choices)
        self.question = self.key.question
        self.answer = self.key.answer_letter
        self.x = self.key.x
        self.check = None
        self.start()

    def check_answer(self):
        if self.check == self.answer:
            print('correct')
            key = gTest(self.initialize, self.choices)
            self.question = key.question
            self.answer = key.answer_letter
            self.x = key.x
            time.sleep(1)
            self.start()
        else:
            print('incorrect')
            time.sleep(1)
            self.start()

    def start(self):
        answers = []
        reading = []
        question = []
        if self.language:            
            for i in self.question[self.x]:
                if self.reading:
                    if list(i)[0] == self.answer:
                        if len(i[list(i)[0]].split()) > 1:
                            question.append('%s: %s' % (self.x, i[list(i)[0]].split(' ',1)[0]))
                        else: question.append('%s' % self.x)
                try: answers.append('%s: %s' % (list(i)[0], i[list(i)[0]].split(' ',1)[1]))
                except IndexError: answers.append('%s: %s' % (list(i)[0], i[list(i)[0]].split(' ',1)[0]))
            if not self.reading: question.update(self.x)
        else:
            for i in self.question[self.x]:
                answers.append('%s: %s' % (list(i)[0], i[list(i)[0]]))
            question.append(self.x)                
        print('question: '+' '.join(question))
        for x in answers:
            print(x)
        answer = input('answer: ')
        self.check = answer
        self.check_answer()
        
