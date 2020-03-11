#method 1:use python2
while True:
    try:
        strShort = raw_input()
        strLong = raw_input()
        num = 0
        for s in strShort:
            if s in strLong:
                num += 1
        if num == len(strShort):
            print('true')
        else:
            print('false')
    except:
        break

# method 2: use python3
while True:
    try:
        a,b=set(input()),set(input())
        print ("true" if a&b==a else "false")
    except:
        break
