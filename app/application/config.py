import os
from dotenv import load_dotenv


load_dotenv(os.path.join(os.path.abspath('.'), '.env'))


class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or "6IxOGEa58UtIzWujwoTAIzzsb832OcLmr8V-mNSBoA4"
