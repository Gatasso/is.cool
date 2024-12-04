import os
# basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY= os.environ.get('SECRET_KEY') or '0d0m0C_3d_04g4rD'

    SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL') or (
        os.environ.get('DATABASE_URL') or 
        f"mysql+pymysql://{os.environ.get('DB_USERNAME')}:{os.environ.get('DB_PASSWORD')}"
        f"@{os.environ.get('DB_HOST')}/{os.environ.get('DB_NAME')}"
    )
