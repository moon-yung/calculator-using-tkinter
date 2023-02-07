from tkinter import *
import tkinter.font as font
from tkinter import ttk

# Create function everytime you press a num or operation


def button_press(num):
	global expression	

	expression = expression + str(num)

	equation.set(expression)



# Create equals function
def equals():
	global expression	

	try:
		total = str(eval(expression)) #equation_text

		equation.set(total) #equation_label

		expression = total
		
	except SyntaxError:
		equation.set("Syntax Error")

		expression = ""

	except ZeroDivisionError:
		equation.set("error")

		expression = ""

def clear():
	global expression

	expression = ""
	equation.set("")
	

# Initialize the main window
root = Tk()
root.title("Calculator")
root.config(bg='#fca335', borderwidth=4)
root.resizable(False,False)
root.geometry("300x352") 


def_padx = 0
def_pady = 0
num_padx = 22

# Set font
f = font.Font(family='Arial', size=14)
numfont = font.Font(family='Arial bold', size=8)

expression = ""
equation = StringVar()

# Create label for display
label = Label(root, width=8, height=2, textvariable=equation, font=f, bg ='#474747', fg='#ffffff', relief=RIDGE, bd=10, anchor='w')
label.pack()

# Setting Buttons
div = Button   (root, text="÷", padx=num_padx, pady=def_pady,	 bg='#b4b4b4',	height=3,	width=3,  command=lambda: button_press('/'))
mul = Button   (root, text="×", padx=num_padx, pady=def_pady,	 bg='#b4b4b4',	height=3,	width=3,  command=lambda: button_press('*'))
minus = Button (root, text="-", padx=num_padx, pady=def_pady,	 bg='#b4b4b4',	height=3,	width=3,  command=lambda: button_press('-'))
plus = Button  (root, text="+", padx=num_padx, pady=def_pady,	 bg='#b4b4b4',	height=3,	width=3,  command=lambda: button_press('+'))
equals = Button(root, text="=", padx=num_padx, pady=def_pady,	 bg='#d6d6cf',	height=3,	width=3,  command=equals)
pt = Button    (root, text="•", padx=num_padx, pady=def_pady,				   	height=3,	width=3,  command=lambda: button_press('.'))

nine = Button  (root, text="9", padx=num_padx, pady=def_pady,	height=3,	width=3,	command=lambda: button_press(9))
eight = Button (root, text="8", padx=num_padx, pady=def_pady,	height=3,	width=3,	command=lambda: button_press(8))
seven = Button (root, text="7", padx=num_padx, pady=def_pady,	height=3,	width=3,	command=lambda: button_press(7))
six = Button   (root, text="6", padx=num_padx, pady=def_pady,	height=3,	width=3,	command=lambda: button_press(6))
five = Button  (root, text="5", padx=num_padx, pady=def_pady,	height=3,	width=3,	command=lambda: button_press(5))
four = Button  (root, text="4", padx=num_padx, pady=def_pady,	height=3,	width=3,	command=lambda: button_press(4))
three = Button (root, text="3", padx=num_padx, pady=def_pady,	height=3,	width=3,	command=lambda: button_press(3))
two = Button   (root, text="2", padx=num_padx, pady=def_pady,	height=3,	width=3,	command=lambda: button_press(2))
one = Button   (root, text="1", padx=num_padx, pady=def_pady,	height=3,	width=3,	command=lambda: button_press(1))
zero = Button  (root, text="0", padx=58, 	   pady=def_pady,	height=3,	width=3,	command=lambda: button_press(0))
clear = Button (root, text="C L E A R", 	   padx=36, 	  	pady=def_pady,  		bg='#d6d6cf',	height=3,	width=20, command=clear)


# Setting Grid
label.grid (row=0, column=0, columnspan=4, padx=def_padx,pady=def_pady, sticky='ew')
clear.grid  (row=1, column=0, padx=0, pady=1, columnspan = 3)
div.grid	(row=1, column=3, padx=0, pady=1)
mul.grid	(row=2, column=3, padx=0, pady=1)
minus.grid	(row=3, column=3, padx=0, pady=1)
plus.grid	(row=4, column=3, padx=0, pady=1)
equals.grid (row=5, column=3, padx=0, pady=1, columnspan = 2)
pt.grid		(row=5, column=2, padx=0, pady=1)

seven.grid	(row=2, column=0, padx=0, pady=1)
eight.grid	(row=2, column=1, padx=0, pady=1)
nine.grid	(row=2, column=2, padx=0, pady=1)
four.grid	(row=3, column=0, padx=0, pady=1)
six.grid	(row=3, column=2, padx=0, pady=1)
five.grid	(row=3, column=1, padx=0, pady=1)
four.grid	(row=3, column=0, padx=0, pady=1)
three.grid	(row=4, column=2, padx=0, pady=1)
two.grid	(row=4, column=1, padx=0, pady=1)
one.grid	(row=4, column=0, padx=0, pady=1)
zero.grid	(row=5, column=0, padx=0, pady=1, columnspan = 2)





root.mainloop()

