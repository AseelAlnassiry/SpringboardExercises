from models import Pet, db
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

with app.app_context():
    Pet.query.delete()

wilton = Pet(
    name="Wilton",
    species="Shiba Inu",
    photo_url="https://i.ytimg.com/vi/rx3LVs0_JR4/sddefault.jpg",
    age="3",
    notes="""This jerk loves nothing but being near people but not touching them. 
    He loves nibbling on peoples feet but hates pets.""",
    available=True,
)
decoy = Pet(
    name="Decoy",
    species="Husky",
    photo_url="https://t3.gstatic.com/licensed-image?q=tbn:ANd9GcSrmXDX0SAyzNSjl3zZuG-BgzTK1qsmo-9r4OvKZvJMtCHgxLiS7lqlyE3dxqCCkJ-T",
    age="3",
    notes="""This jerk loves nothing but being near people but not touching them. 
    He loves nibbling on peoples feet but hates pets.""",
    available=True,
)
raven = Pet(
    name="Raven",
    species="Belgian Malinois",
    photo_url="https://preview.redd.it/hun69ozfr9k81.jpg?width=640&crop=smart&auto=webp&s=f1c5d16844af2a39996466cb982b0627419223f5",
    age="3",
    notes="""This jerk loves nothing but being near people but not touching them. 
    He loves nibbling on peoples feet but hates pets.""",
    available=False,
)

with app.app_context():
    db.session.add_all([wilton, decoy, raven])
    db.session.commit()
