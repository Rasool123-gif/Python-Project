from quizmanager import QuizManager

class QuizApp:

    def __init__(self,Q):
        self.username=""
        self.QUIZ_FOLDER=Q
        self.qm=QuizManager(self.QUIZ_FOLDER)

    def startup(self):
        self.greeting()
        self.username=input("What is your name")
        print(f'Welcome,{self.username}!')
        print()

    def greeting(self):
        print("********************")
        print("Welcome to PyQuiz")
        print("********************")
        print()

    def menu_header(self):
        print("--------------------")
        print("please make a selection:")
        print("(M): Repeat this menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit the Program")

    def menu_error(self):
        print("That's not a valid selection.please try again")

    def goodbye(self):
        print("********************")
        print(f'Thanks for using PyQuiz, {self.username}!')
        print("********************")

    def menu(self):
        self.menu_header()
        selection=""
        while(True):
            selection=input("Selection? ")
            if(len(selection)==0):
                self.menu_error()
                continue
            selection=selection.capitalize()
            if(selection[0]=='E'):
                self.goodbye()
                break
            elif selection[0]=='M':
                self.menu_header()
                continue
            elif selection[0]=='L':
                print("Available Quizzes are:")
                self.qm.list_quizzes()
                print("********************")
                continue
            elif selection[0]=='T':
                try:
                    quiznum=int(input("Quiz number:"))
                    print(f"You have selected quiz {quiznum}")
                    self.qm.take_quiz(quiznum,self.username)
                    self.qm.print_results()
                    dosave=input("Save the results? (y/n):")
                    dosave=dosave.capitalize()
                    if len(dosave)>0 and dosave[0]=='Y':
                        self.qm.save_results()
                except:
                    self.menu_error()
            else:
                self.menu_error()

    def run(self):
        self.startup()
        self.menu()

if __name__=='__main__':
    app=QuizApp("Quizzes")
    app.run()