"""
Create an hierarchy of classes - abstract class Employee and subclasses 
HourlyEmployee, SalariedEmployee, Manager and Executive. 
Every one's pay is calculated differently, research a bit about it. 
After you've established an employee hierarchy, 
create a Company class that allows you to manage the employees. 
You should be able to hire, fire and raise employees.
"""
import random
import string
from abc import ABC, abstractmethod

class Employee(ABC):
    _used_ids = set()

    def __init__(self, name):
        self.name = name
        self.id = self.generate_id()

    @staticmethod
    def generate_id():
        while True:

            digits = ''.join(random.choices(string.digits, k=8))

            id = f"E-{digits}"

            if id not in Employee._used_ids:
                Employee._used_ids.add(id)
                return id

    @abstractmethod
    def calculate_pay(self):
        pass

    @abstractmethod
    def position(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, name, hrs, hrs_rate):
        super().__init__(name)
        self.hours_worked = hrs
        self.hourly_rate = hrs_rate

    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate
    
    def position(self):
        return 'hourly employee'
    
    def __str__(self) -> str:
        return f"Employee ID: {self.id}, Name: {self.name}, Working hrs: {self.hours_worked}, Rate: {self.hourly_rate}, Salary: {self.calculate_pay()}, Position: {self.position()}"
    
class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def calculate_pay(self):
        return self.salary
    
    def position(self):
        return 'salary employee'
    
    def __str__(self) -> str:
        return f"Employee ID: {self.id}, Name: {self.name}, Salary: {self.salary}, Position: {self.position()}"
    
class Manager(Employee):
    def __init__(self, name, salary, initial_bonus=0):
        super().__init__(name)
        self.salary = salary
        self._bonus = initial_bonus

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, bonus_value):
        self._bonus = bonus_value

    def calculate_pay(self):
        return self.salary + self.bonus
    
    def position(self):
        return 'manager employee'
    
    def __str__(self) -> str:
        return f"Employee ID: {self.id}, Name: {self.name}, Salary: {self.calculate_pay()}, Position: {self.position()}"

class Executive(Employee):
    def __init__(self, name, salary, initial_bonus=0, initial_stock_options=0):
        super().__init__(name)
        self.salary = salary
        self._bonus = initial_bonus
        self._stock_options = initial_stock_options

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, bonus_value):
        self._bonus = bonus_value
    
    @property
    def stock_options(self):
        return self._stock_options

    @stock_options.setter
    def stock_options(self, value):
        self._stock_options = value

    def position(self):
        return 'executive employee'
    
    def calculate_pay(self):
        return self.salary + self.bonus + self.stock_options
    
    def __str__(self) -> str:
        return f"Employee ID: {self.id}, Name: {self.name}, Salary: {self.calculate_pay()}, Position: {self.position()}"

class Company:
    
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def hire_employee(self, employee):
        if not isinstance(employee, Employee):
            raise ValueError("Employee must be an instance of the Employee class.")
        self.employees.append(employee)

    def fire_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            raise f"She is not an employee"

    def raise_employee_salary(self, employee_id, amount):
        for employee in self.employees:
            if hasattr(employee, 'id') and employee.id == employee_id:
                if hasattr(employee, 'salary'):
                    employee.salary += amount
                elif hasattr(employee, 'hourly_rate'):
                    employee.hourly_rate += amount
            else:
                print(f"{employee.name} is not an employee of the company.")

    def company_info(self):
        print(self.company_name)
        for emp in self.employees:
            print(f"{emp.__str__()}")

def main():
    hourly_employee = HourlyEmployee("Tom", 40, 15)
    salaried_employee = SalariedEmployee("Jane", 10000)
    salaried_employee1 = SalariedEmployee("Jenny", 20000)
    manager = Manager("Bob", 60000, 10000)
    executive = Executive("Eve", 80000, 20000, 10000)

    comp = Company("Test Company Ltd.")
    comp.hire_employee(hourly_employee)
    comp.hire_employee(salaried_employee)
    comp.hire_employee(manager)
    print(comp.company_info())
    comp.fire_employee(manager)
    comp.raise_employee_salary(salaried_employee.id, 500)
    print(comp.company_info())

    comp1 = Company("Best Test Corp.")
    comp1.hire_employee(executive)
    comp1.hire_employee(salaried_employee)
    comp1.hire_employee(salaried_employee1)
    print(comp1.company_info())
    comp1.fire_employee(salaried_employee)
    print(comp1.company_info())

if __name__ == "__main__":
    main()