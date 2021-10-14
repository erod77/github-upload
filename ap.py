from Database import Database
from models.blog import Blog
from models.posts import Post

Database.initialize()

blog = Blog(author="Eli",
            title="Sample Title",
            description="Sample Description"
            )
blog.new_post()

blog.save_to_mongodb()

from_database = Blog.from_mongodb(blog.id)

print(blog.get_posts())