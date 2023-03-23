import sys
import datetime
import random

#Quiz Class 
class Quiz:

    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0
        self.completion_time=0

    #Display the details of the quiz
    def print_header(self):
        print("********************")
        print(f"Quiz Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Questions: {len(self.questions)}")
        print(f"Total Points: {self.total_points}")
        print("*********************")

    #Display the results of the quiz or stores the result in a file
    def print_results(self, quiztaker,thefile=sys.stdout):
        print("********************",file=thefile,flush=True)
        print(f"Results for {quiztaker}",file=thefile,flush=True)
        print(f"Date: {datetime.datetime.today()}",file=thefile,flush=True)
        print(f"Questions: {self.correct_count} out of {len(self.questions)} correct",file=thefile,flush=True)
        print(f"Score: {self.score} points out of possible {self.total_points}",file=thefile,flush=True)
        print("********************")

    #Take quiz function 
    def take_quiz(self):
        self.score = 0       
        self.correct_count = 0
        self.completion_time=0
        random.shuffle(self.questions)
        start=datetime.datetime.now()
        for q in self.questions:
            q.is_correct = False
        self.print_header()
        for q in self.questions:
            q.ask()
            if (q.is_correct):
                self.correct_count += 1
                self.score += q.points
        end=datetime.datetime.now()
        self.completion_time=end-start
        print("********************")
        return (self.score, self.correct_count, self.total_points,self.completion_time)

#Question class for creating Questions to the quiz
class Question:

    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False

#True or False Class
class QuestionTF(Question):

    def __init__(self):
        super().__init__()

    #Take the response from the user and have a look on the answer
    def ask(self):
        while(True):
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("?")
            if len(response) == 0:
                print("sorry, that's not a valid response. Please try again")
                continue
            response = response.lower()
            if response[0] != "t" and response[0] != "f":
                print("sorry, that's not a valid response. Please try again")
                continue
            if response[0] == self.correct_answer:
                self.is_correct = True
            break

#Multiple Choice Class
class QuestionMC(Question):

    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while(True):
            print(self.text)
            for a in self.answers:
                print(f"({a.name}) {a.text}")
            response = input("?")
            if len(response) == 0:
                print("sorry, that's not a valid response. Please try again")
                continue
            response = response.lower()
            if response[0] == self.correct_answer:
                self.is_correct = True
            break

#Answer Class to store the answers
class Answer:
    def __init__(self):
        self.text = ""
        self.name = ""