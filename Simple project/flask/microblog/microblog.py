from app import apps, db
from app.models import User, Post

@apps.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

apps.app_context().push()

u = User(username='John', email='john@example.com')
db.session.add(u)
db.session.commit()

u = User(username='Susan', email='john@example.com')
db.session.add(u)
db.session.commit()


u = User.query.get(1)
p = Post(body='my first post!', author=u)
db.session.add(p)
db.session.commit()

users = User.query.all()
for u in users:
    print(u.id, u.username)

posts = Post.query.all()
for p in posts:
    print(p.id, p.author.username, p.body)


users = User.query.all()
for u in users:
    db.session.delete(u)

posts = Post.query.all()
for p in posts:
    db.session.delete(p)

db.session.commit()