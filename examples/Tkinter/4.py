#!/usr/local/bin/Python
# -*- coding: utf-8 -*-
"""Отображает символ клавиши (keysym) для каждого события KeyPress (нажатия клавиатуры)."""
import Tkinter
	
root = Tkinter.Tk()
root.title("Регистратор символов клавиатуры")
	
def reportEvent(event):
        print 'keysym=%s, keysym_num=%s' % (event.keysym, event.keysym_num)
	
text  = Tkinter.Text(root, width=20, height=5, highlightthickness=2)
	
text.bind('<KeyPress>', reportEvent)
	
text.pack(expand=1, fill="both")
text.focus_set()
root.mainloop()
