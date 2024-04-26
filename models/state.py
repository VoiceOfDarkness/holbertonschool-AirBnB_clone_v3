#!/usr/bin/python3
""" State Module for HBNB project """
import os

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import Base, BaseModel
from models.city import City


class State(BaseModel, Base):
    """State Model"""

    __tablename__ = "states"

    name: Mapped[str] = mapped_column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        cities: Mapped[list] = relationship("City", backref="state",
                                            cascade="delete")
    else:
        @property
        def cities(self):
            """Get a list of all related City objects."""
            from models import storage

            city_list = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
