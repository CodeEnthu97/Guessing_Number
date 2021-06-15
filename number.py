from tkinter import*
from PIL import Image,ImageTk
import random

class Guess:
    def __init__(self,root):
        self.root=root
        self.root.geometry("600x393+350+50")
        self.root.title("Guess The Nummber")
        self.root.iconbitmap("images/number.ico")
        self.root.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file=r"images/Numbers.png")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        welc=Label(self.root,text="--- Welcome to  The Game ---",font="timesnewroman 14 bold underline",fg="#58D68D",bg="black",bd=0)
        welc.place(x=160,y=20)

        title=Label(self.root,text="Guess The Number Between 1 to 99",font="timesnewroman 14 bold underline",fg="#DE3163",bg="black",bd=0)
        title.place(x=129,y=70)

        title1=Label(self.root,text="Enter :-",font="timesnewroman 14 bold ",fg="#04B4AE",bg="black",bd=0)
        title1.place(x=70,y=153)

        self.entry_window=Entry(self.root,borderwidth=4,width=25,relief=SUNKEN,bg="#FF7F50",fg="black",font="timesnewroman 14 bold")
        self.entry_window.place(x=170,y=150,height=35)

        self.check=Button(self.root,command=self.check_answer,text="Check",width=15,borderwidth=4,relief=SUNKEN,bg="#FF0040",fg="yellow",font="timesnewroman 10 bold")
        self.check.place(x=248,y=210)

        qui=Button(self.root,text="Quit",width=12,borderwidth=4,relief=SUNKEN,bg="#0A1B2A",font="timesnewroman 10 bold",fg="white",command=self.root.quit)
        qui.place(x=258,y=260)

        self.txt=StringVar()
        self.txt.set("You have 10 attempts remaining! Good Luck")
        self.guess_attempts=Label(self.root,font=("times new roman",13,"bold"),textvariable=self.txt,fg="yellow",bg="black")
        self.guess_attempts.place(x=130,y=320,width=430)

        self.attempts=10
        self.answer=random.randint(1,99)

        
    
    def check_answer(self):
        self.attempts-=1
        self.guess= int(self.entry_window.get())

        if self.answer == self.guess:
            self.txt.set("You Win! Congrats!")
            self.check.pack_forget()
        elif self.attempts == 0:
            self.txt.set("You are out of attempts!")
            self.check.pack_forget()
        elif self.guess<self.answer:
            self.txt.set("Incorrect! You have"+str(self.attempts)+"attempts remaining -> Go Higher")
        elif self.guess>self.answer:
            self.txt.set("Incorrect! You have"+str(self.attempts)+"attempts remaining -> Go Lower")







if __name__ == "__main__":
    root=Tk()
    obj=Guess(root)
    root.mainloop()

