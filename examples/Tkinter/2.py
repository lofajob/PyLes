from Tkinter import *

def report():
    print "A button has been pressed"

outer_frame = Frame(None)
outer_frame.pack()

first_line = Frame(outer_frame)
first_line.pack(side=TOP)
button1 = Button(first_line, text='Button 1', command=report)
button1.pack(side=LEFT)
button2 = Button(first_line, text='Button 2', command=report)
button2.pack(side=LEFT)

second_line = Frame(outer_frame)
second_line.pack(side=TOP)
button3 = Button(second_line, text='Button 3', command=report)
button3.pack(side=LEFT)
button4 = Button(second_line, text='Button 4', command=report)
button4.pack(side=LEFT)

outer_frame.mainloop()
