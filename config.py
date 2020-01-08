import os
basedir = os.path.abspath(os.path.dirname(__file__)) #Makes file path relative, works on all OS, regardless of file path on
#different OS

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False