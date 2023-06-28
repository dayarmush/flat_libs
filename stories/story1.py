import os

def mad_lib():
    
    os.system('clear')

    adjective= input("enter an adjective  : ")
    noun= input("enter a noun : ")
    name= input("enter a name : ")
    animal= input("enter an animal : ")
    adjective= input("enter an adjective  : ")
    place= input("enter a place  : ")
    verb= input("enter a verb  : ")
    noun= input("enter a plural noun  : ")
    noun= input("enter a noun : ")


    os.system('clear')

    story = " In a "+ adjective +"  world, a "+ noun +" named "+ name +" teamed up with a " + animal + " named "+ adjective +" for a hilarious comedy tour. Their witty banter and funny tales left audiences in stitches everywhere they performed. From bustling cafes to "+ place +", they brought laughter to people's lives. Their jokes about "+ verb +" "+ noun +" became legendary, making them the talk of the town. Through humor, they bridged gaps and united people from diverse backgrounds. Together, they proved that laughter truly is the best "+ noun +". "

    print(story)
    return story
