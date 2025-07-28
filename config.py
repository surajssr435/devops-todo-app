import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:suraj559@15.207.249.132:3306/devops_todo'
#    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:suraj559@host.docker.internal:3306/devops_todo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
