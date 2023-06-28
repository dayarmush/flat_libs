from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
import random

Base = declarative_base()
engine = create_engine('sqlite:///stories.db')
Session = sessionmaker(bind = engine)
session = Session()

class Story(Base):

    @classmethod
    def get_by_title(cls, title):
        story = session.query(cls).filter(cls.title == title).first()
        print("\033[1;38;5;63m" + str(story) + "\033[0m")
    
    @classmethod
    def get_all_stories(cls):
        W  = '\033[0m'  # white (normal)
        R  = '\033[31m' # red
        G  = '\033[32m' # green
        O  = '\033[33m' # orange
        B  = '\033[34m' # blue
        P  = '\033[35m' # purple
        my_color = [W, R, G, O, B, P]
        stories = session.query(cls).all()
        for story in stories:
            print(f'{story}\n\n' , random.choice(my_color))
    

    __tablename__ = 'stories'

    id = Column(Integer(), primary_key = True)
    title = Column(String())
    story = Column(String())

    def __repr__(self) -> str:
        return f'<Story {self.title}: {self.story}>'
        
    