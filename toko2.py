from tkinter import*
from tkinter import ttk

root = Tk()
root.title("Titleused419thtime")
root.geometry("1000x1000")


color_label = Label(root,text = "End y")
color_label.place(relx = 0.9,rely = 0.86,anchor = CENTER)

color_label2 = Label(root,text = "End x")
color_label2.place(relx = 0.8,rely = 0.86,anchor = CENTER)

color_label3 = Label(root,text = "Start y")
color_label3.place(relx = 0.7,rely = 0.86,anchor = CENTER)

color_label4 = Label(root,text = "Start x")
color_label4.place(relx = 0.6,rely = 0.86,anchor = CENTER)

color_label5 = Label(root,text = "Color")
color_label5.place(relx = 0.5,rely = 0.86,anchor = CENTER)

cl = ["red","blue"]
ey = ["10","20","30","40","50","100","200"]
sv = StringVar()

d1 = ttk.Combobox(root,values = ey,textvariable  = sv)
d1.place(relx = 0.9,rely = 0.88,anchor = CENTER)

d2 = ttk.Combobox(root,values = ey,textvariable  = sv)
d2.place(relx = 0.8,rely = 0.88,anchor = CENTER)

d3 = ttk.Combobox(root,values = ey,textvariable  = sv)
d3.place(relx = 0.7,rely = 0.88,anchor = CENTER)

d4 = ttk.Combobox(root,values = ey,textvariable  = sv)
d4.place(relx = 0.6,rely = 0.88,anchor = CENTER)

d5 = ttk.Combobox(root,values = cl,textvariable  = sv)
d5.place(relx = 0.5,rely = 0.88,anchor = CENTER)

canvas = Canvas(root,width = 590,height = 510,bg = "white",highlightbackground = "lightgray")
canvas.pack()






root.mainloop()