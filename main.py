import importlib; import sys; import os; import time
from classes.story import Story, Base, engine, session

story_num = input("\033[1;38;5;63m" + 'Select a Story:' + "\033[0m")

if story_num == 'q':
    exit()

package_name = __package__ or '.'.join(__name__.split('.')[:-1])
stories_path = os.path.join(os.path.dirname(__file__), '.', 'stories')
sys.path.append(stories_path)
story_module = importlib.import_module(f'story{story_num}')
mad_lib_function = getattr(story_module, 'mad_lib')

Base.metadata.create_all(engine)

story = mad_lib_function()

# time.sleep(10)

title = input("\033[1;38;5;63m" + 'input title:' + "\033[0m")
if title == 'q':
    exit()

os.system('clear')
another_story = input("\033[1;38;5;63m" + 'Would you like another story? [Y/N]:' + "\033[0m")

title = Story(title=title, story=story)

session.add(title)
session.commit()

    
if another_story == 'y':
    os.system('clear')
    os.system('python main.py')
else:
    exit()

# Stories: funny story, sad story, horror story, romance story, stupid story
# Laughing ascii
# Add color
# Center text


