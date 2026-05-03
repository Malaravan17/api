from pydantic import BaseModel

class validate(BaseModel):
    name:str
    roll_no:str
    age:int
    cgp:float

class mark_validate(BaseModel):
    roll_no:str
    eng:int
    tam:int
    mat:int
    sci:int