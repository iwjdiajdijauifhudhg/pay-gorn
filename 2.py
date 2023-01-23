def res(i):
    summ = int(i.split()[3]) + int(i.split()[4])
    return summ

f = open('mat_dv.txt', 'r')
max8 = ['', '', 0]
max9 = ['', '', 0]
max10 = ['', '', 0]
max11 = ['', '', 0]

for i in f :
    if int(i.split()[2]) == 8:
        if res(i) > max8[2] :
            max8[0] = i.split()[0]
            max8[1] = i.split()[1]
            max8[2] = res(i)
    print(max8)
    if int(i.split()[2]) == 9:
        if res(i) > max9[2] :
            max9[0] = i.split()[0]
            max9[1] = i.split()[1]
            max9[2] = res(i)
    print(max9)
    if int(i.split()[2]) == 10:
        if res(i) > max10[2] :
            max10[0] = i.split()[0]
            max10[1] = i.split()[1]
            max10[2] = res(i)
    print(max10)
    if int(i.split()[2]) == 11:
        if res(i) > max11[2] :
            max11[0] = i.split()[0]
            max11[1] = i.split()[1]
            max11[2] = res(i)
    print(max11)
