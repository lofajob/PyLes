# -*- coding: utf-8 -*-

class Person(object):
    """Base class"""
    def __init__(self, Name):
        self.Name = Name

    def ShowData(self):
        """
        This method will present attributes of current person
        """
        part_of_message = "Person's %s is %s. "
        message = ""
        for key in self.__dict__:
             message += part_of_message % (key ,self.__dict__[key])

        print message.rstrip()


class Student(Person):
    def __init__(self, Name, Education):
        Person.__init__(self, Name)
        self.Education = Education

class Worker(Person):
    def __init__(self, Name, WorkPlace):
        Person.__init__(self, Name)
        self.WorkPlace = WorkPlace


class Academy(object):
    """Class Academy"""
    def __init__(self):
        self.collection = []

    def ShowAll(self):
        for person in self.collection:
            person.ShowData()

    def AddPerson(self, obj, *args, **kwargs):
        self.collection.append(obj) 

