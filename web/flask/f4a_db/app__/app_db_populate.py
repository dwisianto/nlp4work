# flask db init
# flask db migrate
# flask db upgrade

from app import app, db
from app.models import User, Post

# https://overiq.com/flask-101/contexts-in-flask/
app.app_context().push()
u = User(username='john', email='john@example.com')
db.session.add(u)
db.session.commit()

u = User(username='susan', email='susan@example.com')
db.session.add(u)
db.session.commit()

users = User.query.all()
for u in users: 
    print(u.id, u.username)


# Now let's add a blog post:
# u = User.query.get(1)
# p = Post(body='my first post!', author=u)
# db.session.add(p)
# db.session.commit()




>>> # get all posts written by a user
>>> u = User.query.get(1)
>>> u
<User john>
>>> posts = u.posts.all()
>>> posts
[<Post my first post!>]

>>> # same, but with a user that has no posts
>>> u = User.query.get(2)
>>> u
<User susan>
>>> u.posts.all()
[]

>>> # print post author and body for all posts
>>> posts = Post.query.all()
>>> for p in posts:
...     print(p.id, p.author.username, p.body)
...
1 john my first post!

# get all users in reverse alphabetical order
User.query.order_by(User.username.desc()).all()
# [<User susan>, <User john>]


#
# [] Cleanup
#
users = User.query.all()
for u in users:
    db.session.delete(u)

posts = Post.query.all()
for p in posts:
    db.session.delete(p)

db.session.commit()