import tkinter


#pack examples
window = tkinter.Tk()
window.title("Pack")
window.geometry("480x242")

tkinter.Label(window,text = "Hello world").pack()

top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side ="bottom")

def say_hi():
	tkinter.Label(window, text = "Hi RSK", fg= "green").pack()

tkinter.Button(top_frame, text ="Button 1", fg = "red", command = say_hi).pack()
tkinter.Button(top_frame, text = "Button 2", fg = "blue").pack()
tkinter.Button(bottom_frame, text = "Button 3", fg = "green").pack(side ="left")
tkinter.Button(bottom_frame, text = "Button 4", fg = "violet").pack(side ="right")

tkinter.Label(window, text = "Label", fg = "green", bg ="Black").pack(fill = "x")

tkinter.Radiobutton(window, text = "Radio button", fg = 'blue').pack()

tkinter.Checkbutton(window, text ='check box').pack()

icon = tkinter.PhotoImage(file = "C:/Users/srathina/Downloads/image.png") #this doesn't have pack method. so we need to use the label widget to pack it.
tkinter.Label(window, image = icon).pack()


#grid example
window1 = tkinter.Tk()
window1.title("Grid")

tkinter.Label(window1, text = 'Username' , fg = 'indigo').grid(row = 0, column = 0)
tkinter.Label(window1, text = 'Password', fg = 'black').grid(row = 1, column = 0)
tkinter.Entry(window1, text = 'Type Username' , fg = 'indigo').grid(row = 0, column = 1)
tkinter.Entry(window1, text = 'Type Password', fg = 'black').grid(row = 1, column = 1)

window.mainloop()
window1.mainloop()