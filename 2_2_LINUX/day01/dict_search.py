word = input("Please enter the word:")
f = open("dict.txt", "r")
for line in f:
    w = line.split()[0]
    if w > word:
        print("Not found")
        break
    elif w == word:
        print(line)
        break
else:
    print("Not found")
f.close()