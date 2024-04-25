def find_key(dict_input):
    list_key = []
    for i in range(len(list(dict_input.keys()))):
        if list(dict_input.values())[i] == max(list(dict_input.values())):
            list_key.append(list(dict_input.keys())[i])
    return list_key

a = int(input("enter parameter a in mm:"))
h = int(input("enter parameter h in mm:"))
d = int(input("enter parameter d in mm:"))
name = "a%d-h%d-d%d.txt"%(a,h,d)
f = open(name,"r")
rawdata = f.readlines()
linesnum = len(rawdata)
accuracy = dict()
f1score = dict()
calculating = []
for i in range(linesnum):
    if i%4 == 0:
        continue
    elif i%4 == 1:
        nowline = rawdata[i]
        nowline = nowline.split('.')
        nowline = nowline[0:3]
        nowline[0] = nowline[0][2:]
        nowline = [int(i) for i in nowline]
        calculating += nowline
        continue
    elif i%4 == 2:
        nowline = rawdata[i]
        nowline = nowline.split('.')
        nowline = nowline[0:3]
        nowline[0] = nowline[0][2:]
        nowline = [int(i) for i in nowline]
        calculating += nowline
        nowaccuracy = (calculating[0]+calculating[4])/(calculating[0]+calculating[4]+calculating[1]+calculating[3])
        accuracy[(i-2)//4] = nowaccuracy
        p = calculating[0]/(calculating[0]+calculating[3])
        r = calculating[0]/(calculating[0]+calculating[1])
        nowf1score = 2*p*r/(p+r)
        f1score[(i-2)//4] = nowf1score
        continue
    else:
        calculating = []
        continue

accuracylist = find_key(accuracy)
for item1 in accuracylist:
#     print(item1,accuracy[item1])
    print("the highest accuracy is %f"%accuracy[item1])
# f1scorelist = find_key(f1score)
# for item2 in accuracylist:
#     print(item2,f1score[item2])

f.close()
