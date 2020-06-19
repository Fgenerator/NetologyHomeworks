from application.salary import calculate_salary
from application.people import get_employee
import datetime

if __name__ == '__main__':
    print(datetime.datetime.now())
    calculate_salary()
    get_employee()