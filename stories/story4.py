import os

def mad_lib():
    os.system('clear')

    city= input("enter a name of a city  : ")
    occupation = input("enter an occupation   : ")
    name= input("enter a name  : ")
    occupation = input("enter an occupation   : ")
    weapon= input("enter a weapon  : ")
    adjective = input("enter an adjective   : ")

    os.system('clear')

    story = "In the bustling city of " + city + ", a fearless ex-" + occupation +" named "+ name +" found himself caught in a web of conspiracy and danger. He embarked on a mission to uncover the truth behind a powerful "+ occupation +" organization. He encountered relentless adversaries at every turn, engaging in intense "+ weapon +" fights and adrenaline-pumping chase sequences. As the plot thickened, he discovered a government conspiracy that threatened the entire nation. With "+ adjective +" determination, he fought against all odds, single-handedly dismantling the criminal empire and exposing the corrupt officials. In the end, justice prevailed, and he emerged as a hero, leaving a legacy of courage and resilience for all to remember."

    print(story)
    return story
