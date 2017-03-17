from abc import ABCMeta, abstractmethod
from os import path
import pickle
import json


class ParamHandlerException(BaseException):
    pass

class ParamHandler(metaclass=ABCMeta):
    types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name!')
        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException('Class "{}" is not ParamHandler!'.format(klass)
        )

        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):

        _, ext = path.splitext(str(source).lower())
        ext = ext.lstrip('.')

        klass = cls.types.get(ext)

        if klass is None:
            raise ParamHandlerException('Type "{}" not found!'.format(ext))
        return klass(source, *args, **kwargs)


class JsonParamHandler(ParamHandler):
    def read(self):
        """
        Чтение из текстового файла и присвоение значений в self.params """

    def write(self):
        """
        Запись в текстовый файл параметров self.params """

class PickleParamHandler(ParamHandler):

    def read(self):

        with open(self.source, 'rb') as f:
            print(pickle.load(f))

    def write(self):

        with open(self.source, 'wb') as f:
            pickle.dump(self.data, f)


ParamHandler.add_type('pickle', PickleParamHandler)
ParamHandler.add_type('json', JsonParamHandler)

config = ParamHandler.get_instance('./datafile.pickle')
config.add_param('data', '{"users": [{"id": 1, "name": "Vasya"}, {"id": 2, "name": "Kolya"}]}')
config.write() # запись файла в Pickle формате

config = ParamHandler.get_instance('./datafile.pickle')
config.read()
