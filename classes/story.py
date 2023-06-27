from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

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
        stories = session.query(cls).all()
        stories_str = "\n\n".join(str(story) for story in stories)
        print("\033[1;38;5;63m" + stories_str + "\033[0m")
    
    __tablename__ = 'stories'

    id = Column(Integer(), primary_key = True)
    title = Column(String())
    story = Column(String())

    def __repr__(self) -> str:
        return f'<Story {self.title}: {self.story}>'
        
    