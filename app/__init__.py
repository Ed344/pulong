from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)
app.config.from_object(Config)
bootstrap=Bootstrap(app) #11.3 Intiate Bootstrap at the start to parallel frontend development with backend
db=SQLAlchemy(app)
migrate=Migrate(app,db)



from app import routes,models