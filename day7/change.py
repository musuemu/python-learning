while True:
    try:
        rmb = input().split('.')
        num = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
        inter = ['元', '拾', '佰', '仟', '万', '拾', '佰', '仟', '亿', '拾', '佰', '仟', '亿']
        dc = ['角', '分']
        result = '人民币'
        a = rmb[0]
        b = rmb[1]
        tmp = tmp2 = sep = ''
        m = n = 0
        a = a[::-1]
        if int(a) != 0:
            for i in a:
                tmp = num[int(i)] + inter[m] + tmp
                m += 1
            if tmp[0] == '壹':
                if tmp[1] == '拾':
                    tmp = tmp [1::]
        if b == '00':
            tmp2 = '整'
        else:
            for i in b:
                if int(i) != 0:
                    tmp2 = tmp2 + num[int(i)] + dc[n]
                    n += 1
                else:
                    n += 1
        result = result + tmp + tmp2
        print(result)
    except:
        break






