import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favCharacter = relationship('Fav_characters', backref='user', lazy=True)
    favPlanet = relationship('Fav_planets', backref='user', lazy=True)


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(Integer, nullable=False)
    eye_color = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    homeworld = Column(String(250), nullable=False)    
    mass = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    edited = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    starships= Column(String(250), nullable=False)
    url= Column(String(250), nullable=False)
    vehicles = Column(String(250), nullable=False)
    favCharacter= relationship('Fav_Characters', backref='characters', lazy=True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    climate = Column(String(250), nullable=False)
    created = Column(Integer(), nullable=False)
    diameter = Column(Integer(), nullable=False)
    edited = Column(Integer(), nullable=False)
    films = Column(String(250), nullable=False)
    gravit = Column(Integer(), nullable=False)
    name = Column(String(250), nullable=False)
    orbital_= Column(Integer(), nullable=False)
    populati = Column(Integer(), nullable=False)
    resident= Column(String(250), nullable=False)
    rotation_period = Column(Integer(), nullable=False)
    surface_water = Column(Integer(), nullable=False)
    terrain = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    favPlanet = relationship('Fav_planets', backref='planets', lazy=True)


class Fav_planets(Base):
    __tablename__ = 'fav_planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=False)


class Fav_characters(Base):
    __tablename__ = 'fav_characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable=False)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')