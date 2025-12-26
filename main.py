from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.db import get_connection
import mysql.connector

app = FastAPI(title="Employee API")

# Pydantic model for request validation
class Employee(BaseModel):
    emp_name: str
    emp_email: str
    salary: int

@app.get("/")
def health():
    return {"status": "API running"}

# CREATE
@app.post("/employees", status_code=201)
def create_employee(employee: Employee):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO employees (emp_name, emp_email, salary) VALUES (%s, %s, %s)",
            (employee.emp_name, employee.emp_email, employee.salary)
        )
        conn.commit()
        return {"message": "Employee created"}
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

# READ ALL
@app.get("/employees")
def get_employees():
    try:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM employees")
        return cur.fetchall()
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

# READ ONE
@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM employees WHERE emp_id=%s", (emp_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Employee not found")

    return row

# UPDATE
@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, employee: Employee):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE employees SET emp_name=%s, emp_email=%s, salary=%s WHERE emp_id=%s",
        (employee.emp_name, employee.emp_email, employee.salary, emp_id)
    )
    conn.commit()

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Employee not found")

    cur.close()
    conn.close()
    return {"message": "Employee updated"}

# DELETE
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM employees WHERE emp_id=%s", (emp_id,))
    conn.commit()

    if cur.rowcount == 0:
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Employee not found")

    cur.close()
    conn.close()
    return {"message": "Employee deleted"}
