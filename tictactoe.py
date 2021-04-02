from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("GUI")
window.geometry("400x460")

# top and bottom frame
top_frame = Frame(window, width = 400, height = 60, bg = "grey")
top_frame.pack()

bottom_frame = Frame(window, width = 400, height = 400, bg = "green")
bottom_frame.pack(side = BOTTOM)


Xor0 = True
count = 0
win = False


# check if win
def winlol():
    global count
    global win
    if b1.get() == "X" and b2.get() == "X" and b3.get() == "X":
        answer = messagebox.showinfo("Glückwunsch!", "##############X hat gewonnen##############")
        win = True
        disable()
    elif b1.get() == "X" and b4.get() == "X" and b7.get() == "X":
        amswer = messagebox.showinfo("Glückwunsch!", "##############X hat gewonnen##############")
        win = True
        disable()
    elif b1.get() == "X" and b5.get() == "X" and b9.get() == "X":
        amswer = messagebox.showinfo("Glückwunsch!", "##############X hat gewonnen##############")
        win = True
        disable()
    elif b9.get() == "X" and b6.get() == "X" and b3.get() == "X":
        answer = messagebox.showinfo("Glückwunsch!", "##############X hat gewonnen##############")
        win = True
        disable()
    elif b9.get() == "X" and b8.get() == "X" and b7.get() == "X":
        answer = messagebox.showinfo("Glückwunsch!", "##############X hat gewonnen##############")
        win = True
        disable()
    elif b5.get() == "X" and b4.get() == "X" and b6.get() == "X":
        answer = messagebox.showinfo("Glückwunsch!", "##############X hat gewonnen##############")
        win = True
    elif b5.get() == "X" and b2.get() == "X" and b8.get() == "X":
        answer = messagebox.showinfo("Glückwunsch!", "##############X hat gewonnen##############")
        win = True
        disable()
    elif b5.get() == "X" and b3.get() == "X" and b7.get() == "X":
        answer = messagebox.showinfo("Glückwunsch!", "##############X hat gewonnen##############")
        win = True
        disable()

    if b1.get() == "O" and b2.get() == "O" and b3.get() == "O":
       answer =  messagebox.showinfo("Glückwunsch!", "##############O hat gewonnen##############")
       win = True
       disable()
    elif b1.get() == "O" and b4.get() == "O" and b7.get() == "O":
        answer = messagebox.showinfo("Glückwunsch!", "##############O hat gewonnen##############")
        win = True
        disable()
    elif b1.get() == "O" and b5.get() == "O" and b9.get() == "O":
        answer = messagebox.showinfo("Glückwunsch!", "##############O hat gewonnen##############")
        win = True
        disable()
    elif b9.get() == "O" and b6.get() == "O" and b3.get() == "O":
        answer = messagebox.showinfo("Glückwunsch!", "##############O hat gewonnen##############")
        win = True
        disable()
    elif b9.get() == "O" and b8.get() == "O" and b7.get() == "O":
        answer = messagebox.showinfo("Glückwunsch!", "##############O hat gewonnen##############")
        win = True
        disable()
    elif b5.get() == "O" and b4.get() == "O" and b6.get() == "O":
        answer = messagebox.showinfo("Glückwunsch!", "##############O hat gewonnen##############")
        win = True
        disable()
    elif b5.get() == "O" and b2.get() == "O" and b8.get() == "O":
        answer = messagebox.showinfo("Glückwunsch!", "##############O hat gewonnen##############")
        win = True
        disable()
    elif b5.get() == "O" and b3.get() == "O" and b7.get() == "O":
        answer = messagebox.showinfo("Glückwunsch!", "##############O hat gewonnen##############")
        win = True
        disable()

# draw
def draw():
    global count
    global win


    if count == 9 and win != True:
        messagebox.showinfo("","##############Unentschieden##############")


# restart program
def disable():
    btn1 = Button(top_frame, state = DISABLED, textvariable = b1 ,command = lambda: change(b1), width = 17, height = 8).grid(ipady = 2, ipadx = 2, row = 0)
    btn2 = Button(top_frame, state = DISABLED, textvariable=b2, command=lambda: change(b2), width=17, height=8).grid(ipady=2, ipadx=2,row=0, column=1)
    btn3 = Button(top_frame, state = DISABLED, textvariable=b3, command=lambda: change(b3), width=17, height=8).grid(ipady=2, ipadx=2,row=0, column=2)

    btn4 = Button(top_frame, state = DISABLED, textvariable=b4, command=lambda: change(b4), width=17, height=8).grid(ipady=2, ipadx=2,row=1)
    btn5 = Button(top_frame, state = DISABLED, textvariable=b5, command=lambda: change(b5), width=17, height=8).grid(ipady=2, ipadx=2, row=1, column=1)
    btn6 = Button(top_frame, state = DISABLED, textvariable=b6, command=lambda: change(b6), width=17, height=8).grid(ipady=2, ipadx=2, row=1, column=2)

    btn7 = Button(top_frame ,state = DISABLED, textvariable=b7, command=lambda: change(b7), width=17, height=8).grid(ipady=2, ipadx=2, row=2)
    btn8 = Button(top_frame, state = DISABLED, textvariable=b8, command=lambda: change(b8), width=17, height=8).grid(ipady=2, ipadx=2, row=2, column=1)
    btn9 = Button(top_frame, state = DISABLED, textvariable=b9, command=lambda: change(b9), width=17, height=8).grid(ipady=2, ipadx=2, row=2, column=2)

# restart button
def reset():
    global count
    count = 0

    b1.set("")
    btn1 = Button(top_frame, state=ACTIVE, textvariable=b1, command=lambda: change(b1), width=17, height=8).grid(ipady=2, ipadx=2, row=0)
    b2.set("")
    btn2 = Button(top_frame, state = ACTIVE, textvariable=b2, command=lambda: change(b2), width=17, height=8).grid(ipady=2, ipadx=2,row=0, column=1)
    b3.set("")
    btn3 = Button(top_frame, state = ACTIVE, textvariable=b3, command=lambda: change(b3), width=17, height=8).grid(ipady=2, ipadx=2,row=0, column=2)
    b4.set("")
    btn4 = Button(top_frame, state = ACTIVE, textvariable=b4, command=lambda: change(b4), width=17, height=8).grid(ipady=2, ipadx=2,row=1)
    b5.set("")
    btn5 = Button(top_frame, state=ACTIVE, textvariable=b5, command=lambda: change(b5), width=17, height=8).grid(ipady=2, ipadx=2, row=1, column=1)
    b6.set("")
    btn6 = Button(top_frame, state=ACTIVE, textvariable=b6, command=lambda: change(b6), width=17, height=8).grid(ipady=2, ipadx=2, row=1, column=2)
    b7.set("")
    btn7 = Button(top_frame ,state = ACTIVE, textvariable=b7, command=lambda: change(b7), width=17, height=8).grid(ipady=2, ipadx=2, row=2)
    b8.set("")
    btn8 = Button(top_frame, state = ACTIVE, textvariable=b8, command=lambda: change(b8), width=17, height=8).grid(ipady=2, ipadx=2, row=2, column=1)
    b9.set("")
    btn9 = Button(top_frame, state = ACTIVE, textvariable=b9, command=lambda: change(b9), width=17, height=8).grid(ipady=2, ipadx=2, row=2, column=2)







my_menu = Menu(window)
window.config(menu = my_menu)

options = Menu(my_menu, tearoff = False )
my_menu.add_cascade(label = "Optionen", menu = options)
options.add_command(label = "Neustart", command = reset)



# when click then change text and Xor0
def change(b):
    global Xor0
    global count
    global answer
    global win

    if Xor0 == True and b.get() == "":
        b.set("X")
        count += 1
        Xor0 = False
        winlol()
        draw()
        change_play()
    elif Xor0 == False and b.get() == "":
        b.set("O")
        count += 1
        Xor0 = True
        winlol()
        draw()
        change_play()
    else:
        messagebox.showinfo("Stop!", "Feld bereits besetzt, wähle ein anderes")


# current player
text = StringVar()
def change_play():
    global Xor0
    if Xor0 == True:
        text.set("X")
    elif Xor0 == False:
        text.set("O")







player = Label(bottom_frame)
player.grid(row = 0)

player.config(text= "Wer ist dran:")

xo = Label(bottom_frame)
xo.config(textvariable = text, command = change_play())
xo.grid(row = 0,column = 1)











b1 = StringVar()
b2 = StringVar()
b3 = StringVar()
b4 = StringVar()
b5 = StringVar()
b6 = StringVar()
b7 = StringVar()
b8 = StringVar()
b9 = StringVar()


# 9x9 game grid in top_frame
btn1 = Button(top_frame, textvariable = b1 ,command = lambda: change(b1), width = 17, height = 8).grid(ipady = 2, ipadx = 2, row = 0)
btn2 = Button(top_frame, textvariable = b2, command = lambda: change(b2), width = 17, height = 8).grid(ipady = 2, ipadx = 2, row = 0, column = 1)
btn3 = Button(top_frame, textvariable = b3, command = lambda: change(b3), width = 17, height = 8).grid(ipady = 2, ipadx = 2, row = 0, column = 2)

btn4 = Button(top_frame, textvariable = b4, command = lambda: change(b4), width = 17, height = 8).grid(ipady = 2, ipadx = 2, row = 1)
btn5 = Button(top_frame, textvariable = b5, command = lambda: change(b5), width = 17, height = 8).grid(ipady = 2, ipadx = 2, row = 1, column = 1)
btn6 = Button(top_frame, textvariable = b6, command = lambda: change(b6), width = 17, height = 8).grid(ipady = 2, ipadx = 2, row = 1, column = 2)

btn7 = Button(top_frame, textvariable = b7, command = lambda: change(b7), width = 17, height = 8).grid(ipady = 2, ipadx = 2, row = 2)
btn8 = Button(top_frame, textvariable = b8, command = lambda: change(b8), width = 17, height = 8).grid(ipady = 2, ipadx = 2, row = 2, column = 1)
btn9 = Button(top_frame, textvariable = b9, command = lambda: change(b9), width = 17, height = 8).grid(ipady = 2, ipadx = 2, row = 2, column = 2)





window.mainloop()