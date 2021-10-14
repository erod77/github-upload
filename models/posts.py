import datetime
from Database import Database
import uuid


class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date =  date
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongodb(self):
        Database.insert(collections='posts',
                        data=self.json())

    def json(self):
        return{
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date

        }
        @classmethod
        def from_mongodb(cls, id):
            post_data = Database.find_one(collections='posts', query={'id': id})
            return cls(blog_id=post_data['blog_id'],
                       title=post_data['title'],
                       content=post_data['content'],
                       author=post_data['author'],
                       date=post_data['created_date'],
                       id=post_data['id'])

        @staticmethod
        def from_blog(id):
            return [post for post in Database.find(collections='posts', query={'blog_id': id})]

    @classmethod
    def from_blog(cls, id):
        pass


