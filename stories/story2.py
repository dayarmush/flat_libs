import os

def mad_lib():
    os.system('clear')

    room= input("enter a room in your house : ")
    drink= input("enter a drink : ")
    adjective = input("enter an adjective  : ")
    verb= input("enter a verb : ")
    body_part= input("enter a body part : ")
    verb= input("enter a verb : ")

    os.system('clear')

    story = "Late at night, as the wind howled outside, a young woman heard a faint whisper coming from her "+ room +". Terrified, she dropped her "+ drink +" but mustered the courage to investigate. As she opened the door, a pair of "+adjective +" eyes stared back at her, freezing her in place. The sinister whispers grew louder, revealing a chilling secret about the house's dark history. Shadows "+ verb +" menacingly on the walls as a "+ body_part +"-chilling coldness filled the room. Desperate to escape, she "+ verb +" towards the exit, but with each step, the house seemed to shift and block her path. In the end, the house consumed her, leaving behind only an eerie silence."

    print(story)
    return story
