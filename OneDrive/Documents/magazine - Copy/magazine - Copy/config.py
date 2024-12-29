# config.py
import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '9fa1a032524cfff1d5cf3e19259942535a7c68eb3b5eb0df2497a31c51148b0b301d3919b9adaa12d8803cb77702fc170731b7562feec7c01a0b08c0014e4a44'
    
    # MySQL Configuration
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'  # Change this to your MySQL username
    MYSQL_PASSWORD = 'nishant123'  # Change this to your MySQL password
    MYSQL_DB = 'college_magazine'
    
    # MySQL URI for SQLAlchemy
    SQLALCHEMY_DATABASE_URI = f'mysql://root:nishant123@localhost/college_magazine'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # File Upload Configuration
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    
    # Session Configuration
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # mysql+pymysql://root:nishant123@localhost:3306/social_media_app_db