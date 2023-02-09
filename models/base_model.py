#!/usr/bin/python3
import uuid
from datetime import datetime
import models.engine.file_storage


"""
Module base_model
defines class BaseModel for AirBnb clone 
"""


class BaseModel:
    """defines all common atrributes/methods for other claseses"""

    def __init__(self, *args, **kwargs):
        """
        Initialise atrributes id, created-at, updated_at
        """
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                if "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                if "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel class"""
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dict__))
    def __repr__(self):
        """Return string represantion of BaseModel class"""
        return

    def save(self):
        """update updated_at time """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        create a dictionary represantion of attributes
        """
        dic = {}
        
        dic["__class__"] = self.__class__.__name__
        for key, Value in self.__dict__.items():
            if isinstance(Value, (datetime)):
                dic[key] = Value.isoformat()
            else:
                dic[key] = Value
        return dic
    
