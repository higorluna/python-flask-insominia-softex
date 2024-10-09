import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///produtos.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False