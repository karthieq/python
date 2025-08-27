import datetime

class Employee:

    emp_total = 0
    pay_raise = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@xyz.com'

        Employee.emp_total += 1

    def pf(self):
        return int(self.pay * 0.12)

    def apply_raise(self):
        self.pay = int(self.pay * self.pay_raise)

    @classmethod
    def set_pay_raise(cls, amount):
        cls.pay_raise = amount

    @classmethod
    def fromstring(cls, emp_string): # alternate constructor
        first, last, pay = emp_string.split(',')
        return cls(first, last, pay)

    @staticmethod
    def isworkday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


print(Employee.emp_total)
emp1 = Employee('a', 'b', 100)
emp2 = Employee('c', 'd', 200)
print(Employee.emp_total)

Employee.set_pay_raise(1.1)
print(Employee.pay_raise)
print(emp1.pay_raise)
print(emp2.pay_raise)
emp1.apply_raise()
emp2.apply_raise()
print(emp1.pay)
print(emp2.pay)

emp_str1 = 'e,f,300'
emp_str2 = 'g,h,400'

emp = Employee.fromstring(emp_str1)
print(emp.email)
print(emp.emp_total)

date = datetime.datetime.now()
print(Employee.isworkday(date))
