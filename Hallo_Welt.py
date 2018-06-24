# -*- coding: utf-8 -*-
#Example (Hallo Welt):
import Tkinter

tk = Tkinter.Tk()
frame = Tkinter.Frame(tk, relief="ridge", borderwidth=2)
tk.title("Mein Fenster")

#Fullscrenmodus
tk.attributes('-fullscreen',True)
tk.attributes('-topmost',True)
tk.overrideredirect(True)

#Fenstergroeße (X)x(y)

#tk.geometry('640x480') 
frame.pack(fill="both",expand=1)
label = Tkinter.Label(frame, text="Hallo Welt!")
label.pack(expand=1)
button = Tkinter.Button(frame,text="Beenden", command=tk.destroy)
button.pack(side="bottom")

tk.mainloop()
