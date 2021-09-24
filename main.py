import tkinter as tk

BUTTON_FONT = ('Consolas', 15) 

GRID_SIZE =  5

window = tk.Tk()

window.rowconfigure(tuple(range(GRID_SIZE)), weight=1)
window.columnconfigure(tuple(range(GRID_SIZE)), weight=1)

window.geometry('350x500')

window.config(bg="white")

temp_number = ""

number1 = ''
number2 = ''

def retrieve_number():
    
    global temp_number
    global number1
    global number2
    global praxh

    if number1 == '':
        number1 = temp_number
        del temp_number
        temp_number = ''
    elif number1 != '' and number2 == '':
        number2 = temp_number
        del temp_number
        temp_number = ''
    else:
        print('This programm cant take over two numbers you can calculate them with equal button and then enter the next number :)')
        main_label.config(text=temp_number)

    main_label.config(text=temp_number)

    print(f"{number1=} {number2=}")

def create_button_function(btn_praxh):

    def btn_function():
        global praxh

        praxh = btn_praxh

        retrieve_number()

    return btn_function

def create_button_function_number(btn_number):
	
	def btn_function_numbers():
		global temp_number
		
		temp_number += btn_number 
		
		main_label.config(text=temp_number)
	return btn_function_numbers


def function_backspace():
	global temp_number
	temp_number=temp_number[:-1]
	main_label.config(text=temp_number)
def function_clear():
    global temp_number, number1, number2
    number1 = ''
    temp_number = ''
    number2 = ''
    main_label.config(text=temp_number)


def function_minus():
	praxh = '-'
	temp_number = 0
def function_diairesh():
	praxh = '/'
	temp_number = 0
def function_polaplasiasmos():
	praxh = '*'
	temp_number = 0
def function_dot():
	global temp_number
	main_label.config(text=temp_number)



def calculate():
    global temp_number
    global number1
    global number2
    global praxh
    retrieve_number()

    number1_float = float(number1)
    number2_float = float(number2)
    
    if praxh == '+':
            apotelesma = number1_float + number2_float
            main_label.config(text=apotelesma)
    
    elif praxh == '*':
            apotelesma = number1_float * number2_float
            main_label.config(text=apotelesma)

    elif praxh == '-':
            apotelesma = number1_float - number2_float
            main_label.config(text=apotelesma)

    elif praxh == '/':
            apotelesma = number1_float / number2_float
            main_label.config(text=apotelesma)
    







main_label = tk.Label(window, font=('Consolas', 20))
main_label.grid(column=0, row=0, columnspan=5, sticky='NSEW')

btn_1 = tk.Button(window, text='1', font=BUTTON_FONT,command=create_button_function_number('1'))
btn_1.grid(column=1, row=3, sticky='NSEW')

btn_2 = tk.Button(window, text='2', font=BUTTON_FONT, command=create_button_function_number('2'))
btn_2.grid(column=2, row=3, sticky='NSEW')

btn_3 = tk.Button(window, text='3', font=BUTTON_FONT, command=create_button_function_number('3'))
btn_3.grid(column=3, row=3, sticky='NSEW')

btn_4 = tk.Button(window, text='4', font=BUTTON_FONT, command=create_button_function_number('4'))
btn_4.grid(column=1, row=2, sticky='NSEW')

btn_5 = tk.Button(window, text='5', font=BUTTON_FONT, command=create_button_function_number('5'))
btn_5.grid(column=2, row=2, sticky='NSEW')

btn_6 = tk.Button(window, text='6', font=BUTTON_FONT, command=create_button_function_number('6'))
btn_6.grid(column=3, row=2, sticky='NSEW')

btn_7 = tk.Button(window, text='7', font=BUTTON_FONT, command=create_button_function_number('7'))
btn_7.grid(column=1, row=1, sticky='NSEW')

btn_8 = tk.Button(window, text='8', font=BUTTON_FONT, command=create_button_function_number('8'))
btn_8.grid(column=2, row=1, sticky='NSEW')

btn_9 = tk.Button(window, text='9', font=BUTTON_FONT, command=create_button_function_number('9'))
btn_9.grid(column=3, row=1, sticky='NSEW')

btn_backspace = tk.Button(window, text= ' <-- ', font=BUTTON_FONT, command=function_backspace)
btn_backspace.grid(column=0, row=1, rowspan=2, sticky='NSEW')

btn_clear = tk.Button(window, text='clear', font=BUTTON_FONT, command=function_clear)	
btn_clear.grid(column=0, row=3, sticky='NSEW')

btn_dot = tk.Button(window, text= '  .  ', font=BUTTON_FONT, command = create_button_function("."))
btn_dot.grid(column=0, row=4, sticky='NSEW')


btn_0 = tk.Button(window, text='0', font=BUTTON_FONT, command=create_button_function_number('0'))
btn_0.grid(column=1, row=4, sticky='NSEW')

btn_plus = tk.Button(window, text='+', font=BUTTON_FONT, command=create_button_function('+'))
btn_plus.grid(column=2, row=4, sticky='NSEW')

btn_minus = tk.Button(window, text='-', font=BUTTON_FONT, command=create_button_function('-'))
btn_minus.grid(column=3, row=4, sticky='NSEW')

btn_equal = tk.Button(window, text='\n=\n', font=BUTTON_FONT, command=calculate)
btn_equal.grid(column=4, row=3, rowspan=2, sticky='NSEW')

btn_diairesh = tk.Button(window, text='/', font=BUTTON_FONT, command=create_button_function('/'))
btn_diairesh.grid(column=4, row=1, sticky='NSEW')

btn_polaplasiasmos = tk.Button(window, text='*', font=BUTTON_FONT, command=create_button_function('*'))
btn_polaplasiasmos.grid(column=4, row=2, sticky='NSEW')


window.mainloop()
