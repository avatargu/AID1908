import random as r
list01 = [item for item in range(1,11)]

print(r.random())
print(r.randint(1,3))
print(r.randrange(1,3,2))
print(r.choice(list01))
r.shuffle(list01);print(list01)



