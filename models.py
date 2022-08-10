from datetime import datetime

from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Date, DateTime


class Item(Base):
    __tablename__ = 'uidai'
    aadhar = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    guardian = Column(String(255), nullable=False, unique=True)
    dob = Column(Date)
    gender = Column(String(32))
    address=Column(String(255))
    status = Column(Integer)

    def __repr__(self):
        return f"<Item name={self.name} address={self.address}>"
