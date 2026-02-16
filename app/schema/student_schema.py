from pydantic import BaseModel, Field, EmailStr
from datetime import date

class StudentCreate(BaseModel):
    """Student BaseModel to create a student

    Args:
        BaseModel (_type_): _description_
    """
    first_name: str = Field(description="Enter first name of student")
    last_name: str = Field(description="Enter last name of student")
    city: str = Field(description="Enter your city name")
    email: EmailStr = Field(description="Enter your email address")
    phone: int = Field(description="Enter your phone number", ge=0, le= 10)
    dob: date = Field(description="Enter your date of birth")


