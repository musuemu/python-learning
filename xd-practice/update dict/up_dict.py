d = {1: "one"}
d1 = {2: "two", 3: "three"}
d.update(d1)
d2 = {3: "三"}
d.update(d2)
d3= {4: "s"}
d.update(d3)
d[1] = "yi"
print(d)

#Result:
{1: 'yi', 2: 'two', 3: '三', 4: 's'}
