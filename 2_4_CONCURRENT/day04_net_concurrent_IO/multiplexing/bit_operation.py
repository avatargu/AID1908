"""
位运算
"""
class Cat:
    def __init__(self):
        self.a = True
        self.b = True
        self.c = True
        self.d = True

class Tiger:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 4
        self.d = 8
        self.attr = 15

if __name__ == "__main__":
    cat = Cat()
    cat.a = False
    cat.c = False

    tiger = Tiger()
    tiger.attr = 10

    tiger.attr = tiger.attr | tiger.a

    if tiger.attr & tiger.c:
        pass
