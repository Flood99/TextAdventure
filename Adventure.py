    
import os   
os.system("clear")

class Player:
     def __init__(self,name):
         self.name = name
     frontDoorKey = False



def ScenePitStart():
    inp = input()
    match inp:
        case "look":
            print("You look")
            print("The End?")
            
        case "climb":
            print("you climb")
            print("The End?")
            
        case _:
            print("Invalid Command")
            print(input)
            ScenePitStart()

        

    
def Start():   
    print("Enter a name!")
    player = Player(input())
    print("Hello " + player.name + "! Press enter to continue or type back to reenter a name")
    if input() == "back":
        Start()
    else:
        print("You wake up in a dark pit\n Tip: Use Enter to move text forward")
        input()
        print("You could LOOK around or try to CLIMB out")
        ScenePitStart()

Start()





