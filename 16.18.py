from collections import OrderedDict

def pattern_matching(p, v):
    lp = len(p)
    lv = len(v)
    d = OrderedDict()

    for e in p:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1

    al = 1
    while al < lv:
        x = lv - (d['a'] * al) 
        if x % d['b'] != 0:
            al += 1
            continue
        bl = x // d['b']
        temp = v[:]
        td = OrderedDict()
        for elem in p:
            if len(td) > 2:
                break
            if elem == 'a':
                c = ''.join(temp[:al])
                if c not in td:
                    td[c] = 1
                else:
                    td[c] += 1
                temp = temp[al:]
            else:
                c = ''.join(temp[:bl])
                if c not in td:
                    td[c] = 1
                else:
                    td[c] += 1
                temp = temp[bl:]
        
        dvals = list(d.values())
        tdvals = list(td.values())

        flag = True
        for i in range(len(dvals)):
            if dvals[i] != tdvals[i]:
                flag = False
                break
        if flag:
            return True

        al += 1
    
    return False

pattern = 'bab'
value = 'amitshwetaamit'
res = pattern_matching(pattern, value)
print(len(value))
print(res)