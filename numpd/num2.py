s = "0-0,4-8,20-20,20-23"
res1 = s.split(",")
out = []


for item in res1:
    temp = item.split("-")
    x, y = temp[0], temp[1]
    a, b = int(x), int(y)

    for i in range(a,b+1):
        out.append(i)

print(out)
