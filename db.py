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

'''
Query all employee records from the employee table
And query employee with condition, emp_num > 101
'''

cursor.execute("SELECT * FROM employee")
employees = cursor.fetchall()

# print(employees)

# datetime.str

# for employee in employees:
#     print(employee[0], employee[1], employee[2], employee[3], employee[4].strftime('%d-%B-%Y'))

# date time conversion format
# https://www.w3schools.com/python/python_datetime.asp#:~:text=A%20reference%20of%20all%20the%20legal%20format%20codes%3A

# cursor.execute("SELECT * FROM employee WHERE emp_num > 101")
# employees_condition = cursor.fetchall()

# for employee in employees_condition:
#     print(employee[0], employee[1], employee[2], employee[3], employee[4].strftime('%d-%B-%Y'))

'''
Join employee with job and select emp_num, emp_lname, emp_fname, emp_initial, emp_hiredate, job_description
'''

# cursor.execute("SELECT * FROM employee INNER JOIN job ON employee.job_code = job.job_code")
# employees = cursor.fetchall()
# for employee in employees:
#     print(employee[0], employee[1], employee[2], employee[3], employee[4].strftime('%d-%B-%Y'), employee[9])

# OR

# cursor.execute('''SELECT 
#                em.emp_num, em.emp_lname, em.emp_fname, em.emp_initial, em.emp_hiredate, job.job_description  
#                FROM employee as em INNER JOIN job ON em.job_code = job.job_code''')

# employees = cursor.fetchall()
# for employee in employees:
#     print(employee[0], employee[1], employee[2], employee[3], employee[4].strftime('%d-%B-%Y'), employee[5])

'''
Insert new employee record, emp_num = 999, emp_lname = Doe, emp_fname = John, emp_initial = D, emp_hiredate = current date
'''

today = datetime.now()
sql = 'INSERT INTO employee (emp_num, emp_lname, emp_fname, emp_initial, emp_hiredate) VALUES (%s, %s, %s, %s, %s)'
value = (999, 'Doe', 'John', 'D', today)

cursor.execute(sql, value)

DB.commit()
print(cursor.rowcount, "record inserted.")


'''
Update employee record, job_code = 510 where emp_num = 999
'''
sql = 'UPDATE employee SET job_code = %s WHERE emp_num = %s'
value = (510, 999)

cursor.execute(sql, value)

DB.commit()




'''
Delete employee record, emp_num = 999
'''
sql = 'DELETE FROM employee WHERE emp_num = %s'
value = (999, )

cursor.execute(sql, value)

DB.commit()



'''
Query assigment where assign_date is larger than 2010-01-01
'''
sql = 'SELECT * FROM assignment WHERE assign_date > %s'
value = ('2010-01-01', )

cursor.execute(sql, value)
assignments = cursor.fetchall()

for assignment in assignments:
    print(assignment[0], assignment[1], assignment[2], assignment[3].strftime('%d-%B-%Y'), assignment[4].strftime('%d-%B-%Y'))

    

