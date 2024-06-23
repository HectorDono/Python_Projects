# Program to remove the duplicate file 

import hashlib
from os import path
import os
import shutil
from tkinter import *
from tkinter import messagebox,filedialog

root = Tk()
myfont = 'verdana'

# Giving root title
root.title('Duplicate Remover')

# giving size to main container
root.geometry(('700x700'))

# image library 
from PIL import ImageTk,Image

img = Image.open('m.png')

# resizing it 
img = img.resize((100,100))

# Opening image by converting into photo image
img=ImageTk.PhotoImage(img)

h1 = Label(root,image =img)

# pack this image on top and giving some padding
h1.pack(side=TOP,padx=10,pady=10)

# adding label for heading
head= Label(root,text='DUPLICATE FILE REMOVAL',font = (myfont,30))

# packing
# head.pack(fill=X)
# adding padding
head.pack(fill=X,padx=10,pady=10)

# adding select folder label and packing
head2=Label(root,text='Select Folder',font=(myfont,17))
head2.pack(fill=X,padx=10,pady=10)

folder = ''
# adding functionality to button adding file dialog box
def Folder():
    # it will open the window
    folder  = filedialog.askdirectory(parent=root,title="CHOOSE THE FOLDER...")
    # printing the path to terminal 
    # print(f)
    txt.config(text='DELETE DUPLICATE FILES OF \n: {}'.format(folder))

# adding button and adding function inside the button
browse = Button(root,text='Browse',font=(myfont,14),command=Folder)
browse.pack()


txt=Label(root,font=(myfont,17),justify=LEFT)
txt.pack(fill=X,padx=10,pady=10)

# 
top = Frame()

top.pack(side=TOP)

# function for below button

def CancelBtn():
    folder = ''
    txt.config(text=folder)

# button to cancel
c=Button(root,text='Cancel',font=(myfont,16),command=CancelBtn)

def hashFile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
# function to delete the duplicate files
def DeleteBtn():
    path=os.path.abspath(folder)
    data={}
    for F,SF,f in os.walk(path):
        for file in f:
            path = os.path.join(F,file)
            chk = hashFile(path)
            
            if chk in data:
                data[chk].append(path)
            else:
                data[chk]=[path]

    newdata = list(filter(lambda x:len(x)>1,data.values()))
    count = 0
    for outer in newdata:
        icnt=0
        for inner in outer:
            icnt = icnt +1
            if icnt>=2:
                count=count+1
                inner = os.path.abspath(inner)
                os.remove(inner)
    print(count)
    messagebox.showinfo("","Succesfully  done .. \nCopied {} text files...".format(count))
    messagebox


# creating a delete button
b =Button(root,text='Delete',font=(myfont,16),command=DeleteBtn)

# packing the delete and cancel button to top frame
c.pack(in_=top,side=LEFT,padx=20)
b.pack(in_=top,side=LEFT,padx=20)


# it will show windows
root.mainloop()