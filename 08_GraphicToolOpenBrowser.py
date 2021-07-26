#graphic tool to open browser

import webbrowser
from tkinter import *

root = Tk( )

root.title('Open Browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Open Google', command=google).pack(pady=20)

root.mainloop()