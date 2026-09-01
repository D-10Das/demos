import socket
from tkinter import *
#creates send funtion to send message to server
def send(listbox,entry):
    #get message from user
    message = entry.get()

    #show message on the listbox widget
    listbox.insert('end',message)

    #deletes the message
    entry.delete(0,END)

    #message sent to server converted to bytes using encoding method
    s.send(bytes(message,"utf-8"))


#creates receive function to receive messages from server
def receive(listbox):

    #receive messages from server
    message = s.recv(50)

    #decoded message displayed on the listbox that is sent by server
    listbox.insert('end',"server: "+ message.decode('utf-8'))


#tkinter object is created
root = Tk()

#creates a textbox object
entry = Entry()

#textbox is created at bottom
entry.pack(side=BOTTOM)

#listbox object is created
listbox = Listbox(root)

#listbox is displayed
listbox.pack()

#button object is created
button = Button(root,text= "send",command=lambda:send(listbox,entry))

# send button is created at bottom
button.pack(side=BOTTOM)

#button object for receive button is created
rbutton = Button(root,text="Receive",command= lambda:receive(listbox))

#receive button is displayed at bottom
rbutton.pack(side= BOTTOM)

#sets title bar text
root.title('client')

#socket object is created
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#gets the computer name
hostname = socket.gethostname()

#asigns port number
PORT = 5002

#requests a connection on server running on the given port
s.connect((hostname,PORT))

#tkinter event loop begins here and window appears here and stays open
root.mainloop()