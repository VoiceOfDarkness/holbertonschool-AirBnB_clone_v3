#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""

    __file_path = "file.json"
    __objects = {}

    def all(self, obj=None):
        """Returns the list of objects of one type of class"""
        if obj:
            temp = {}
            for key, val in self.__objects.items():
                if obj.__name__ in key:
                    temp[key] = val
            return temp
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()["__class__"] + "." + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, "w") as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            if key in self.all():
                del self.all()[key]
            self.save()

    def reload(self):
        """Loads storage dictionary from file"""
        from models.amenity import Amenity
        from models.base_model import BaseModel
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, "r") as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val["__class__"]](**val)
        except FileNotFoundError:
            pass

    def get(self, cls, id):
        """A method to retrieve one object"""
        if cls and id:
            key = cls.__name__ + "." + id
            return self.all().get(key)
        return None

    def count(self, cls=None):
        """A method to count the number of objects in storage"""
        return len(self.all(cls))

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
