

  # from services.db import Db

from models.active_record_entity import ActiveRecordEntity

class User(ActiveRecordEntity):
    _nickname = None
    _email = None
    _is_confirmed = None
    _role = None
    _password_hash = None
    _auth_token = None
    _created_at = None

    def get_author_id(self):
        return self._author_id
    
    def get_text(self):
        return self._text

    def get_name(self):
        return self._name

    def get_created_at(self):
        return self._created_at

    def set_author_id(self,_author_id):
        self._author_id = _author_id

    def set_name(self,name):
        self._name = name

    def set_text(self,_text):
        self._text = _text

    def set_created_at(self,_created_at):
        self._created_at = _created_at

    def get_nickname(self):
        return self._nickname
    
    def get_email(self):
        return self._email
    
    def get_role(self):
        return self._role
    
    def get_password_hash(self):
        return self._auth_token
    
    def get_created_at(self):
        return self._created_at
    
    def set_nickname(self, nickname):
        self._nickname = nickname

    def set_email(self, email):
        self._email = email

    def set_role(self, role):
        self._role = role       

    # def find_all(cls):
    #     db = Db()
    #     return db.query("SELECT * FROM 'articles'",{},cls)
    #     # print(items)
    # def get_by_id(id,cls):
    #     db = Db()
    #     return db.query(f"SELECT * FROM 'articles' WHERE id={id}",{},cls)[0]