import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sge.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False