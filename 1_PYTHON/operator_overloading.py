class Vector:
    """
        随心所欲
    """
    def __init__(self,x):
        self.x = x

    def __str__(self):
        """
            打印实例变量
        :return: 实例变量
        """
        return "%d"%self.x

    # def __add__(self, other):
    #     return Vector(self.x + other)

    def __sub__(self, other):
        return Vector(self.x - other)

    def __mul__(self, other):
        return Vector(self.x * other)

    def __truediv__(self, other):
        return Vector(self.x / other)

    def __floordiv__(self, other):
        return Vector(self.x // other)

    def __mod__(self, other):
        return Vector(self.x % other)

    def __pow__(self, other):
        return Vector(self.x ** other)


    def __radd__(self, other):
        return Vector(self.x + other)

    def __rsub__(self, other):
        return Vector(self.x - other)

    def __rmul__(self, other):
        return Vector(self.x * other)

    def __rtruediv__(self, other):
        return Vector(self.x / other)

    def __rfloordiv__(self, other):
        return Vector(self.x // other)

    def __rmod__(self, other):
        return Vector(self.x % other)

    def __rpow__(self, other):
        return Vector(self.x ** other)


    def __iadd__(self, other):
        self.x += other
        return self

    def __isub__(self, other):
        self.x -= other
        return self

    def __imul__(self, other):
        self.x *= other
        return self

    def __itruediv__(self, other):
        self.x /= other
        return self

    def __ifloordiv__(self, other):
        self.x //= other
        return self

    def __imod__(self, other):
        self.x %= other
        return self

    def __ipow__(self, other):
        self.x **= other
        return self


    def __lt__(self, other):
        if self.x < other:
            return True
        else:
            return False

    def __le__(self, other):
        if self.x <= other:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.x > other:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.x >= other:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.x == other:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.x != other:
            return True
        else:
            return False

    # 发散思维
    def __add__(self, other):
        return Vector(self.x + other.x)

if __name__ == "__main__":
    vector = Vector(10)
    vector1 = Vector(100)
    vector2 = Vector(200)

    print(vector)
    print(vector1)
    print(vector2)

    # 发散思维
    print(vector + vector1)
    print(vector + vector2)

    print("+ - * / // % **")

    # print(vector + 5)
    print(vector - 5)
    print(vector * 5)
    print(vector / 5)
    print(vector // 5)
    print(vector % 5)
    print(vector ** 5)

    print("+ - * / // % **")

    print(5 + vector)
    print(5 - vector)
    print(5 * vector)
    print(5 / vector)
    print(5 // vector)
    print(5 % vector)
    print(5 ** vector)

    print("+ - * / // % **")

    vector += 5
    print(vector)
    vector -= 5
    print(vector)
    vector *= 5
    print(vector)
    vector /= 5
    print(vector)
    vector //= 5
    print(vector)
    vector %= 5
    print(vector)
    vector **= 5
    print(vector)

    print("+ - * / // % **")

    print(vector < 5)
    print(vector <= 5)
    print(vector > 5)
    print(vector >= 5)
    print(vector == 5)
    print(vector != 5)












