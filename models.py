from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Setup for table containing pet info"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    species = db.Column(db.String(), nullable=False)
    photo_url = db.Column(db.String, nullable=True, default='https://www.crossdogs.org/images/dog-placeholder.png')
    age = db.Column(db.Integer(), nullable=True, default='N/A')
    notes = db.Column(db.String(), nullable=True)
    available = db.Column(db.Boolean(), default=True)

    def __repr__(self):
        p = self
        return f"<Pet id:{p.id} name:{p.name} species:{p.species} age:{p.age}>"

