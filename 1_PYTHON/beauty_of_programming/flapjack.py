from random import randint

list_flapjack = []
while len(list_flapjack) < 10:
    random_diameter = randint(1,100)
    if random_diameter not in list_flapjack:
        list_flapjack.append(random_diameter)
print(list_flapjack)

def turn_largest_to_bottom(list_flapjack):
    largest_flapjack = max(list_flapjack)
    list_flapjack_upper = list_flapjack[:list_flapjack.index(largest_flapjack) + 1]
    list_flapjack_lower = list_flapjack[list_flapjack.index(largest_flapjack) + 1:]
    list_flapjack_lower.reverse()
    return list_flapjack_lower + list_flapjack_upper

def sort_flapjack(list_flapjack):
    list_sorted = []
    while len(list_flapjack) > 0:
        list_flapjack = turn_largest_to_bottom(list_flapjack)
        list_sorted.insert(0,list_flapjack.pop())
    return list_sorted

print(sort_flapjack(list_flapjack))
