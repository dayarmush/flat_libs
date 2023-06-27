import os

def mad_lib():
    
    os.system('clear')

    animals= input('enter a animal name : ')
    # profession = input('enter a profession name: ')
    # cloth = input('enter a piece of cloth name: ')
    # things = input('enter a thing name: ')
    # name= input('enter a name: ')
    # place = input('enter a place name: ')
    # verb = input('enter a verb in ing form: ')
    # food = input('food name: ')

    # if (animals == 'q' 
    #     or profession == 'q' 
    #     or cloth == 'q' 
    #     or things == 'q' 
    #     or name == 'q' 
    #     or place == 'q' 
    #     or verb == 'q' 
    #     or food == 'q'):
    #     exit()


    os.system('clear')

    # text = 'say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind'

    text = 'say, ' + animals + 'the photographer said as the camera flashed! \nand I had gone to to get our photos taken on my birthday. \nThe first photo we really wanted was a picture of us dressed as pretending to be a. \nwhen we saw the second photo, it was exactly what I wanted. \nWe both looked like wearing and --exactly what I had in mind'

    print(text)
    return text
