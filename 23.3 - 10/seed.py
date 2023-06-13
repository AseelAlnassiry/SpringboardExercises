from models import User, db
from app import app

db.drop_all()
db.create_all()

cole = User(
    first_name="cole",
    last_name="phelps",
    image_url="https://static.tvtropes.org/pmwiki/pub/images/cole_phelps.jpg",
)

stefan = User(
    first_name="stefan",
    last_name="bekowsky",
)

rusty = User(
    first_name="finbarr",
    last_name="galloway",
)

roy = User(
    first_name="roy",
    last_name="earle",
    image_url="https://pbs.twimg.com/media/FJeQL3KXoAILk_K.jpg",
)
biggs = User(
    first_name="herschel",
    last_name="biggs",
    image_url="https://static1.personality-database.com/profile_images/8b3ead43a7c943f3b99d0496b31bbad3.png",
)
skipper = User(
    first_name="james",
    last_name="donnelly",
    image_url="https://www.rockstargames.com/lanoire/dist/img/global/features/7d7cb74c789a39fe1f8f1071b17b7e37.jpg",
)
weak_sister = User(
    first_name="jacob",
    last_name="henry",
    image_url="https://cdn.videogamesblogger.com/wp-content/uploads/2011/05/la-noire-characters-list-jacob-henry.jpg",
)

sus_master = User(
    first_name="oswald",
    last_name="jacobs",
    image_url="https://staging.cohostcdn.org/attachment/e5ee3476-a1bf-4209-b809-16cdb6050fda/image.png?width=675&dpr=1",
)


db.session.add_all([stefan, rusty, cole, roy, biggs, skipper, weak_sister, sus_master])
db.session.commit()
