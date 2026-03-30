import tkinter as tk
root = tk.Tk()
#root.mainloop()#to open a window (white small window)
root.title('My first tkinter window')
root.geometry('400x300')
root.resizable(False,False)
label=tk.Label(root,text='welsome to Tkinter GUI',font=('Arial',14))
label.pack(pady=100)
root.mainloop()