answer = input("Do You Want To Play This Game[Yes/No]:")

if answer == "yes":
    print("Welcome to the Game!")
    answer = input("Do You Want To Go Jungle or Cave[Jungle/Cave]")
    if answer == "Jungle":
        print("You See The Hungry Tiger Will Eat You ")
    elif answer == "cave":
        print("You Seen The Bear In Front Of Cave")
        answer = input("Do You Want To Fight With The Bear Run or Away! [Fight/Run]")
        if answer == "Fight":
            print("Bear Is Too Much Strong! You Lost")
        else:
            print("WOW! Still You Are Alive!")


else:
    print("The Game Closed")


