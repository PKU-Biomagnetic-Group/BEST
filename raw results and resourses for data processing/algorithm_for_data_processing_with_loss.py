def comput_train_loss(train_loss_raw):
    train_loss_splited = train_loss_raw.split(",")
    train_loss_list = []
    for astr in train_loss_splited:
        if astr[0] == "[":
            train_loss_list.append(float(astr[1:]))
        elif astr[-1] == "\n":
            train_loss_list.append(float(astr[:-2]))
        else:
            train_loss_list.append(float(astr))
    train_loss_total = 0
    for i in range(len(train_loss_list)):
        if i == len(train_loss_list)-1:
            train_loss_total += train_loss_list[i]
        else:
            train_loss_total += train_loss_list[i]*3
    train_loss = train_loss_total/16000
    return train_loss

def comput_val_loss(val_loss_raw):
    val_loss_splited = val_loss_raw.split(",")
    val_loss_list = []
    for astr in val_loss_splited:
        if astr[0] == "[":
            val_loss_list.append(float(astr[1:]))
        elif astr[-1] == "\n":
            val_loss_list.append(float(astr[:-2]))
        else:
            val_loss_list.append(float(astr))
    val_loss_total = 0
    for i in range(len(val_loss_list)):
        if i == len(val_loss_list)-1:
            val_loss_total += val_loss_list[i]
        else:
            val_loss_total += val_loss_list[i]*3
    val_loss = val_loss_total/4000
    return val_loss

def cal_accuracy(accuracy_raw_a, accuracy_raw_b):
    calculating=[]
    nowline_a = accuracy_raw_a.split('.')
    nowline_a = nowline_a[0:3]
    nowline_a[0] = nowline_a[0][2:]
    nowline_a = [int(i) for i in nowline_a]
    calculating += nowline_a
    nowline_b = accuracy_raw_b.split('.')
    nowline_b = nowline_b[0:3]
    nowline_b[0] = nowline_b[0][2:]
    nowline_b = [int(i) for i in nowline_b]
    calculating += nowline_b
    nowaccuracy=(calculating[0]+calculating[4])/(calculating[0]+calculating[4]+calculating[1]+calculating[3])
    return nowaccuracy

a = int(input("enter parameter a in mm:"))
h = int(input("enter parameter h in mm:"))
d = int(input("enter parameter d in mm:"))

# for n in range(36):
with open("a%d-h%d-d%d.txt"%(a,h,d), "r") as loss_data:
    data = loss_data.readlines()
    train_loss_summary = []
    valid_loss_summary = []
    accuracy_summary = []
    for i in range(30):
        train_loss_summary.append(comput_train_loss(data[i*6]))
        valid_loss_summary.append(comput_val_loss(data[i*6+1]))
        accuracy_summary.append(cal_accuracy(data[i*6+3], data[i*6+4]))
#        print(train_loss_summary)
#        print(valid_loss_summary)
#        print(accuracy_summary)
#     print(max(accuracy_summary),n)
    print("the highest accuracy is %f"%max(accuracy_summary))
        
import matplotlib.pyplot as plt
import numpy as np

font = {'family':'Times New Roman'  #'serif', 
#         ,'style':'italic'
        ,'weight':'normal'  # 'normal' 
#         ,'color':'red'
        ,'size':20
       }

# 创建画布和子图
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制折线图
x = np.arange(1, 31)  # x轴数据
ax.plot(x, train_loss_summary, label='Train Loss', linewidth=2)
ax.plot(x, valid_loss_summary, label='Valid Loss', linewidth=2)
ax.plot(x, accuracy_summary, label='Accuracy', linewidth=2)

# 添加竖线
max_index = accuracy_summary.index(max(accuracy_summary)) + 1
ax.axvline(x=max_index, linestyle='--', color='red', linewidth=2, label='Best Accuracy')

# 设置轴标签、标题和图例
ax.set_xlabel('Epoch', fontsize=14)
ax.set_ylabel('Loss or Accuracy', fontsize=14)
#ax.set_title('Training and Validation Loss and Accuracy', fontsize=16)
ax.legend(fontsize=12)

# 设置网格线
ax.grid(True, linestyle='--', alpha=0.5)

# 设置坐标轴范围
ax.set_xlim([1, 30])
ax.set_ylim([0.1, 1])

# 调整坐标轴刻度文字大小
ax.tick_params(labelsize=12)

# 显示图形
plt.show()
        

