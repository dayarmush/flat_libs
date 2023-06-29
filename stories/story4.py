import os

def mad_lib():
    os.system('clear')

    city = input("\033[92mEnter a name of a city: \033[0m")
    if city.lower() == 'q':
        exit()

    occupation1 = input("\033[92mEnter an occupation: \033[0m")
    if occupation1.lower() == 'q':
        exit()

    name = input("\033[92mEnter a name: \033[0m")
    if name.lower() == 'q':
        exit()

    occupation2 = input("\033[92mEnter an occupation: \033[0m")
    if occupation2.lower() == 'q':
        exit()

    object = input("\033[92mEnter an object: \033[0m")
    if object.lower() == 'q':
        exit()

    adjective = input("\033[92mEnter an adjective: \033[0m")
    if adjective.lower() == 'q':
        exit()

    os.system('clear')

    story = " \033[92mIn the bustling city of " + city + ", a fearless ex-" + occupation1 + " named " + name + " found himself caught in a web of conspiracy and danger.\n He embarked on a mission to uncover the truth behind a powerful " + occupation2 + " organization.\n He encountered relentless adversaries at every turn, engaging in intense " + object + " fights and adrenaline-pumping chase sequences.\n As the plot thickened, he discovered a government conspiracy that threatened the entire nation.\n With " + adjective + " determination, he fought against all odds, single-handedly dismantling the criminal empire and exposing the corrupt officials.\n In the end, justice prevailed, and he emerged as a hero, leaving a legacy of courage and resilience for all to remember.\033[0m \n\n"

    print(story)
    return story








