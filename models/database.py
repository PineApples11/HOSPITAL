from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///hospital.db')  # Change to your DB
Session = sessionmaker(bind=engine)
session = Session()
