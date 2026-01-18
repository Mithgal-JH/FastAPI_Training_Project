from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHAMY_DATABASE = "sqlite:///./blog.db"
connect_args = {"check_same_thread": False}

engine = create_engine(SQLALCHAMY_DATABASE, connect_args=connect_args)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

base = declarative_base()
