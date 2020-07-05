class Article:
    '''
    Article class to define article objects
    '''

    def __init__(self,id,name,author,title,description,content):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.content = content