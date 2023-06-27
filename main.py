import importlib; import sys; import os; import time
from classes.story import Story, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

story_num = input('choose story:')

if story_num == 'q':
    exit()

package_name = __package__ or '.'.join(__name__.split('.')[:-1])
stories_path = os.path.join(os.path.dirname(__file__), '.', 'stories')
sys.path.append(stories_path)
story_module = importlib.import_module(f'story{story_num}')
mad_lib_function = getattr(story_module, 'mad_lib')


engine = create_engine('sqlite:///stories.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()

story = mad_lib_function()

# time.sleep(10)

title = input('input title:')
if title == 'q':
    exit()

os.system('clear')
another_story = input('Would you like another story [Y/N]:')

title = Story(title=title, story=story)

session.add(title)
session.commit()

    
if another_story == 'y':
    os.system('clear')
    os.system('python main.py')
else:
    exit()



