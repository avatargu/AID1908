
# dir()

_map_data = [
    # [2, 0, 2, 0],
    # [0, 0, 4, 4],
    # [0, 0, 8, 0],
    # [0, 2, 8, 0]
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]



def _left_move_number(line):
    for _ in range(3):
        for i in range(3):
            if line[i] == 0:
                line[i] = line[i + 1]
                line[i + 1] = 0

def _left_merge_number(line):
    for i in range(3):
        if line[i] == line[i + 1]:
            line[i] *= 2
            line[i + 1] = 0







def test():
    L = [2,0,2,8]
    _left_move_number(L)
    _left_merge_number(L)
    _left_move_number(L)
    print(L)


# test()

def _left_move_aline(line):
    _left_move_number(line)
    _left_merge_number(line)
    _left_move_number(line)






def left():
    for line in _map_data:
        _left_move_aline(line)

def right():
    for line in  _map_data:
        line.reverse()
        _left_move_aline(line)
        line.reverse()

def up():
    for col in range(4):
        line = [0,0,0,0]
        for row in range(4):
            line[row] = _map_data[row][col]
        _left_move_aline(line)
        for row in range(4):
            _map_data[row][col] = line[row]

def down():
    _map_data.reverse()
    up()
    _map_data.reverse()





def get_space_count():
    count = 0
    for r in _map_data:
        count += r.count(0)
    return count




def fill2():
    blanks = get_space_count()
    if 0 == blanks:
        return
    import random
    pos = random.randrange(blanks)
    offset = 0
    for line in _map_data:
        for col in range(4):
            if line[col] == 0:
                if offset != pos:
                    offset += 1
                    continue
                else:
                    line[col] = 2
                    return



def show_map():
    for line in _map_data:
        print("[ %4d %4d %4d %4d     ]" % (line[0],line[1],line[2],line[3]))





def main():
    while True:
        fill2()
        fill2()
        show_map()
        s = input("请输入方向（q退出）：")
        if s == "q":
            break
        elif s == "a":
            left()
            fill2()
        elif s == "d":
            right()
            fill2()
        elif s == "w":
            up()
            fill2()
        elif s == "s":
            down()
            fill2()
        # show_map()
main()







