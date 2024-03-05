import os
os.system("clear")
def ScenePitStart():
    inp = input()
    match inp:
        case "look":
            print("You try looking around but its too dark to see anything")
            ScenePitStart()
            
        case "climb":
            print("You Grasp at the walls looking for any holds,\nuntil eventually you find one and pull yourself up")
            input()
            SceneShedStart()
            
        case _:
            print("Invalid Command")
            ScenePitStart()

def SceneShedStart():

    os.system("clear")
    print("You find Yourself in what seems to be a small tool shed.\nTo the North there is a table.\nTo the south there is a door.\nTo the west there is a Window\n\n What will you do")
    inp = input()
    match inp:
        case "North":
            print("You try looking around but its too dark to see anything")
            ScenePitStart()
            
        case "South":
            print("You walk over to the door. Should you try to \nOPEN the door\n Go NORTH")

            print("The End?")
        case "West":
            print("You walk over to the window\nShould you try to\nLOOK outside,\nOPEN the window\nor go East")
        case _:
            print("Invalid Command\n Tip: To move in a direction type the cardinal direction")
            input()
            SceneShedStart()
    

    
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





