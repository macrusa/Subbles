'''
Created on Mar 31, 2015

@author: Jean
'''
__all__ = ['db', 'OAuth', 'User', 'Forget', \
        'init_account_db']

import hashlib
from datetime import datetime
from utils.token import create_token
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def init_account_db(app):
    db.init_app(app)
    db.app = app
    db.create_all()

class User(object):
    '''
    classdocs
    '''
    USER = 0
    ADMIN = 888
    


    def __init__(self, name, password, lvl):
        '''
        Constructor
        '''
        self.name = name
        self.password=password
        self.lvl = lvl