#!/usr/bin/python
""" holds class Amenity"""
from base_model import BaseModel
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import storage_t

class Amenity(BaseModel):
    """Representation of Amenity """
    if storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
