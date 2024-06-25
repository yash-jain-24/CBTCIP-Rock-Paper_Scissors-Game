from tkinter import *
from PIL import Image, ImageTk
from random import randint
from playsound import playsound
from pygame import mixer


#for playing background music
mixer.init()
mixer.music.load('bg.mp3')
mixer.music.play()


# Main window
root = Tk()
root.title("ROCK PAPER SCISSOR")
root.configure(background="#5af287")
#playsound("bg.mp3")


# Picture
rock_img = ImageTk.PhotoImage(Image.open("rock-comp.png").resize((350, 350)))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png").resize((350, 350)))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png").resize((350, 350)))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock-user.png").resize((350, 350)))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper-comp.png").resize((350, 350)))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors_comp.png").resize((350, 350)))

# Insert picture
user_label = Label(root, image=scissor_img, bg="#5af287")
comp_label = Label(root, image=scissor_img_comp, bg="#5af287")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# Scores
playerscore = Label(root, text=0, font=100, bg="#5af287", fg="#0c0d0c")
computerscore = Label(root, text=0, font=100, bg="#5af287", fg="#0c0d0c")
computerscore.grid(row=1, column=1)
playerscore.grid(row=1, column=3)

# Indicators
user_indicator = Label(root, font=50, text="USER", bg="#5af287", fg="#0c0d0c")
comp_indicator = Label(root, font=50, text="COMPUTER", bg="#5af287", fg="#0c0d0c")
user_indicator.grid(row=0, column=4)
comp_indicator.grid(row=0, column=0)

# Messages
msg = Label(root, font=50, bg="#5af287", fg="#0c0d0c")
msg.grid(row=3, column=2)


# Update message
def updateMessage(x):
    msg['text'] = x


# Update user score
def updateUserScore():
    score = int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)


# Update computer score
def updatecompScore():
    score = int(computerscore["text"])
    score += 1
    computerscore["text"] = str(score)


# Check winner
def checkwin(player, computer):
    if player == computer:
        updateMessage("OH! IT'S A TIE")
        playsound("it's_a_tie.mp3")
    elif player == "rock":
        if computer == "paper":
            updateMessage("YOU LOSE!!")
            playsound("you_loss.mp3")
            updatecompScore()
        else:
            updateMessage("YOU WIN")
            playsound("you_win.mp3")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("YOU LOSE!!")
            playsound("you_loss.mp3")
            updatecompScore()
        else:
            updateMessage("YOU WIN!!")
            playsound("you_win.mp3")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("YOU LOSE!!")
            playsound("you_loss.mp3")
            updatecompScore()
        else:
            updateMessage("YOU WIN!!")
            playsound("you_win.mp3")
            updateUserScore()
    else:
        pass


# Update choices
choices = ["rock", "paper", "scissor"]


def updatechoice(x):
    # For computer
    compchoice = choices[randint(0, 2)]
    if compchoice == "rock":
        comp_label.configure(image=rock_img)
    elif compchoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    # For user
    if x == "rock":
        user_label.configure(image=rock_img_comp)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkwin(x, compchoice)


# Buttons
rock = Button(root, width=20, height=2, text="Rock", bg="#FF3E4D", fg="#0c0d0c",
              command=lambda: updatechoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="Paper", bg="#FAD02E", fg="#0c0d0c",
               command=lambda: updatechoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="Scissor", bg="#0ABDE3", fg="#0c0d0c",
                 command=lambda: updatechoice("scissor")).grid(row=2, column=3)

root.mainloop()