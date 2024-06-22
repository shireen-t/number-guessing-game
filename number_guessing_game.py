from tkinter import *
from PIL import Image, ImageTk # type: ignore
import random
import tkinter.messagebox as tmsg

# Global variables
app = None
comp = None
count = 0
userv = None
sc = None

def generate():
    global comp
    comp = random.randint(1, 100)

def basic():
    global app, sc
    app = Tk()
    app.title("Number Guessing Game")
    app.geometry("500x400")
    app.minsize(500, 400)
    app.maxsize(500, 400)
    app.configure(bg="#303030")  # Dark background for a sleek look

    try:
        icon_image = Image.open('guess.png')
        icon_photo = ImageTk.PhotoImage(icon_image)
        app.iconphoto(False, icon_photo)
    except FileNotFoundError:
        print("Icon file 'guess.png' not found.")

    Label(app, text='Number Guessing Game', font='Helvetica 24 bold', bg='#303030', fg='white').pack(pady=(20, 10))

    # Previous score display
    with open('score.txt', 'r') as f:
        hg = f.read()
    sc = Label(app, text=f'Previous Score: {hg}', font='Helvetica 12 bold', bg='#303030', fg='white')
    sc.pack(anchor=E, padx=20)

    # Footer
    Label(app, text='Developed by Shireen', font="Helvetica 10 bold", bg='#303030', fg='white').pack(side=BOTTOM, pady=10)

    # Menu
    mymenu = Menu(app)
    filee = Menu(mymenu, tearoff=0)
    mymenu.add_cascade(label='Game', menu=filee)
    filee.add_command(label='Restart', command=restart)
    filee.add_command(label='About', command=call1)
    filee.add_command(label='Quit', command=app.quit)
    app.config(menu=mymenu)

    generate()

def result():
    global count, comp
    number = userv.get()
    if number == '':
        tmsg.showerror('Error', 'Please enter a number.')
    else:
        try:
            n = int(number)
            count += 1
            if count == 10:
                tmsg.showinfo('Game Over :(', 'You have exhausted your attempts.')
            elif comp == n:
                score = 11 - count
                tmsg.showinfo('Congratulations!', f'You guessed the number in {count} attempts.\nYour Score: {score}.\nTo Restart the game, Click on the game button on the top-left corner and press "Restart"')
                show.config(text=f'Congratulations! You guessed the number in {count} attempts.', fg='#00cc00')  # Green text for success
                with open('score.txt', 'w') as f:
                    f.write(str(score))
                generate()
            elif comp > n:
                show.config(text='Select a greater number', fg='red')
                userv.set('')  # Clear the entry box
            else:
                show.config(text='Select a smaller number', fg='red')
                userv.set('')  # Clear the entry box
        except ValueError:
            tmsg.showerror('Error', 'Enter a valid integer number.')

def restart():
    global count, sc
    count = 0
    generate()
    show.config(text='')

    with open('score.txt', 'r') as f:
        hg = f.read()
    sc.config(text=f'Previous Score: {hg}')

    with open('score.txt', 'w') as f:
        f.write('0')

def call1():
    about_text = "Number Guessing Game\n\nDeveloped by Shireen\nCopyright@2024"
    tmsg.showinfo('About', about_text)

if __name__ == "__main__":
    basic()
    userv = StringVar()

    # User input
    user = Entry(app, textvariable=userv, justify=CENTER, relief=FLAT, borderwidth=2, font='Helvetica 18 bold')
    user.pack(pady=10)

    # Function to call result when Enter key is pressed
    def on_enter(event):
        result()

    # Submit button
    try:
        i = Image.open('button.jpg')
        resized_image = i.resize((150, 50))
        new_image = ImageTk.PhotoImage(resized_image)
        submit = Button(app, image=new_image, command=result, relief=FLAT)
        submit.pack(pady=10)
    except FileNotFoundError:
        submit = Button(app, text='Submit', command=result, font='Helvetica 14 bold', relief=FLAT)
        submit.pack(pady=10)
        print("Button image 'button.jpg' not found.")

    # Bind Enter key to submit button
    app.bind('<Return>', on_enter)

    # Game message
    show = Label(app, text='', font='Helvetica 12 bold', bg='#303030', fg='white')
    show.pack(pady=10)

    app.mainloop()
