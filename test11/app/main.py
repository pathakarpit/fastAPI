from fastapi import FastAPI
from pydantic import BaseModel
from app.logic import is_eligible_for_loan

app = FastAPI()

class Applicant(BaseModel):
    income: float
    ag: int
    employment_status: str

@app.post('/loan-eligibility')
def check_eligibility(applicant: Applicant):
    if (income>=50000) and (age>=21) and (employment_status =='employed'):
        return {'eligible':True}
    else:
        return {'eligible':False}