import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASS']
host = os.environ['MYSQL_HOST']
database = os.environ['MYSQL_DB']
port = os.environ['MYSQL_PORT']


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or "6IxOGEa58UtIzWujwoTAIzzsb832OcLmr8V-mNSBoA4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')