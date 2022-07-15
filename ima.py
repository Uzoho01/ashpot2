from tkinter import *

#to import pillow
#we install with using pip install

from PIL import ImageTk,Image

#created my window
master = Tk()

#created my title
master.title("learn to create icons")
#location of the
mage = PhotoImage(file = "python_tutorial/ring.png")

master.iconphoto(False,mage)

#using images
#piilow is used to importing image libaries




#creating an exist  button
button_exist = Button(master,text= "Exit program",command=master.quit)
button_exist.pack()


master.mainloop()