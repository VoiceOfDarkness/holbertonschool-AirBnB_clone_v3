#!/usr/bin/python3
"""This module defines a class User"""
import hashlib

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import Base, BaseModel
from models.place import Place
from models.review import Review


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(128), nullable=False)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    first_name: Mapped[str] = mapped_column(String(128), nullable=True)
    last_name: Mapped[str] = mapped_column(String(128), nullable=True)
    places: Mapped["Place"] = relationship("Place", backref="user",
                                           cascade="delete")
    reviews: Mapped["Review"] = relationship("Review", backref="user",
                                             cascade="delete")

    def __init__(self, *args, **kwargs):
        """
        instantiates user object
        """
        if kwargs:
            pwd = kwargs.pop('password', None)
            if pwd:
                User.__set_password(self, pwd)
        super().__init__(*args, **kwargs)

    def __set_password(self, pwd):
        """
        custom setter: encrypts password to MD5
        """
        secure = hashlib.md5()
        secure.update(pwd.encode("utf-8"))
        secure_password = secure.hexdigest()
        setattr(self, "password", secure_password)
