from fastapi import FastAPI, HTTPException
from models import Employee
from typing import List


employees_db: List[Employee] = []

app = FastAPI()

@app.get("/employees", response_model=List[Employee])
def get_employees():
    return employees_db


@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    for index,emp in enumerate(employees_db):
        if emp.id == emp_id:
            return employees_db[index]
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employees", response_model=Employee)
def add_employee(new_emp: Employee):
    for emp in employees_db:
        if emp.id == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")
    employees_db.append(new_emp)
    return new_emp

@app.put("/update_employee/{emp_id}", response_model=Employee)
def update_employee(emp_id: int, updated_employee: Employee):
    for index, emp in enumerate(employees_db):
        if emp.id == emp_id:
            employees_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/delete_employee/{emp_id}")
def delete_employee(emp_id: int):
    for index, emp in enumerate(employees_db):
        if emp.id == emp_id:
            del employees_db[index]
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")