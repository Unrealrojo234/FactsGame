from tkinter import*
from PIL import ImageTk,Image
from tkhtmlview import*
import time
window = Tk()
window.geometry("700x500")
window.title("QUIZ GAME")
window.resizable(False,False)
window.configure(bg="#8000ff")


#Creating an image
my_image = ImageTk.PhotoImage(Image.open("Quize_Game.py/image01.jpg"))

#Creating input box
e = Entry(window,font=("Arial",20),borderwidth=5,bg="#a0a0a0")
e.place(x=180,y=110)


#Creating functions
def button01():
    name = e.get()
    window2 = Toplevel()
    window2.geometry("650x1500")
    window2.resizable(False,False)
    window2.title(name)
    #Creating title for window2
    title = HTMLLabel(window2,html="<h2>ANSWER THE FOLLOWING QUESTIONS </h2>").pack()

    def submit():
        window3 = Toplevel()
        window3.title("Result")
        window3.geometry("800x500")
        window3.resizable(False,False)
        window3.configure(bg="#00d7d7")


        #Awarding marks
        x = 0
        if A1.get()=='42':
            x+=1
        else:
            x+=0
        if A2.get().lower()=='bhagdad':
            x+=1
        else:
            x+=0
        if A3.get().lower()=='mars':
            x+=1
        else:
            x+=0

        if A4.get().lower()=='siamese twins':
            x+=1
        else:
            x+=0

        if A5.get().lower()=='telekinesis':
            x+=1
        else:
            x+=0

        if A6.get().lower()=='electric eel':
            x+=1
        else:
            x+=0

        if A7.get().lower()=='vatican city':
            x+=1
        else:
            x+=0     

        if A8.get()=='28':
            x+=1
        else:
            x+=0     

        if A9.get()=='47':
            x+=1
        else:
            x+=0     

        if A10.get().lower()=='usain bolt':
            x+=1
        else:
            x+=0     
        marks = int((x/10)*100)
        window2.destroy()


        result_label = Label(window3,bg="#00d7d7",text=f"{name} you have scored\n {marks}%",font=("New Times Roman",30))
        result_label.pack()
    #Placing questions
    q1 = Label(window2,text="1.How many teeth does an adult dog have?",font=("Arial",10)).place(x=10,y=50)
    q2 = Label(window2,text="2.What is the capital city of Afghanistan",font=("Arial",10)).place(x=10,y=100)
    q3 = Label(window2,text="3.Which planet is nicknamed the red-planet",font=("Arial",10)).place(x=10,y=150)
    q4 = Label(window2,text="4.What name is given to twins who their bodies are fussed?",font=("Arial",10)).place(x=10,y=200)
    q5 = Label(window2,text="5.What name is given to the power of lifting objects without touching them?",font=("Arial",10)).place(x=10,y=250)
    q6 = Label(window2,text="6.Which fish is capable of producing over 600 volts of electricity",font=("Arial",10)).place(x=10,y=300)
    q7 = Label(window2,text="7.Name the smallest country in the world",font=("Arial",10)).place(x=10,y=350)
    q8 = Label(window2,text="8.How many days does it take the moon to revolve around the earth",font=("Arial",10)).place(x=10,y=400)
    q9 = Label(window2,text="9.How many counties are in Kenya",font=("Arial",10)).place(x=10,y=450)
    q10 = Label(window2,text="10.Who is the fastest person in the world",font=("Arial",10)).place(x=10,y=500)
    
    #Making answer sheet
    A1 = Entry(window2)
    A1.place(x=450,y=50)
    A2 = Entry(window2)
    A2.place(x=450,y=100)
    A3 = Entry(window2)
    A3.place(x=450,y=150)
    A4 = Entry(window2)
    A4.place(x=450,y=200)
    A5 = Entry(window2)
    A5.place(x=450,y=250)
    A6 = Entry(window2)
    A6.place(x=450,y=300)
    A7 = Entry(window2)
    A7.place(x=450,y=350)
    A8 = Entry(window2)
    A8.place(x=450,y=400)
    A9 = Entry(window2)
    A9.place(x=450,y=450)
    A10 = Entry(window2)
    A10.place(x=450,y=500)
    
    
    #Creating submit button
    submit_button = Button(window2,text="SUBMIT",command=submit,bg="Purple",fg="Blue")
    submit_button.place(x=250,y=650)
    #Marking the quiz 



#Creating labels
label01 = Label(window,bg="#8000ff",text="WELCOME TO QUIZ GAME",font=("Ink Free",40)).place(x=15,y=0)
label02 = Label(window,text="Enter name: ",font=("Arial",20),bg="#8000ff").place(x=15,y=110)
label03 = Label(window,image=my_image,padx=0,pady=10,bg="#8000ff").place(x=-1,y=200)



#Creating button
button01 = Button(window,text="PLAY",command=button01,
                  bg="Green",
                  font=("Javanese Text",15),padx=20).place(x=250,y=300)




window.mainloop()