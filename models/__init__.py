#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv
import sys
sys.path.append('/path/to/parent/directory')

storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
