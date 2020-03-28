#method 1
line = []
result = []
while True:
    tmp = input()
    if tmp == '':
        break
    for i in tmp.split('\n'):
        line.append(tmp)


def fun1(string):
    count = []
    new = ''
    for a in string:
        count.append(string.count(a))
    m = min(count)
    for a in string:
        if string.count(a) != m:
            new = new + a
    return new


for i in line:
    temp = fun1(i)
    result.append(temp)

print(result)


#method2-->better than method1

while True:
    try:
        a=input()
        b=[]
        for i in a:
            b.append(a.count(i))
        c=[]
        d=min(b)
        for i,j in zip(a,range(len(b))):
            if b[j]!=d:
                c.append(i)
        print(''.join(c))
    except:
        break



