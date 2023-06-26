
# name = input('put in a name:')
story_read = input('choose story:')

print(story_read)


class Story:
    
    def __init__(self, story):
        self.story = story

    def __repr__(self) -> str:
        return f'<Story {self.story}>'
        
        
        


if __name__ == '__main__':
    mike = Story(story_read)
    print(mike)