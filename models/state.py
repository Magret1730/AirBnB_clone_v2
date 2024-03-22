#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)

        cities = relationship("City", backref="state", cascade="all, delete")
    """else:
        name = """

    @property
    def cities(self):
        """
        Getter attribute to return a list of City instances with
        state_id equal to the current State.id
        """
        from models import storage
        matching_cities = []
        city_instances = storage.all(City)
        for city in city_instances.values():
            if city.state_id == self.id:
                matching_cities.append(city)
        return matching_cities
