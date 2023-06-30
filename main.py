import importlib
import sys
import os
from classes.story import Story, Base, engine, session

def exit_program():
    sys.exit()

def main_component():
    print('Enter "Q" anytime to exit')
    story_num = input("\033[1;38;5;63m" + 'Select 1 for Comedy,  2 for Scary, 3 for Romance, 4 for Action: ' + "\033[0m")

    if story_num.lower() == 'q' or len(story_num) > 20:
        exit_program()

    package_name = __package__ or '.'.join(__name__.split('.')[:-1])
    stories_path = os.path.join(os.path.dirname(__file__), '.', 'stories')
    sys.path.append(stories_path)
    story_module = importlib.import_module(f'story{story_num}')
    mad_lib_function = getattr(story_module, 'mad_lib')

    Base.metadata.create_all(engine)

    story = mad_lib_function()

    title = input("\033[1;38;5;63m" + 'input title: ' + "\033[0m")
    if title.lower() == 'q' or len(title) > 20:
        exit_program()

    os.system('clear')
    another_story = input("\033[1;38;5;63m" + 'Would you like another story? [Y/N]: ' + "\033[0m")

    title = Story(title=title, story=story)

    session.add(title)
    session.commit()
    
    if another_story.lower() == 'y' and len(another_story) <= 3:
        os.system('clear')
        main_component()
    else:
        question = input("\033[1;38;5;63m" + 'Would you like to browse previous stories [Y/N]: ' + "\033[0m")
        os.system('clear')
        if question.lower() == 'y':
            a_or_b = input("\033[1;38;5;63m" + 'A: For all of the stories. B: For one particular story: ' + "\033[0m")
            os.system('clear')
            if a_or_b.lower() == 'a':
                Story.get_all_stories()
            else:
                grab_title = input("\033[1;38;5;63m" + 'What title are you looking for? ' + "\033[0m")
                os.system('clear')
                Story.get_by_title(grab_title)

main_component()
exit_program()


# Stories: funny story, sad story, horror story, romance story, stupid story
# Laughing ascii
# Add color
# Center text


