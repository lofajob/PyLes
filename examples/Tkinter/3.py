# -*- coding: utf-8 -*-
import Tkinter
import FileDialog

root = Tkinter.Tk()
root.withdraw()
fdlg = FileDialog.LoadFileDialog(root, title="Выберите файл")
fname = fdlg.go() # необязательные аргументы: dir_or_file=os.curdir, pattern="*", default="", key=None)
if fname == None: 
	print ("No File")# отмена пользователем
root.mainloop()
