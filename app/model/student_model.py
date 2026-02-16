from sqlalchemy import Column, String, Integer, DateTime

class Student:
    id = Column("id", Integer, autoincrement=True)
    first_name = Column(String(225), nullable=False)
    last_name = Column(String(225), nullable=False)
    city = Column(String(225), nullable=False)
    email = Column(String(225), nullable=False)
    phone = Column(Integer, nullable=False)
    dob = Column(DateTime, nullable=False)
    
    
    