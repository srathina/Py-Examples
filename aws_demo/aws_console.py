import tkinter
import aws_ec2_demo as ec2
import datetime

window = tkinter.Tk()
window.geometry("600x600")
window.title("AWS Mini Console")

toggle = False

#EC2
def ec2_start_stop():
    global toggle
    if toggle == False:
        resp = ec2.start_instance()
        start_text = f'{datetime.datetime.now()}: EC2 Instance Started'
        tkinter.Label(text = start_text , fg = "green", font = 'Tahoma').pack()
        toggle = True
    else:
        resp = ec2.stop_instance()
        stop_text = f'{datetime.datetime.now()}: EC2 Instance Stopped'
        tkinter.Label(text = stop_text , fg = "red", font = 'Tahoma').pack()
        toggle = False


tkinter.Label(text = "Welcome to mini AWS Console" , fg = "purple", font = 'Tahoma').pack()
frame = tkinter.Frame(window, height="200", width="200", borderwidth = 10, relief = "groove")
frame.pack()
tkinter.Label(frame,text = "EC2" , fg = "Blue", bg = "black", font = 'Tahoma', height="3", width="30", relief = "sunken",borderwidth = 8).pack()
tkinter.Button(frame,text = "Start", fg = "green", font = 'Tahoma', height="3", width="30", highlightcolor ="yellow",command = ec2_start_stop).pack()
tkinter.Button(frame,text = "Stop", fg = "red", font = 'Tahoma', height="3", width="30",highlightcolor ="yellow",command = ec2_start_stop).pack()

window.mainloop()

