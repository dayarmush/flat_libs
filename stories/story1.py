import os

def mad_lib():
        
        os.system('clear')

        adjective = input("\033[92mEnter an adjective: \033[0m")
        if adjective.lower() == 'q':
            exit()

        name1 = input("\033[92mEnter a name: \033[0m")
        if name1.lower() == 'q':
            exit()

        animal = input("\033[92mEnter an animal: \033[0m")
        if animal.lower() == 'q':
            exit()

        name2 = input("\033[92mEnter a name: \033[0m")
        if name2.lower() == 'q':
            exit()

        place = input("\033[92mEnter a place: \033[0m")
        if place.lower() == 'q':
            exit()

        verb = input("\033[92mEnter a verb: \033[0m")
        if verb.lower() == 'q':
            exit()

        noun1 = input("\033[92mEnter a plural noun: \033[0m")
        if noun1.lower() == 'q':
            exit()

        noun2 = input("\033[92mEnter a noun: \033[0m")
        if noun2.lower() == 'q':
            exit()

        os.system('clear')

        story = " \033[92mIn a " + adjective + " world, a man named " + name1 + " teamed up with a " + animal + " named " + name2 + " for a hilarious comedy tour. \n Their witty banter and funny tales left audiences in stitches everywhere they performed. \n From bustling cafes to " + place + ", they brought laughter to people's lives.\n Their jokes about " + verb + " " + noun1 + " became legendary, making them the talk of the town.\n Through humor, they bridged gaps and united people from diverse backgrounds.\n Together, they proved that laughter truly is the best " + noun2 + ".\033[0m \n\n"

        print(story)



