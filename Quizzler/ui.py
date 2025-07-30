from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=10,bg=THEME_COLOR)

        self.label=Label(text="Score:0",bg=THEME_COLOR,fg="White",font=("Arial", 16, "bold") )
        self.label.grid(row=0,column=1,pady=20)


        self.canvas=Canvas(height=250,width=300)
        self.question=self.canvas.create_text(150,125,width= 280,text="Hello", font=("Arial", 20, "italic"),fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,padx=20)

        self.t_img=PhotoImage(file="images//true.png")

        self.T_button=Button(image=self.t_img,highlightthickness=0,borderwidth=0,command=self.t_check_answer)
        self.T_button.grid(row=2,column=0,pady=20)

        self.f_img = PhotoImage(file="images//false.png")

        self.F_button = Button(image=self.f_img,highlightthickness=0,borderwidth=0,command=self.f_check_answer)
        self.F_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.window.config(bg=THEME_COLOR)
            self.label.config(text=f"Score:{self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.itemconfig(self.question,text="You have reached the end of the TRIVIA.")
            self.T_button.config(state="disabled")
            self.F_button.config(state="disabled")


    def t_check_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def f_check_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self,check):
        if check:
            self.window.config(bg="Green")
        else:
            self.window.config(bg="Red")

        self.window.after(1000,self.get_next_question)
