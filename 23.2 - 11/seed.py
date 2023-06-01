from models import User, Post, db
from app import app

# Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

# If the table isn't empty, empty it
with app.app_context():
    User.query.delete()
    Post.query.delete()


# Add Users
mike_trant = User(first_name="mike", last_name="trant")
adam_drive = User(first_name="adam", last_name="drive")
haley_swart = User(first_name="haley", last_name="swart")

# Add new users to psql
with app.app_context():
    db.session.add_all([mike_trant, adam_drive, haley_swart])
    db.session.commit()

# Add Posts
post_one = Post(title="Why am I here?", content="Just to Suffer...", user_id=1)
post_two = Post(title="Every Night", content="I feel my limbs", user_id=2)
post_three = Post(title="The Comrades I lost", content="I can still hear", user_id=1)

# Add new posts to psql
with app.app_context():
    db.session.add_all([post_one, post_two, post_three])
    db.session.commit()
