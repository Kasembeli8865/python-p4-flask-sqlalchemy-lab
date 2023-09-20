#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)  # Use query.get(id) to retrieve an object by its primary key.

    if animal:
        response_body = f'''
            <h1>Information for {animal.name}</h1>
            <h2>Animal Species is {animal.species}</h2>
            <h2>Animal enclosure is {animal.enclosure_id}</h2>
            <h2>Zookeeper is {animal.zookeeper_id}</h2>
        '''
        response = make_response(response_body, 200)
    else:
        response = make_response('<h1>Animal not found</h1>', 404)

    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)

    if zookeeper:
        response_body = f'''
            <h1>Zookeeper is {zookeeper.name}</h1>
            <h2>Zookeeper's birthday is {zookeeper.birthday}</h2>
        '''
        response = make_response(response_body, 200)
    else:
        response = make_response('<h1>Zookeeper not found</h1>', 404)

    return response

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)

    if enclosure:
        response_body = f'''
            <h1>Information for {enclosure.environment}</h1>
            <h2>Enclosure is open for visitors {enclosure.open_to_visitors}</h2>
        '''
        response = make_response(response_body, 200)
    else:
        response = make_response('<h1>Enclosure not found</h1>', 404)

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
