word = input()
word_split = word.split(" ")
a = word_split[0]
b = word_split[1]
result = []
for i in range(0,2):
    for j in range(0,2):
        result.append(a[i]+b[j])

child = []
for k in result:
    if k == "AO" or k == "AA" or k == "OA":
        child.append("A")
    elif k == "BO" or k == "BB" or k == "OB":
        child.append("B")
    elif k == "AB" or k == "BA":
        child.append("AB")
    elif k == "OO":
        child.append("O")
        
child_tmp = list(set(child))
child_tmp.sort()

for l in child_tmp:
    print(l, end=" ")
