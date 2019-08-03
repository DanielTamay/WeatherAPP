import tkinter
from tkinter.constants import*
root = tkinter.Tk()
canvas = tkinter.Canvas(root, height=500, width= 500)
canvas.pack()

file object = open('friendBridge.png' )
background_image = tkinter.PhotoImage('FriendBridge.png')
background_label = tkinter.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tkinter.Frame(root,bg="#80c1ff",bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75, relheight=0.1, anchor= 'n')


entry = tkinter.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tkinter.Button(frame,text='Close',font=40)
button.place(relx=0.7,relwidth=0.3, relheight=1)

lower_frame = tkinter.Frame(root,bg="#80c1ff",bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor ='n')

label = tkinter.Label(lower_frame)
label.place(relwidth=1, relheight=1)
root.mainloop()