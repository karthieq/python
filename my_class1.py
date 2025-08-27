class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@oracle.com'

    def fullname(self):
        return f'{self.first} {self.last}'

e1 = Employee('Karthikeyan', 'Ramanujam', 100)
e2 = Employee('X', 'L', 500)
print(e1.fullname())
print(e2.first)


