

from tkinter import *


root = Tk()
root.title("Calculator Made By Pranto Paul")
root.geometry("431x530")
root.maxsize(431,530)
root.minsize(431,530)
font = ("Time" , 18 , "bold")



list = []
def valueIs(argu):
    list.append(argu)
    data = ""
    for i in list:
        data = data + str(i)
    screen.config(text = data)

def off_scrren():
    list.clear()
    screen.config(text="" , bg = 'black' , fg = 'white')
    

def clr_screen():
    try:
        list.pop()
        data = ""
        for i in list:
            data = data + str(i)
        screen.config(text = data , bg = 'black' , fg = 'white')
    except:
        pass

def calculate():
    data = ""
    for i in list:
        data = data + str(i)
    try:
        screen.config(text = eval(data))
    
    except ZeroDivisionError:
        screen.config(text = "Can not Divide something By Zero" , font = ('Time' , 15 , 'bold') , bg = "red" , fg = 'white')
    except SyntaxError:
        screen.config(text = "Please Input A Valid Syntax" , font = ('Time' , 15 , 'bold') , bg = "red" , fg = 'white')
    except:
        screen.config(text = "Something Went Wrong", bg = "red" , fg = 'white')


screen = Label(root , background="black" , fg=  "white"  , font = ("Time" , 26 , "bold" ) , text = "My First Projetc" , pady=20)
screen.pack(side = TOP , fill=X , expand=True , anchor="nw")

btns = Frame(root)
btns.pack(side = TOP , fill=X , expand=True , anchor="nw")

Button(btns , text = "C" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2, bg = "red" , activebackground="red" , command=clr_screen).grid(row = 1 ,column=0 , padx=5 , pady = 5)
Button(btns , text = "AC" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2, bg = "cyan" , activebackground="cyan", command=off_scrren).grid(row = 1 ,column=1 , padx=5 , pady = 5)
Button(btns , text = "/" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2 , bg = "#f5923e" , activebackground="#f5923e", command=lambda:valueIs('/')).grid(row = 1 ,column=2 , padx=5 , pady = 5)
Button(btns , text = "X" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2 , bg = "#f5923e" , activebackground="#f5923e", command=lambda:valueIs('*')).grid(row = 1 ,column=3 , padx=5 , pady = 5)

Button(btns , text = "7" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2, command=lambda:valueIs('7')).grid(row = 2 ,column=0 , padx=5 , pady = 5)
Button(btns , text = "8" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2, command=lambda:valueIs('8')).grid(row = 2 ,column=1 , padx=5 , pady = 5)
Button(btns , text = "9" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2, command=lambda:valueIs('9')).grid(row = 2 ,column=2 , padx=5 , pady = 5)
Button(btns , text = "-" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2 , bg = "#f5923e" , activebackground="#f5923e", command=lambda:valueIs('-')).grid(row = 2 ,column=3 , padx=5 , pady = 5)

Button(btns , text = "4" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2, command=lambda:valueIs('4')).grid(row = 3 ,column=0 , padx=5 , pady = 5)
Button(btns , text = "5" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2, command=lambda:valueIs('5')).grid(row = 3 ,column=1 , padx=5 , pady = 5)
Button(btns , text = "6" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2, command=lambda:valueIs('6')).grid(row = 3 ,column=2 , padx=5 , pady = 5)
Button(btns , text = "+" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=5 , bg = "#f5923e" , activebackground="#f5923e", command=lambda:valueIs('+')).grid(row = 3 ,column=3 , padx=5 , pady = 5 , rowspan=2)

Button(btns , text = "1" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2, command=lambda:valueIs('1')).grid(row = 4 ,column=0 , padx=5 , pady = 5)
Button(btns , text = "2" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2, command=lambda:valueIs('2')).grid(row = 4 ,column=1 , padx=5 , pady = 5)
Button(btns , text = "3" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2, command=lambda:valueIs('3')).grid(row = 4 ,column=2 , padx=5 , pady = 5)


Button(btns , text = "0" , font = font , cursor="hand2" , width = 12 , bd = 1 , height=2, command=lambda:valueIs('0')).grid(row = 5 ,column=0,columnspan=2 , padx=5 , pady = 5)
Button(btns , text = "." , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2, command=lambda:valueIs('.')).grid(row = 5 ,column=2 , padx=5 , pady = 5)
Button(btns , text = "=" , font = font , cursor="hand2" , width = 6 , bd = 1 , height=2 , bg = "green" , activebackground="green", command=calculate).grid(row = 5 ,column=3 , padx=5 , pady = 5)


root.mainloop()