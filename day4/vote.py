while True:
    try:
        pnum = int(input())
        names = input().strip().split()
        vnum = int(input())
        vote = input().strip().split()
        result ={}
        for name in names:
            result[name] = 0
        invaild = []
        for name in vote:
            if name in names:
                result[name] += 1
            else:
                invaild.append(name)
        for name in names:
            print('%s : %d' %(name,result[name]))
        print('Invalid : %d' %(len(invaild)))  
    except:
        break
