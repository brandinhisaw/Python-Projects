#
# Python:   3.9
#
# Author:   Brandin Hiaw
#
# Purpose:  Python Course for the Tech Academy bootcamp.
#           Demonstrating how to pass variables between functions and
#           creating a functional game.
#
from playsound import playsound

def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)



def describe_game(name):
    """
        check if this is a new game.
        if it is, get the user's name.
        if it isn't, thank the player for
        playing again and continue with the game.
    """
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name =="":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name



def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score() function



def show_score(nice,mean,name):
    print("\n{}, your current total: \n ({}, Nice) and ({}, Mean)".format(name,nice,mean))



def score(nice,mean,name):
    # score function is being passed the values stored with the 3 main variables
    if nice > 2: # if condition is met, call win function
        win(nice,mean,name)
    if mean > 2: # if condition is met, call lose function
        lose(nice,mean,name)
    else:        # else, call nice_mean function again
        nice_mean(nice,mean,name)



def win(nice,mean,name):
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade a lot of friends along the way!".format(name))
    playsound("win.mp3") # sound from Zapsplat.com
    # call again function to see if player wants to reset the game
    again(nice,mean,name)



def lose(nice,mean,name):
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    playsound("lose.mp3") # sound from Zapsplat.com
    # call again function to see if the player wants to reset the game
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while(stop):
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")



def reset(nice,mean,name):
    nice = 0
    mean = 0
    # name will remain the same since the same user is choosing to play again
    start(nice,mean,name)


                

if __name__ == "__main__":
    start()
