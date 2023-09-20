from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.Date)
    
    # Define a relationship to the Animal model
    animals = db.relationship('Animal', backref='zookeeper')

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __repr__(self):
        return f'<Zookeeper {self.name}>'

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)  # Grass, Sand, or Water
    open_to_visitors = db.Column(db.Boolean, default=False)
    
    # Define a relationship to the Animal model
    animals = db.relationship('Animal', backref='enclosure')

    def __init__(self, environment, open_to_visitors=False):
        self.environment = environment
        self.open_to_visitors = open_to_visitors

    def __repr__(self):
        return f'<Enclosure {self.id}: {self.environment}>'


class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    def __init__(self, name, species, zookeeper_id, enclosure_id):
        self.name = name
        self.species = species
        self.zookeeper_id = zookeeper_id
        self.enclosure_id = enclosure_id

    def __repr__(self):
        return f'<Animal {self.name}: {self.species}>'
