from sqlalchemy.orm import sessionmaker
from database_models import Table,Base,Marks_Table
from schemas import validate,mark_validate
from fastapi import Depends,APIRouter
from models import start_db


router=APIRouter()

@router.get("/info")
def get_info(roll_no:str,db=Depends(start_db)):
    person=db.query(Table).filter(Table.roll_no==roll_no).first()

    if person is None:
        return "No details found"
    else:
        return person

@router.get("/mark")
def get_marks(roll_no:str,db=Depends(start_db)):
    student=db.query(Table).filter(Table.roll_no==roll_no).first()
    result=[]
    for m in student.mark:
       result.append(m.eng)
    return result



@router.post("/info")
def add_info(add_detail:validate,db=Depends(start_db)):
 try:
    new_record=Table(name=add_detail.name,
                roll_no=add_detail.roll_no,
                age=add_detail.age,
                cgp=add_detail.cgp
                )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return "details added"
 except:
    db.rollback()

@router.post("/mark")
def add_marks(add_marks:mark_validate,db=Depends(start_db)):
    try:
      new_mark=Marks_Table(roll_no=add_marks.roll_no,
                           eng=add_marks.eng,
                           tam=add_marks.tam,
                           mat=add_marks.mat,
                           sci=add_marks.sci)
      db.add(new_mark)
      db.commit()
      db.refresh(new_mark)
      return "mark added"
    except:
       db.rollback()
