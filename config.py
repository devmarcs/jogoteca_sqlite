import os

SECRET_KEY = 'marc123'

SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://{usuario}:{senha}@{servidor}/{database}'.format(
        
        usuario='postgres',
        senha='123',
        servidor='localhost',
        database='jogoteca'
    )


'''UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
UPLOAD_PATH_USER = os.path.dirname(os.path.abspath(__file__)) + '/uploadsUser
'''
