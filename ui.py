from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"



class Quizzler:

    def __init__(self, quiz: QuizBrain):
        self.question = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg = THEME_COLOR)

        self.score_label = Label(text = "Score: 0", bg = THEME_COLOR)
        self.score_label.grid(row= 0, column = 1)

        self.canvas = Canvas(width = 300, height = 250)
        self.question_text = self.canvas.create_text(150, 120, text = "Question",width = 280,font =("Ariel", 20, "italic"))
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)


        self.tick = PhotoImage(file="images/true.png")
        self.cross = PhotoImage(file="images/false.png")
        self.right_button = Button(image = self.tick, command = self.true_res)
        self.right_button.grid(row = 2, column = 0)
        self.wrong_button = Button(image = self.cross, command = self.false_res)
        self.wrong_button.grid(row = 2, column = 1)
        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.question.still_has_questions():
            self.score_label.config(text = f"Score: {self.question.score}")
            next_que = self.question.next_question()
            self.canvas.itemconfig(self.question_text, text = next_que)
        else:
            self.canvas.itemconfig(self.question_text, text = "You have reached end of quiz")
            self.right_button.config(state = "disabled")
            self.wrong_button.config(state = "disabled")

    def true_res(self):
        is_true=self.question.check_answer("True")
        self.feedback(is_true)

    def false_res(self):
        is_false = self.question.check_answer("False")
        self.feedback(is_false)

    def feedback(self,x):
        if x:self.canvas.config(bg = "green")

        else: self.canvas.config(bg = "red")
        self.window.after(1000, func=self.next_question)
