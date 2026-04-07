

  # from services.db import Db
import re
from models.active_record_entity import ActiveRecordEntity
from exceptions import InvalidArgumentException
from email_validator import validate_email, EmailNotValidError
import hashlib
import random

import re

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

    def refresh_auth_token(self):
        self._auth_token = hashlib.sha1(random.randbytes(100)).hexdigets()
        + hashlib.sha1(random.randbytes(100)).hexdigets()

    def sign_up(user_data):
        if not user_data['nickname']:
            raise InvalidArgumentException('Не передан логин')
        
        if re.search(r'^[a-zA-Z0-9]+$', user_data['nickname']) is None:
            raise InvalidArgumentException('Логин может состоять только из символов латинского алфавита и цифр')
        
        if __class__.find_one_by_column('nickname', user_data['nickname']):
            raise InvalidArgumentException('Логин уже существует')
        
        if not user_data['email']:
            raise InvalidArgumentException('Не передан email')
        try:
            validate_email(user_data['email'])
        except EmailNotValidError as e:
            raise InvalidArgumentException('Неверный email')
        
        if __class__.find_one_by_column('email', user_data['email']):
            raise InvalidArgumentException('Email уже существует')
        
        if not user_data['password']:
            raise InvalidArgumentException('Не передан пароль')
        
    def sign_in(user_data):
        if not user_data['nickname']:
            raise InvalidArgumentException('Не передан логин')
        
        if not user_data['password']:
            raise InvalidArgumentException('Не передан пароль')
        
        user = User.find_one_by_column('nickname', user_data['nickname'])

        if user is None:
            raise InvalidArgumentException("Пользователь не найден")
        if check_pasword_hash(user_data['password'], user.get_password_hash):
            raise InvalidArgumentException('Неверный логин или пароль')
        user.refresh_auth_token()
        user.save()
        return user
        
        user = User()
        user._nickname = user_data['nickname']
        user._email = user_data['email']
        user._is_confirmed = True
        user._role = 'user'
        user._password_hadh = generate_password_hash(user_data['password'])
        user.refresh_auth_token()
        user.save()
        return user
        
    @staticmethod
    def get_table_name():
        return 'users'