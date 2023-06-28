import os

def mad_lib():
    os.system('clear')

    town = input("enter a name of a town  : ")
    verb= input("enter a verb in the past tense  : ")
    body_part= input("enter a body part plural  : ")
    verb = input("enter a verb ending in “ing”  : ")
    body_part= input("enter a body part plural  : ")
    verb = input("enter a verb  : ")

    os.system('clear')

    story = "In the picturesque town of "+ town +", two strangers "+ verb +" on a crowded street, their "+ body_part +" locking in an instant connection. Time seemed to stand still as they exchanged a smile that spoke volumes. Fate continued to bring them together, their paths "+ verb +" at every turn. They shared stolen glances, sparking a whirlwind of emotions that neither could deny. With each encounter, their "+ body_part +" grew closer, until they couldn't resist the pull any longer. Finally, they embraced, sealing their love in a passionate "+ verb +", knowing that their destinies were forever intertwined."

    print(story)
    return story