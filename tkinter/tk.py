from tkinter import *
from PIL import Image, ImageTk
root = Tk()

# widthXhight
root.geometry("1444x934")

#WIdth,hight
#root.minsize(200,100)
#root.maxsize(1000,600)

#photo = PhotoImage(file="2.jpg")
#for jpg images


f1 =Frame(root,bg='red',borderwidth=20)
f1.pack(side=LEFT,fill='y')
f2= Frame(root,bg='grey',borderwidth=30)
f2.pack(side=TOP,fill='x')

images= Image.open("2.jpg")
images = images.resize((250, 250), Image.ANTIALIAS) ## The (250, 250) is (height, width)
photo =ImageTk.PhotoImage(images) 
image_label = Label(f1,image= photo)
image_label.pack(padx=3)

lab= Label(f2,text="This is my lable")
lab.pack()

root.mainloop()