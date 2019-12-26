class EmployeeManager:
    def __init__(self):
        self.__employee_list = []

    @property
    def employee_list(self):
        return self.__employee_list

    def add_employee(self,employee_new):
        if isinstance(employee_new,Employee):
            self.employee_list.append(employee_new)
        else:
            raise ValueError("类型错误")

    def remove_employee(self,employee_target):
        if isinstance(employee_target,Employee):
            self.employee_list.remove(employee_target)
        else:
            raise ValueError("类型错误")

    def calculate_total_salary(self):
        total_salary = 0
        for item in self.employee_list:
            total_salary += item.get_salary()
        return total_salary

    def __iter__(self):
        return EmployeeIterator(self.__employee_list)


class Employee:
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def base_salary(self):
        return self.__base_salary

    @base_salary.setter
    def base_salary(self,base_salary):
        if base_salary > 0:
            self.__base_salary = base_salary
        else:
            raise ValueError("数值错误")

    def get_salary(self):
        # raise NotImplementedError("子类没有重写")
        return self.base_salary


class EmployeeIterator:
    def __init__(self,target):
        self.__target = target
        self.__index = 0
    def __next__(self):
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp
# -------------------------------------------------------------------


class Programmer(Employee):
    def __init__(self,name,base_salary,project_dividend):
        super().__init__(name,base_salary)
        self.project_dividend = project_dividend

    @property
    def project_dividend(self):
        return self.__project_dividend

    @project_dividend.setter
    def project_dividend(self,project_dividend):
        if project_dividend > 0:
            self.__project_dividend = project_dividend
        else:
            raise ValueError("数值错误")

    def get_salary(self):
        return super().get_salary() + self.project_dividend #　扩展重写


class Salesperson(Employee):
    def __init__(self, name, base_salary, sales_volume):
        super().__init__(name, base_salary)
        self.sales_volume = sales_volume

    @property
    def sales_volume(self):
        return self.__sales_volume

    @sales_volume.setter
    def sales_volume(self, sales_volume):
        if sales_volume > 0:
            self.__sales_volume = sales_volume
        else:
            raise ValueError("数值错误")

    def get_salary(self):
        return self.base_salary + self.sales_volume * 0.05

employee_manager = EmployeeManager()
programmer = Programmer("孙悟空",10000,108000)
sales_person = Salesperson("猪八戒",8000,80000)
employee_manager.add_employee(programmer)
employee_manager.add_employee(sales_person)
# print(employee_manager.calculate_total_salary())

# for item in employee_manager:
#     print(item)
iterator = employee_manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break





















































