class BaseDamageError(Exception):
    """
        自定义异常类，基础攻击力错误
    """
    def __init__(self,message,base_damage_value,code_line,error_number):
        # super().__init__(message)
        self.message = message
        self.base_damage_value = base_damage_value
        self.code_line = code_line
        self.error_number = error_number


class Enemy:
    def __init__(self,base_damage):
        self.base_damage = base_damage
    @property
    def base_damage(self):
        return self.__base_damage
    @base_damage.setter
    def base_damage(self,value):
        if 0<= value <=100:
            self.__base_damage = value
        else:
            # raise ValueError("我不要")
            raise BaseDamageError("超过基础攻击力范围啦",value,26,1001)

# wife = Wife(81)
try:
    enemy = Enemy(200)
except BaseDamageError as e:
    print(e.message)
    print(e.base_damage_value)
    print(e.code_line)
    print(e.error_number)