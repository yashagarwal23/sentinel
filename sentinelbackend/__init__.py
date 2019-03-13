# from flask import Flask
# app = Flask(__name__)
# from flask_sqlalchemy import SQLAlchemy
# import os
# if os.name == "nt":
#   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////static/test.db'
# else:
#   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)

# import sqlachemy as db
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
#
# Base = declarative_base()
# engine = create_engine('sqlite:////tmp/test.db')
# Base.metadata.create_all(engine)

from sentinelbackend import routes, schedulers
from sentinelbackend.models import addToBlacklist
from sentinelbackend import sqlalchemy_declarative
