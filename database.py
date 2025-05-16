from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

db =  create_engine(os.getenv("DATABASE_URL"))
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class User(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(255), nullable=False)
  email = Column(String(255), nullable=False, unique=True)
  password = Column(String(255), nullable=False)

  def __init__(self, name, email, password):
    self.name = name
    self.email = email
    self.password = password 

Base.metadata.create_all(bind=db)
