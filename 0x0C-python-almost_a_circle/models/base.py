#!/usr/bin/python3
"""base class for all other classes"""
import json
import os
import csv
import turtle


class Base:
    """The base class"""
    
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries is " ":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json representation to a file"""
        file_name = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open(file_name, 'w') as json_file:
            json_file.write(cls.to_json_string(new_list))
    
    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation json_string
        Args:
            json_string(str): a string representing a list
            of dictionaries
        """
        if json_string is None:
            return []
        if json_string == [] or not isinstance(json_string, str):
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            result = cls(32, 3)
            result.update(**dictionary)
            return result
        if cls.__name__ == "Square":
            result = cls(32)
            result.update(**dictionary)
            return result
    
    @classmethod
    def load_from_file(cls):
        """A class method that returns a list instance"""
        list_instance = []
        file_name = cls.__name__ + ".json"
        if os.path.isfile(file_name):
            with open(file_name, "r") as file:
                s = cls.from_json_string(file.read())
            for i in s:
                list_instance.append(cls.create(**i))
            return list_instance
        return []
    
    @classmethod
    def load_from_file_csv(cls):
        """Loads from csv file"""
        list_instance = []
        name = cls.__name__ + ".csv"
        if os.path.isfile(name):
            with open(name, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    d = {key: int(value) for key, value in row.items()}
                    list_instance.append(cls.create(**d))
            return list_instance
        return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws sqaures and rectangles"""
        for i in list_rectangles + list_squares:
            tt = turtle.Turtle()
            tt.shape("turtle")
            turtle.bgcolor("black")
            tt.fillcolor("white")
            tt.begin_fill()
            tt.pen(fillcolor="white", pencolor="red", pensize=2)
            for _ in range(2):
                tt.forward(i.width)
                tt.right(90)
                tt.forward(i.height)
                tt.right(90)
            tt.end_fill()
            turtle.done()