class Employee:
    def __init__(self, name: str, salary: int):
        self.__name = name
        self.__salary = salary
        self.__bonus = 0

    @property
    def name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus):
        self.__bonus = bonus

    def to_pay(self):
        return self.__salary + self.__bonus


class SalesPerson(Employee):
    def __init__(self, name, salary, percent):
        super().__init__(name, salary)
        self.__percent = percent

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus):
        if self.__percent > 200:
            self.__bonus = bonus * 3
        elif self.__percent > 100:
            self.__bonus = bonus * 2
        else:
            self.__bonus = bonus


class Manager(Employee):
    def __init__(self, name, salary, client_number):
        super().__init__(name, salary)
        self.__client_number = client_number

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, bonus):
        if self.__client_number > 150:
            self.__bonus = bonus + 1000
        elif self.__client_number > 100:
            self.__bonus = bonus + 500
        else:
            self.__bonus = bonus


class Company:
    def __init__(self, employees, n):
        self.employees = employees

    def give_everybody_bonus(self, bonus):
        for employee in self.employees:
            employee.bonus = bonus

    def total_to_pay(self):
        total = 0
        for employee in self.employees:
            total += employee.to_pay()
        return total

    def name_max_salary(self):
        max_salary = self.employees[0]
        for employee in self.employees:
            if employee.to_pay() > max_salary.to_pay():
                max_salary = employee
        return max_salary.name
