from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "iyfmq0j007i"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:[password]@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'register'

# file upload constraints
app.config['PROFILE_PIC_FOLDER'] = 'app/static/profile_pic'
app.config['ALLOWED_PROFILE_PIC_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

app.config.from_object(__name__)
from app import views
