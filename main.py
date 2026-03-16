from tkinter import *
from tkinter import ttk

#colors
black = "#1f1f1f"
gray = "#828282"
white = "#ffffff"
orange = "#FF8300"
cool_gray = "#CBCBCB"
dark_gray = "#5C5C5C"

#Screen Config
window = Tk()
window.title("Calculadora")
window.geometry("360x600")
window.config(bg=black)


#frames
frame_display = Frame(window, width=360, height=150, bg=black)
frame_display.grid(row=0, column=0)

frame_screen = Frame(window, width=360, height=470, bg=black)
frame_screen.grid(row=1, column=0)

#functions
all_values = ''
text_value = StringVar()

def input_data(e):
    global all_values
    all_values += e
    text_value.set(all_values)

def calc():
    global all_values
    result = eval(all_values)
    text_value.set(result)

def clear():
    global all_values
    all_values=""
    text_value.set("")

#label
app_label = Label(frame_display, textvariable = text_value, width=18, height=4, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 23 bold"), bg=black, fg=white)
app_label.place(x=0,y=0)


#buttons
#C
bC = Button(frame_screen, command = clear, text="C", width=17, height=4,relief=RAISED, bg=gray, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
bC.place(x=0, y=0)

#%
bMod = Button(frame_screen, command = lambda: input_data('%') , text="%", width=8, height=4, relief=RAISED, bg=gray, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
bMod.place(x=180, y=0)

#/
bDiv = Button(frame_screen, command = lambda: input_data('/') , text="/", width=8, height=4, relief=RAISED, bg=orange, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
bDiv.place(x=270, y=0)
#---------------------------------------------------------------line 1---------------------------------------------------------------------------------------------------------------------------------------

#7
b7 = Button(frame_screen, command = lambda: input_data('7') , text="7", width=8, height=4, relief=RAISED, bg=dark_gray, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
b7.place(x=0, y=90)

#8
b8 = Button(frame_screen, command = lambda: input_data('8') , text="8", width=8, height=4, relief=RAISED, bg=dark_gray, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
b8.place(x=90, y=90)

#9
b9 = Button(frame_screen, command = lambda: input_data('9') , text="9", width=8, height=4, relief=RAISED, bg=dark_gray, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
b9.place(x=180, y=90)

#*
bMult = Button(frame_screen, command = lambda: input_data('*') , text="*", width=8, height=4, relief=RAISED, bg=orange, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
bMult.place(x=270, y=90)
#------------------------------------------------------------------line 2--------------------------------------------------------------------------------------------------------------------------------------

#4
b4 = Button(frame_screen, command = lambda: input_data('4') , text="4", width=8, height=4, relief=RAISED, bg=dark_gray, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
b4.place(x=0, y=180)

#5
b5 = Button(frame_screen, command = lambda: input_data('5') , text="5", width=8, height=4, relief=RAISED, bg=dark_gray, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
b5.place(x=90, y=180)

#6
b6 = Button(frame_screen, command = lambda: input_data('6') , text="6", width=8, height=4, relief=RAISED, bg=dark_gray, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
b6.place(x=180, y=180)

#-
bSub = Button(frame_screen, command = lambda: input_data('-') , text="-", width=8, height=4, relief=RAISED, bg=orange, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
bSub.place(x=270, y=180)
#-------------------------------------------------------------------line 3----------------------------------------------------------------------------------------------------------------------------------------

#1
b1 = Button(frame_screen, command = lambda: input_data('1') , text="1", width=8, height=4, relief=RAISED, bg=dark_gray, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
b1.place(x=0, y=270)

#2
b2 = Button(frame_screen, command = lambda: input_data('2') , text="2", width=8, height=4, relief=RAISED, bg=dark_gray, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
b2.place(x=90, y=270)

#3
b3 = Button(frame_screen, command = lambda: input_data('3') , text="3", width=8, height=4, relief=RAISED, bg=dark_gray, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
b3.place(x=180, y=270)

#1
bAdd = Button(frame_screen, command = lambda: input_data('+') , text="+", width=8, height=4, relief=RAISED, bg=orange, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
bAdd.place(x=270, y=270)
#--------------------------------------------------------------------line 4----------------------------------------------------------------------------------------------------------------------------------------

#0
b0 = Button(frame_screen, command = lambda: input_data('0') , text="0", width=17, height=4,relief=RAISED, bg=dark_gray, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
b0.place(x=0, y=360)

#.
bDot = Button(frame_screen, command = lambda: input_data('.') , text=".", width=8, height=4, relief=RAISED, bg=dark_gray, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
bDot.place(x=180, y=360)

#=
bEqual = Button(frame_screen, command = calc , text="=", width=8, height=4, relief=RAISED, bg=orange, fg=white, font=("Arial", 12, "bold"), activebackground=cool_gray, overrelief=RIDGE)
bEqual.place(x=270, y=360)

window.mainloop()
