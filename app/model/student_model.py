from sqlalchemy import Column, String, Integer, DateTime, func

class Student(Base):
    
    __tablename__ = "Students"
    
    id = Column("id", Integer, autoincrement=True)
    first_name = Column(String(225), nullable=False)
    last_name = Column(String(225), nullable=False)
    city = Column(String(225), nullable=False)
    email = Column(String(225), Unique=True, nullable=False)
    phone = Column(Integer, Unique=True, nullable=False)
    dob = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), server_onupdate=func.now())
    
    
    