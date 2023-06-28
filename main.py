import importlib; import sys; import os; import time
from classes.story import Story, Base, engine, session

print('Enter "Q" anytime to exit')
story_num = input("\033[1;38;5;63m" + 'Select a Story:' + "\033[0m")

if story_num == 'q' or len(story_num) > 20:
    exit()

package_name = __package__ or '.'.join(__name__.split('.')[:-1])
stories_path = os.path.join(os.path.dirname(__file__), '.', 'stories')
sys.path.append(stories_path)
story_module = importlib.import_module(f'story{story_num}')
mad_lib_function = getattr(story_module, 'mad_lib')

Base.metadata.create_all(engine)

story = mad_lib_function()

# time.sleep(10)
# os.system('clear')

title = input("\033[1;38;5;63m" + 'input title: ' + "\033[0m")
if title == 'q' or len(title) > 20:
    exit()

os.system('clear')
another_story = input("\033[1;38;5;63m" + 'Would you like another story? [Y/N]: ' + "\033[0m")

title = Story(title=title, story=story)

session.add(title)
session.commit()
    
if another_story == 'y' and len(another_story) <= 3:
    os.system('clear')
    os.system('python main.py')
elif another_story == 'q':
    exit()
else:
    question = input("\033[1;38;5;63m" + 'Would you like to browse previous stories [Y/N]: ' + "\033[0m")
    os.system('clear')
    if question == 'y':
        a_or_b = input("\033[1;38;5;63m" + 'A: For all of the stories. B: For one particular story: ' + "\033[0m")
        os.system('clear')
        if a_or_b == 'a':
            Story.get_all_stories()
        else:
            grab_title = input("\033[1;38;5;63m" + 'What title are you looking for? ' + "\033[0m")
            os.system('clear')
            Story.get_by_title(grab_title)
    else:
        exit()


# Stories: funny story, sad story, horror story, romance story, stupid story
# Laughing ascii
# Add color
# Center text


