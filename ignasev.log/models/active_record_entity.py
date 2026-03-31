from services.db import Db

class ActiveRecordEntity:
    def findAll(cls):
        db = Db()
        return db.query("SELECT * FROM 'articles'", {}, cls)
    
    def get_by_id(id, cls):
        db = Db()
        retutn db.query(f"SELECT * FROM 'articles' WHERE id= {id}", {}, cls)[0]