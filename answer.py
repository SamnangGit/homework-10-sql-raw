import os
from dotenv import load_dotenv
import mysql.connector
from datetime import datetime

load_dotenv()

DB = mysql.connector.connect(
host=os.getenv("DB_HOST"),
db=os.getenv("DB_NAME"),
user=os.getenv("DB_USER"),
password=os.getenv("DB_PASS")
)

cursor = DB.cursor()

# 1. Add new employee record to employee table with id = 168, firstname = 'John', lastname = 'Doe', initials = 'JD', job = 'Programmer', hire_date = today's date.
today = datetime.now()
sql = """
INSERT INTO employee (emp_num, emp_lname, emp_fname, emp_initial, emp_hiredate, job_code) 
VALUES(%s, %s, %s, %s, %s, %s)
"""
value= (168, "Doe", "John", "JD", today, 500)

cursor.execute(sql, value)
DB.commit()
print(cursor.rowcount, "record inserted.")

# 2. Query the new created employee (id=168) from employee table, with information of employee id, firstname, lastname, initials, job description (join with job), charge per hour (join with job) and hire_date.
sql = """
SELECT
    EMP.EMP_NUM,
    EMP.EMP_FNAME,
    EMP.EMP_LNAME,
    EMP.EMP_INITIAL,
    JOB.JOB_DESCRIPTION,
    JOB.JOB_CHG_HOUR,
    EMP.EMP_HIREDATE
FROM
    employee AS EMP
JOIN
    job ON EMP.JOB_CODE = JOB.JOB_CODE
WHERE
    EMP.EMP_NUM = 168
"""

cursor.execute(sql)
employee = cursor.fetchone()

print("Employee: ")
print("ID\tFirst Name\tLast Name\tInitial\tJob Description\tCharge per Hour\tHire Date")
print("-----------------------------------------------------------------------------------------------")
print(employee[0], "\t", employee[1], "\t\t", employee[2], "\t\t", employee[3], "\t", employee[4], "\t\t", employee[5], "\t\t", employee[6].strftime('%d-%B-%Y'))

# 3. Update the new created employee (id=168) job, from 'Programmer' to 'Database Designer'.
sql = """
UPDATE employee
SET job_code = (SELECT job_code FROM job WHERE job_description = 'Database Designer')
WHERE emp_num = 168
"""

cursor.execute(sql)
DB.commit()
print(cursor.rowcount, "record(s) affected")

# 4. Query all project that has "Programmer" assigned to, with information of project id, project name and program manager (join with employee).
sql = """
SELECT
    PROJ.PROJ_NUM,
    PROJ.PROJ_NAME,
    EMP.EMP_FNAME,
    EMP.EMP_LNAME
FROM
    project AS PROJ
JOIN
    `assignment` AS ASS ON PROJ.PROJ_NUM = ASS.PROJ_NUM
JOIN
    employee AS EMP ON ASS.EMP_NUM = EMP.EMP_NUM
JOIN
    job ON EMP.JOB_CODE = JOB.JOB_CODE
WHERE
    JOB.JOB_DESCRIPTION = 'Programmer'
"""

cursor.execute(sql)
projects = cursor.fetchall()
print(projects)

# 5. Delete the new created employee (id=168) from employee table.
sql = "DELETE FROM employee WHERE EMP_NUM = 168"

cursor.execute(sql)
DB.commit()
print(cursor.rowcount, "record(s) affected")