from Tkinter import *

tk = Tk()
tk.title("delete words!")
tk.geometry('300x400')
def button_clicked():
    text1.delete('1.0',END)
    print 'tlala'

button = Button(tk, text="Other words", command=button_clicked)
button.pack(fill =BOTH)

text1=Text(height=7,width=7,font='Arial 14')
text1.pack()

tk.mainloop()
