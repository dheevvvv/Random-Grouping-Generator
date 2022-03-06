import random

name = list(input("insert name (separated with space) = ").split())
total_group = int(input("Total of Group = "))
group = [""]*total_group

i = 0
while len(name)!=0:
    total_people = len(name)
    selected = random.randint(0, total_people-1)
    group[i] = group[i] + " " + name[selected]
    del name[selected]
    i += 1
    if i == total_group:
        i = 0
    
for i in range(total_group):
    print("group", str(i+1) + ":" + group[i])