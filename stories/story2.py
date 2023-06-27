import os

def mad_lib():
    os.system('clear')

    adjective = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name :')
    place = input('enter a place name : ')
    person= input('enter a person name : ')
    adjective1 = input('enter a adjective : ')
    insect= input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')

    os.system('clear')

    story = 'Last night I dreamed I was a ' + adjective + ' butterfly with ' + color + ' splotches that looked like '+ thing + ' .I flew to ' + place + ' with my best friend and '+ person + ' who was a '+ adjective1 + ' ' + insect +' .We ate some ' + food + ' when we got there and then decided to '+ verb + ' and the dream ended when I said-- lets ' + verb + '.'

    print(story)
    return story
