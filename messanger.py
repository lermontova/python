from Tkinter import *

def print_mes():
    print ent.get() +' '+ 'said: '+ text.get('0.0',END) 


root=Tk()
root.title('Messanger')
frame = Frame(root,width=500, height=300)
frame.grid()
lab = Label(frame,text='Name: ')
lab.grid(row=0,column=1)
ent= Entry(frame)
ent.grid(row=1, column=1)
lab2 = Label(frame,text='Message ')
lab2.grid(row=2,column=1)
text=Text(frame,width=50,height=10)
text.grid(columnspan=3)
but = Button(frame,text='Send',command=print_mes)
but.grid(row=4,column=1)
root.mainloop()
