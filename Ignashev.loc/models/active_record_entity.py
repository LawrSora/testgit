from services.db import Db
from abc import ABCMeta, abstractmethod

class ActiveRecordEntity(metaclass = ABCMeta):
    def get_id(self):
        return self._id
    @classmethod
    def find_all(cls):
        db = Db()
        table_name = cls.get_table_name()
        return db.query(f"SELECT * FROM {table_name}", {}, cls)
    
    @classmethod
    def get_by_id(cls, id):
        db = Db()
        table_name = cls.get_table_name()
        result = db.query(f"SELECT * FROM '{table_name}' WHERE id = {id}", {}, cls)
        if result != []:
            result = result[0]
        else:
            result = None
        return result
    
    @classmethod
    @abstractmethod
    def get_table_name():
        pass