
def ScenePitStart():
    inp = input()
    match inp:
        case "look":
            print("You look")
            print("The End?")
            
        case "Climb":
            print("you climb")
            print("The End?")
        case _:
            print("Invalid Command")
            ScenePitStart()

        

    
def Start():   
    print("Enter a name!")
    name = input()
    print("Hello " + name + "! Press enter to continue or type back to reenter a name")
    if input() == "back":
        Start()
    else:
        print("You wake up in a dark pit\n Tip: Use Enter to move text forward")
        input()
        print("You could LOOK around or try to CLIMB out")
        ScenePitStart()

Start()





