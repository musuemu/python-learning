import sys
while True:
    try:
        num = int(sys.stdin.readline().strip('\n'))
        num_list = sys.stdin.readline().strip('\n').split()
        ave = []
        count = 0
        for i in num_list:
            if int(i) < 0:
                count += 1
            elif int(i) == 0:
                pass                
            else:                
                ave.append(int(i))
        if len(ave) != 0:
            ave = sum(ave)/len(ave)
        print(count, round(ave, 1))
    except:
        break
