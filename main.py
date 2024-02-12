main.py

import datetime as dt
from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    print(f'Today is {dt.date.today()}')
    calculate_salary()
    get_employees()