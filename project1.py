from tkinter import messagebox, simpledialog, Tk

def get_task():
    task = simpledialog.askstring('task','Do you want to encrypt or decrypt?')
    return task

def get_message():
    message = simpledialog.askstring('message','Enter the secret message.')
    return message

root = Tk()
while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        messagebox.showinfo('The message to encrypt is:',message)
    elif task == 'decrypt':
        message = get_message()
        messagebox.showinfo('The message to decrypt is:',message)
    else:
        break

root.mainloop()

