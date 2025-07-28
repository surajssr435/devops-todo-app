#import os
#class Config:
#    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
#    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:suraj559@15.207.249.132:3306/devops_todo'
#    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:suraj559@host.docker.internal:3306/devops_todo'
#    SQLALCHEMY_TRACK_MODIFICATIONS = False
import os
from dotenv import load_dotenv

load_dotenv()  # Take environment variables from .env

class Config:
    # Flask Security
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-fallback-key'

    # Database Configuration
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', '3306')
    DB_NAME = os.environ.get('DB_NAME', 'devops_todo')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')

    # SQLAlchemy URI Construction
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@"
        f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # For Docker compatibility (uncomment if needed)
    # @property
    # def DOCKER_DATABASE_URI(self):
    #     return f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}@host.docker.internal:{self.DB_PORT}/{self.DB_NAME}"
