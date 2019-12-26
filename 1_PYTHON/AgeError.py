class AgeError(Exception):
    """
        自定义异常类，年龄错误
    """
    def __init__(self,message,age_value,code_line,error_number):
        # super().__init__(message)
        self.message = message
        self.age_value = age_value
        self.code_line = code_line
        self.error_number = error_number


class Wife:
    def __init__(self,age):
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if 21<= value <=31:
            self.__age = value
        else:
            # raise ValueError("我不要")
            raise AgeError("超过我想要的范围啦",value,26,1001)

# wife = Wife(81)
try:
    wife = Wife(81)
except AgeError as e:
    print(e.message)
    print(e.age_value)
    print(e.code_line)
    print(e.error_number)