from models import User, db
from app import app

# Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

# If the table isn't empty, empty it
with app.app_context():
    User.query.delete()

# Add users
user_one = User(
    first_name="John",
    last_name="Branston",
    image_url="https://ssb.wiki.gallery/images/5/5b/SnakeSubArt.jpg",
)
user_two = User(
    first_name="Mike",
    last_name="Tanaka",
    image_url="https://ssb.wiki.gallery/images/5/5b/SnakeSubArt.jpg",
)
user_three = User(
    first_name="Marvin",
    last_name="Kastle",
    image_url="https://ssb.wiki.gallery/images/5/5b/SnakeSubArt.jpg",
)

# Add new users to session
with app.app_context():
    db.session.add_all([user_one, user_two, user_three])
    db.session.commit()
