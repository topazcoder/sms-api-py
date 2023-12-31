from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    Date,
    Boolean,
)
from sqlalchemy.orm import relationship
from sqlalchemy.types import BigInteger
from app.db.base_class import Base


class Student(Base):
    id = Column(BigInteger, primary_key=True)
    first_name = Column(String, nullable=False)
    father_name = Column(String, nullable=False)
    gfather_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(Boolean, default=True, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    guardian_phone_no = Column(String, nullable=False)
    nationality_id = Column(ForeignKey('nationalities.id'), nullable=False)

    registrations = relationship('Registration', back_populates='student')
    nationality = relationship('Nationality', back_populates='students')