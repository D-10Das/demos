import socket
from tkinter import *
# function for send messages
def send(listbox,entry):
 # to get messages from user
    message = entry.get()

 # to insert and show  message in the listbox widget
    listbox.insert('end',message)

 # clears the message when deleted by the user
    entry.delete(0,END)
 #send messages to client using encoding method that converts characters to bytes
    client.send(bytes(message ,"utf-8"))


# function to receive messages from client
def receive(listbox):

   #receive messages from client
    message_from_client = client.recv(50)

   #displays the decoded message on the listbox coming from the client side
    listbox.insert('end',"Client:"+ message_from_client.decode('utf-8'))

#creates the tkinter object and the main application window is created
root = Tk()

#creates a textbox
entry = Entry()

#places widget at bottom of the screen
entry.pack(side=BOTTOM)

#creates the Listbox object
listbox = Listbox(root)

#displays the listbox
listbox.pack()

#creates the button object where the button name is "send"
button = Button (root,text ="Send",command = lambda:send(listbox,entry))

#send button is displayed at bottom
button.pack(side= BOTTOM)


#button object for "receive" is created
rbutton = Button(root,text= "Receive",command = lambda:receive(listbox))

#receive button is displayed at bottom
rbutton.pack(side=BOTTOM)

#sets title bar text
root.title('server')

#a socket object is created
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#gets computer name
hostname = socket.gethostname()

#assigns the port number
PORT= 5002

#attaches socket to address
s.bind((hostname,PORT))

#socket object starts listening
s.listen(4)

#accepts client connection
client,address = s.accept()

#tkinter event loop begins here and window appears and stays open
root.mainloop()