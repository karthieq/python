class Employee:

    emp_total = 0
    pay_raise = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.name = first + ' ' + last
        self.email = first + '.' + last + '@xyz.com'

        Employee.emp_total += 1

    def pf(self):
        return int(self.pay * 0.12)

    def apply_raise(self):
        self.pay = int(self.pay * self.pay_raise)


class Developer(Employee):

    pay_raise = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def show_employee(self):
        for emp in self.employees:
            print('-->', emp.name)


dev1 = Developer('Karthikeyan', 'R', 500, 'python')
dev2 = Developer('Karthik', 'R', 100, 'java')

mgr1 = Manager('x', 'y', 500, [dev1])
mgr1.add_employee(dev2)
print(mgr1.email)
mgr1.show_employee()
mgr1.remove_employee(dev2)
mgr1.show_employee()

print(isinstance(mgr1, Employee))
print(isinstance(mgr1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
