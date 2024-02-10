import random as rnd

scandal = 0
obsession = 10
food = 10
playing = True

def main():
    intro()
    gameLoop()
    

def intro():
    print("Trapped in your House because of Hans Christian Andersen!")
    print("Hans Christian Andersen is on your lawn")
    print("He wont leave and you refuse to let him in")
    print("Surely he has to go home eventually?")
    print("Why does he have camping supplies with him?")

def gameLoop():
    while playing:
        print("scandal: " + str(scandal))
        print("obsession: " + str(obsession))
        print("food: " + str(food))
        
        if scandal == 10:
            print("The scandal has become too much to bear, you are forced to sell your house and run away. Hans moves in and squats there")
            playing = False
        if obsession == 0:
            print("Too much has been happening for Hans to focus on you, he wanders off following a new obsession")
            playing = False
        if food == 0:
            print("You run out of food and starve to death, your friends host a small but tasteful funeral, Hans sends a card but does not attend")
            playing == False
        
        input("press enter to roll")
        
        roll = rnd.randint(1,6)
        
        if roll == 1 or roll == 2:
            desperationRolls()
        if roll == 3 or roll == 4:
            curtainRolls()
        if roll == 5 or roll == 6:
            anticsRolls()

def desperationRolls(): #1/2
    print("Your desperation mounts")
    
    roll = rnd.randint(1,6)
    
    if roll == 1:
        print("You enter the basement to search for food, rats have eaten some")
        food -= 1
    if roll == 2:
        print("Your dog stares at you with those big brown eyes, you cannot resist")
        food -= 2
    if roll == 3:
        print("You find an ugly duckling, your hunger forces you to eat it")
        food += 1
    if roll == 4:
        print("you write letters to your friends asking for help, none comes")
        scandal += 1
    if roll == 5:
        print("out of sheer boredome you play solitaire, you manage to stay out of trouble for the duration")
    if roll == 6:
        print("More of your food spoils")
        food -= 1

def curtainRolls(): #3/4
    print("You take a peek through the curtains")
    
    roll = rnd.randint(1,6)
    
    if roll == 1:
        print("A small girl selling matchsticks dies on your lawn, Hans takes this hard for some reason")
        obsession -= 1
        scandal += 1
    if roll == 2:
        print("He hired a painter to have a portrait of himself, posing on your lawn")
        scandal += 1
    if roll == 3:
        print("He hired an orchestra to play loud music at your house")
        scandal += 2
    if roll == 4:
        print("A new person wanders past")
        obsession -= 1
    if roll == 5:
        print("He is talking to your neighbours about you")
        obsession += 1
    if roll == 6:
        print("He notices you looking through your curtains")
        obsession += 1

def anticsRolls(): #5/6
    print("Hans is up to something")
    
    roll = rnd.randint(1,6)
    
    if roll == 1:
        print("He is naked, although he claims his clothes are visible")
        scandal += 2
    if roll == 2:
        print("He is posting letters through your door, stacks of them")
        obsession -= 1
    if roll == 3:
        print("He is weeping and howling while rolling around on the grass")
        scandal += 1
        obsession -= 1
    if roll == 4:
        print("He stamps on a parcel intended for you")
        food -= 1
    if roll == 5:
        print("He is crying and hammering on the house")
        obsession -= 1
    if roll == 6:
        print("He is screaming through the letter box")
        scandal += 1
    
if __name__ == "__main__":
    main()
