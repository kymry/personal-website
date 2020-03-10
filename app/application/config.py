import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or "6IxOGEa58UtIzWujwoTAIzzsb832OcLmr8V-mNSBoA4"
    #DATABASE = os.environ.get('DATABASE') or os.path.join(basedir, 'databases/astronomicaldata.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
