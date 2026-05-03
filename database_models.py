from sqlalchemy import Column,Integer,Float,String,ForeignKey
from sqlalchemy.orm import declarative_base,relationship

Base=declarative_base()

class Table(Base):
    __tablename__ = "students_table"

    name=Column(String)
    roll_no=Column(String,primary_key=True,index=True)
    age=Column(Integer)
    cgp=Column(Float)

    mark=relationship("Marks_Table",back_populates="student")

class Marks_Table(Base):
    __tablename__="marks_table"

    id = Column(Integer, primary_key=True, index=True)
    roll_no=Column(String,ForeignKey("students_table.roll_no"))
    eng=Column(Integer)
    tam=Column(Integer)
    mat=Column(Integer)
    sci=Column(Integer)

    student=relationship("Table",back_populates="mark")