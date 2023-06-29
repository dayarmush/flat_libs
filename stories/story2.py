import os

def mad_lib():
    os.system('clear')


    room = input("\033[92mEnter a room in your house: \033[0m")
    if room.lower() == 'q':
        exit()

    drink = input("\033[92mEnter a drink: \033[0m")
    if drink.lower() == 'q':
        exit()

    adjective = input("\033[92mEnter an adjective: \033[0m")
    if adjective.lower() == 'q':
        exit()

    verb1 = input("\033[92mEnter a verb: \033[0m")
    if verb1.lower() == 'q':
        exit()

    body_part = input("\033[92mEnter a body part: \033[0m")
    if body_part.lower() == 'q':
        exit()

    verb2 = input("\033[92mEnter a verb: \033[0m")
    if verb2.lower() == 'q':
        exit()

    os.system('clear')

    story = " \033[92mLate at night, as the wind howled outside, a young woman heard a faint whisper coming from her " + room + ".\n Terrified, she dropped her " + drink + " but mustered the courage to investigate.\n As she opened the door, a pair of " + adjective + " eyes stared back at her, freezing her in place.\n The sinister whispers grew louder, revealing a chilling secret about the house's dark history.\n Shadows " + verb1 + " menacingly on the walls as a " + body_part + "-chilling coldness filled the room.\n Desperate to escape, she " + verb2 + " towards the exit, but with each step, the house seemed to shift and block her path.\n In the end, the house consumed her, leaving behind only an eerie silence.\033[0m \n\n"

    print(story)
    return story


