from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Story(Base):
    
    __tablename__ = 'stories'

    id = Column(Integer(), primary_key = True)
    title = Column(String())
    story = Column(String())

    def __repr__(self) -> str:
        return f'<Story {self.title}: {self.story}>'
        

if __name__ == '__main__':
    pass
    