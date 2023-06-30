import os

def mad_lib():
    os.system('clear')

    town = input("\033[92mEnter a name of a town: \033[0m")
    if town.lower() == 'q':
        exit()

    verb1 = input("\033[92mEnter a verb in the past tense: \033[0m")
    if verb1.lower() == 'q':
        exit()

    body_part1 = input("\033[92mEnter a body part plural: \033[0m")
    if body_part1.lower() == 'q':
        exit()

    verb2 = input("\033[92mEnter a verb ending in 'ing': \033[0m")
    if verb2.lower() == 'q':
        exit()

    body_part2 = input("\033[92mEnter a body part plural: \033[0m")
    if body_part2.lower() == 'q':
        exit()

    verb3 = input("\033[92mEnter a verb: \033[0m")
    if verb3.lower() == 'q':
        exit()

    os.system('clear')

    story = " \033[92mIn the picturesque town of " + town + ", two strangers " + verb1 + " on a crowded street, their " + body_part1 + " locking in an instant connection.\n Time seemed to stand still as they exchanged a smile that spoke volumes.\n Fate continued to bring them together, their paths " + verb2 + " at every turn.\n They shared stolen glances, sparking a whirlwind of emotions that neither could deny.\n With each encounter, their " + body_part2 + " grew closer, until they couldn't resist the pull any longer.\n Finally, they embraced, sealing their love in a passionate " + verb3 + ", knowing that their destinies were forever intertwined.\033[0m \n\n"

    print(story)
    return story

