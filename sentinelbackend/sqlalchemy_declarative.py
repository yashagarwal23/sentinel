import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Blacklist(Base):
    # sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    __tablename__ = 'blacklist'
    ip = db.Column(db.String, primary_key=True)
    port = db.Column(db.String(6), primary_key=True)

class badIP(Base):
    # sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    __tablename__ = 'badIP'
    ip = db.Column(db.String, primary_key=True)
    count = db.Column(db.Integer)

class scheduledFiles(Base):
    __tablename__ = 'scheduled_files'
    file = db.Column(db.String, primary_key=True)
    hash = db.Column(db.String)
    time = db.Column(db.String)
    user = db.Column(db.String)

class badProcess(Base):
    __tablename__ = 'bad_process'
    PID = db.Column(db.Integer, primary_key=True)
    IP = db.Column(db.String, primary_key=True)
    positives = db.Column(db.Integer)
    totals = db.Column(db.Integer)


engine = create_engine('sqlite:////tmp/test.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine