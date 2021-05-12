from tkinter import Tk, Button, Label, DoubleVar, Entry, StringVar

window = Tk() #for the window variable Tk class has been imported to use GUIinterfaces like button,labe,entry etc
window.title("BMI Calculator")
window.configure(background="light blue")
window.geometry("320x320") #width and height
window.resizable(width=False,height=False) #width and height cannot be changed by user since its set to false

def Calculate():  #function call
    h_value = float(height_entry.get()) #using get we are getting the height/weight value as input
    w_value = float(weight_entry.get())
    bmi = w_value / (h_value*h_value)   #calculattion
    bmi_value.set("%.2f" %bmi)  #Using set we are setting the value and in 2decimal formats
    if bmi < 18.5:  #Based on condition healthrate_value is set...
        healthrate_value.set("Under Weight")
    elif bmi >= 18.5 and bmi <= 24.9:
        healthrate_value.set("Normal Weight")
    elif bmi >= 25 and bmi <= 29.9:
        healthrate_value.set("Over Weight")
    elif bmi > 30:
        healthrate_value.set("Obese")

def clear():
    height_value.set("")
    weight_value.set("")
    bmi_value.set("")
    healthrate_value.set("")

height_lbl = Label(window,text="Height (meter)",bg="pink",fg="black",width=14) #label widget - (window-where to place label, text of the label,bakground,foreground colors,width of the label)
height_lbl.grid(column=0,row=0,padx=15,pady=15) #To position a label inside container we used grid(Grid - It works like table to position rows and columns) and inside(where to position(column and row), padx- to leave space horizontally,pady-to leave space vertically
weight_lbl = Label(window,text="Weight (Kg)",bg="pink",fg="black",width=14)
weight_lbl.grid(column=0,row=1,padx=15,pady=15)

height_value = DoubleVar() #set the height value to double datatype
height_entry = Entry(window,textvariable=height_value,width=14) #entry widget(window,data to expect,width of widget)
height_entry.grid(column=1,row=0) #position of the widget
height_entry.delete(0,'end') #To clear any value in widget when application launches

weight_value = DoubleVar() #set the weight value to double datatype
weight_entry = Entry(window,textvariable=weight_value,width=14) #entry widget(window,data to expect,width of widget)
weight_entry.grid(column=1,row=1) #position of the widget
weight_entry.delete(0,'end') #To clear value in widget when application launches

bmi_lbl = Label(window,text="BMI",bg="pink",fg="black",width=14) #label widget - (window-where to place label, text of the label,bakground,foreground colors,width of the label)
bmi_lbl.grid(column=0,row=2) #To position a label inside container we used grid(Grid - It works like table to position rows and columns) and inside(where to position(column and row), padx- to leave space horizontally,pady-to leave space vertically
bmi_value = DoubleVar() #set the value to double datatype
bmi_entry = Entry(window,textvariable=bmi_value,width=14) #entry widget(window,data to expect,width of width)
bmi_entry.grid(column=1,row=2,pady=15) #position of the widget
bmi_entry.delete(0,'end') #To clear value in widget when application launches

healthrate_lbl = Label(window,text="Health Rate",bg="pink",fg="black",width=14)
healthrate_lbl.grid(column=0,row=3)
healthrate_value = StringVar()  #set the value to string
healthrate_entry = Entry(window,textvariable=healthrate_value,width=14)
healthrate_entry.grid(column=1,row=3,pady=15)
healthrate_entry.delete(0,'end')

convert_btn = Button(window,text="Calculate",bg="light green",fg="black",width=14,command=Calculate)  #command acts like a placeholder where u enter the function name
convert_btn.grid(column=0,row=4,padx=15,pady=25)

clear_btn = Button(window,text="Clear",bg="light green",fg="black",width=14,command=clear)
clear_btn.grid(column=1,row=4,padx=15,pady=25)

window.mainloop() #it runs the application
#To remove console when running an application you can save the file .pyw and when you click on the file it runs without console
# To convert a python code to an standalone executable file (i.e to run the application on any computer ) - Py installer - Builds and packages code and component as a single file
#command to convert the file is pyinstaller --onefile filename.pyw
