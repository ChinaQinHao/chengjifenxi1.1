# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import filedialog
import tkinter
import xlrd
from matplotlib import font_manager
from pylab import *
import os
import webbrowser as web
from tkinter import *


plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False  # 解决中文显示问题

data_col_history = []
data_row_history = []
读取数量 = 0
读取次数 = 0
def 弹出读取次数():
    window = tk.Tk()

    window.title("读取文件")
    window.geometry("500x300")

    bt = tkinter.Label(window, text="输入分析次数")
    bt.pack()
    e = tk.Entry(window)
    e.pack()


    def get():
        global 读取次数
        读取次数 =int( e.get())
        window.destroy()

    b = tk.Button(window, text="确定", command=get)
    b.pack()

    window.mainloop()
def 读取(name):
    work_book = xlrd.open_workbook(name)
    sheet_1 = work_book.sheet_by_index(0)
    global data_col_history
    global 读取数量
    global data_row_history

    data_col_history.append([sheet_1.col_values(i) for i in range(sheet_1.ncols)])
    data_row_history.append([sheet_1.row_values(i) for i in range(sheet_1.ncols)])
    读取数量 = 读取数量 + 1

def 打开文件资源管理器():
    qh = tk.Tk()
    # qh.withdraw()
    global f_path
    f_path = filedialog.askopenfilename()
    qh.destroy()
    return ('{}'.format(f_path))


my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

弹出读取次数()
第一次读取 = 打开文件资源管理器()
读取(第一次读取)

for i in range(读取次数-1):
    读取(打开文件资源管理器())

work_book = xlrd.open_workbook(第一次读取)  # 读取成绩单
sheet_1 = work_book.sheet_by_index(0)


# x_axis_data = []
# y_axis_data = []


def 保存分段与个人对比():

    # 输入统计数据
    科目名称 = list(科目name)[:-1]
    分段成绩 = 各科分段平均分[:-1]#最后一项是总分！不取最后
    个人成绩 = 个人各科成绩[:-1]

    bar_width = 0.4  # 条形宽度
    index_male = np.arange(len(科目名称))  # 分段条形图的横坐标
    index_female = index_male + bar_width  # 个人条形图的横坐标

    # 使用两次 bar 函数画出两组条形图
    plt.bar(index_male, height=分段成绩, width=bar_width, color='springgreen', label='分段平均成绩')
    plt.bar(index_female, height=个人成绩, width=bar_width, color='dodgerblue', label='你的成绩')

    plt.legend()  # 显示图例
    plt.xticks(index_male + bar_width / 2, 科目名称)  # 让横坐标轴刻度显示
    plt.ylabel('分数')  # 纵坐标轴标题
    plt.title('第{0}分段平均成绩与你的成绩对比'.format(所处分段))  # 图形标题

    plt.savefig('{0}/0各科成绩对比.jpg'.format(username))  # 保存图片
    plt.close()


def 各科全班与分段对比():
    科目名称 = list(科目name)
    分段成绩 = 各科分段平均分
    全班成绩 = 各科全班平均分
    个人成绩 = 个人各科成绩
    waters = ('分段平均', '全班平均', '你的成绩')
    颜色 = ['orange', 'cornflowerblue', 'limegreen']

    for i in range(科目数量):
        buy_number = [分段成绩[i], 全班成绩[i], 个人成绩[i]]
        plt.bar(waters, buy_number, color=颜色)
        plt.title('{0}成绩的对比图'.format(科目名称[i]))

        plt.text(1, 全班成绩[i] + 0.5, int(全班成绩[i]))  # 添加具体成绩标签
        plt.text(0, 分段成绩[i] + 0.5, int(分段成绩[i]))
        plt.text(2, 个人成绩[i] + 0.5, int(个人成绩[i]))
        plt.savefig('{0}/{1}成绩对比.jpg'.format(username, 科目名称[i]))  # 保存图片
        plt.close()


# 创建文件夹
def 创建文件夹(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径

        print("---  创建文件夹成功  ---")
        print('正在保存您的成绩，请稍后')

    else:
        print("---  文件夹被创建过了！  ---")
        print('正在保存您的成绩，请稍后')


def 饼状图():
    for i in range(科目数量):
        # 饼状图占比
        fraces = [len(allname) - 个人各科成绩排名[i], 个人各科成绩排名[i]]
        # 设置显示方式为标准圆
        plt.axes(aspect=1)
        # 设置两个数据得文字说明
        plt.pie(x=fraces, autopct='%3.1f%%', labels=['您超过的', '全班人数'])
        # 显示上部文字说明
        plt.title(科目name[i] + '超过全班')
        # 设置图片
        photo = '{1}/{0}全班.jpg'.format(科目name[i], username)
        plt.savefig(photo)  # 保存图片
        # plt.show()
        plt.close()


def 折线图():
    各科成绩 = []

    各科历次成绩 = []
    各科历次成绩字典 = []
    for j in range(len(data_col_history)):
        位置 = data_col_history[j][0].index(username)
        try:
            for i in range(len(data_col_history[j]) - 1):
                各科成绩.append(data_col_history[j][i + 1][位置])
            各科历次成绩.append(各科成绩)
            各科历次成绩字典.append(dict(zip(data_row_history[j][0][1:], 各科成绩)))
            各科成绩 = []
        except IndexError:
            print("科目数量再历次成绩中不对应")
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 添加这条可以让图形显示中文
    历次科目名称 = []
    历次成绩 = []
    for i in range(len(各科历次成绩字典)):
        历次科目名称.append(list(各科历次成绩字典[i].keys()))
        历次成绩.append(list(各科历次成绩字典[i].values()))
    global 输出科目
    输出科目 = 历次科目名称[0]

    输出成绩 = []
    for i in range(len(历次科目名称[0])):
        输出成绩.append([历次成绩[0][i]])
        for j in range(len(各科历次成绩字典) - 1):
            输出成绩[i].append(0)
    for i in range(len(各科历次成绩字典) - 1):
        for j in range(len(历次科目名称[i + 1])):
            if 历次科目名称[i + 1][j] in 历次科目名称[0]:
                输出成绩[历次科目名称[0].index(历次科目名称[i + 1][j])][i + 1] = (历次成绩[i + 1][历次科目名称[i + 1].index(历次科目名称[i + 1][j])])
            else:
                输出成绩.append([])
                for x in range(len(各科历次成绩字典)):
                    输出成绩[-1].append(0)
                输出成绩[-1][i + 1] = (历次成绩[i + 1][历次科目名称[i + 1].index(历次科目名称[i + 1][j])])
                输出科目.append(历次科目名称[i + 1][j])

    for i in range(len(输出成绩)):
        输出成绩[i].reverse()
    y_axis_data = 输出成绩
    for i in range(len(输出科目)):

        # print(y_axis_data)
        # plot中参数的含义分别是横轴值，纵轴值，线的形状，颜色，透明度,线的宽度和标签
        x_axis_data = []
        for j in range(len(y_axis_data[i])):
            x_axis_data.append(j)
        plt.plot(x_axis_data, y_axis_data[i], '-', color='#4169E1', alpha=0.8, linewidth=1, label=输出科目[i])
        # 显示标签，如果不加这句，即使在plot中加了label='一些数字'的参数，最终还是不会显示标签

        plt.legend(loc="upper right")
        plt.xlabel('考试次数')
        plt.ylabel('分数')
        for x in range(读取数量):
            plt.text(x_axis_data[x], float(y_axis_data[i][x]) + 0.2, str(y_axis_data[i][x]))
        plt.savefig('{1}/{0}.jpg'.format(输出科目[i], username))
        plt.close()
        x_axis_data = []
    y_axis_data = []

def 保存txt():
    files = open('通信文件.txt','w',encoding='utf-8')
    files.write(username+"\n"+str(len(输出科目)))




preselected_options = ["语文", "数学", "英语", "物理", "化学", "道法", "政治", "历史", "生物", "理综", "文综"]
选择的科目 = []
选择的姓名 = []
选择的总分 = []
最终选择 = []
root = None
def 创造按钮(root, checkbox_labels, preselected_options, i):
    checkbox_vars = []  # 初始化选择框
    l1 = tk.Label(root, text='第{}次考试科目'.format(i + 1))  # 标题
    l1.grid(row=0, columnspan=len(checkbox_labels))  # 控制位置
    checkbox_vars.append([])
    checkbox_vars.append([])
    checkbox_vars.append([])

    for label in checkbox_labels:  # 遍历取值
        var = tk.IntVar()  # 用var控制是否在预选里，初始为0
        if label in preselected_options:  # 判断是否在预选里
            var.set(1)  # 设置初始状态为选中

        checkbox_vars[0].append(var)  # 在返回列表里写入变量
        checkbox = tk.Checkbutton(root, text=label, variable=var)  # 用变量控制按钮
        checkbox.grid(column=checkbox_labels.index(label), row=1)  # 控制位置
    # 姓名选择
    l2 = tk.Label(root, text='请选择姓名')  # 标题
    l2.grid(row=4, columnspan=len(checkbox_labels))  # 控制位置
    for label in checkbox_labels:  # 遍历取值
        var = tk.IntVar()  # 用var控制是否在预选里，初始为0
        checkbox_vars[1].append(var)  # 在返回列表里写入变量

        checkbox = tk.Checkbutton(root, text=label, variable=var)  # 用变量控制按钮
        checkbox.grid(column=checkbox_labels.index(label), row=5)  # 控制位置
        if label == "姓名":  # 判断是否在预选里
            var.set(1)  # 设置初始状态为选中

    # 总分选择
    l3 = tk.Label(root, text='请选择总分')  # 标题
    l3.grid(row=6, columnspan=len(checkbox_labels))  # 控制位置
    for label in checkbox_labels:  # 遍历取值
        var = tk.IntVar()  # 用var控制是否在预选里，初始为0
        checkbox_vars[2].append(var)  # 在返回列表里写入变量

        checkbox = tk.Checkbutton(root, text=label, variable=var)  # 用变量控制按钮
        checkbox.grid(column=checkbox_labels.index(label), row=7)  # 控制位
        if label == "总分":  # 判断是否在预选里
            var.set(1)  # 设置初始状态为选中
    return checkbox_vars  # 返回选择列表


def 获取按钮值(checkbox_vars, root):
    selected_values = [var.get() for var in checkbox_vars[0]]
    selected_values_name = [var.get() for var in checkbox_vars[1]]
    selected_values_sum = [var.get() for var in checkbox_vars[2]]
    global 选择的科目
    选择的科目.append(selected_values)
    选择的姓名.append(selected_values_name)
    选择的总分.append(selected_values_sum)
    root.quit()  # 终止主循环并停止程序运行
    root.destroy()

def 选择科目():
    for i in range(len(data_row_history)):
        root = tk.Tk()
        weight = int(len(data_row_history[i][0]) * 60)
        root.geometry("{}x300".format(weight))
        checkbox_vars = 创造按钮(root, data_row_history[i][0], preselected_options, i)

        button = tk.Button(root, text="确定", command=lambda: 获取按钮值(checkbox_vars, root))
        button.grid(row=8, columnspan=len(data_row_history[i][0]))
        root.mainloop()

    for j in range(len(选择的科目)):
        最终选择.append([])
        for i in range(len(选择的科目[j])):
            最终选择[j].append(选择的科目[j][i] + 选择的总分[j][i] + 选择的姓名[j][i])
    result_col = []
    result_row = []
    for j in range(len(选择的科目)):
        result_col.append([item2 for item1, item2 in zip(最终选择[j], data_col_history[j]) if item1 == 1])

    for j in range(len(选择的科目)):
        result_row.append([])
        for i in range(len(data_row_history[j])):
            result_row[j].append([item_b for item_a, item_b in zip(最终选择[j], data_row_history[j][i]) if item_a == 1])

    return result_col, result_row


#print(data_row_history)

result_col, result_row = 选择科目()

data_row = result_row[0]
data_col = result_col[0]

print(data_col)
# 删除第一横排第一项：姓名
data_row[0].pop(0)
# 设置全班名字，删除第一竖排第0项‘姓名’
allname = data_col[0]
allname.pop(0)

科目 = list(data_row[0])
科目name = tuple(data_row[0])
各科成绩排名 = []
科目字典 = data_row[0]
各科全班平均分 = []
各科分段平均分 = []
科目数量 = len(科目name)
print(科目name)

for i in range(科目数量):
    # 读取各科成绩单
    科目[i] = data_col[i + 1]
    # 删除此列第一项（第一项为科目名称，转为纯数字列表来排序）
    科目[i].pop(0)
    # 排序

    #科目[i].append(sum())
    各科成绩排名.append(sorted(科目[i], reverse=True))
    # 把姓名与各科成绩结合成字典
    科目[i] = zip(allname, 科目[i])

    科目[i] = dict(科目[i])
    科目字典[i] = dict(科目[i])

    科目[i] = sorted(科目[i].items(), key=lambda x: x[1], reverse=True)
    # 计算平均分
    各科目成绩 = data_col[i + 1]
    各科全班平均分.append(sum(各科目成绩) / len(allname))

    # print(科目name[i],科目[i])
# print(各科成绩排名)


个人各科成绩 = list(科目name)  # 读取各个科目
个人各科成绩排名 = []
所处分段 = 0
print('指引:请输入"秦昊"')
username =input("请输入您的姓名")
# 暂时修改
print(data_col_history)
print(data_row_history)
if username in allname:
    print('查询到以下结果')
    # [[['秦昊', '孙文旭', '柏昕彤', '王福栋', '郑文轩', '李勇昊', '杜文慧', '冯雨晴', '杨曦', '王宇浩', '鲍明浩', '李清睿', '朱万达', '秦国强', '曹哲', '祝怀美',
    #    '鲍广欣', '张曦月', '高明庆', '刘航宇', '高家旺', '闵功堂', '李子涵', '尤冠霖', '郑昊阳', '赵梦雪', '高男子', '刘洪举', '胡姊洋', '郭恩杰', '于怀鑫', '周浩',
    #    '朱梓萌', '闫慧欣', '王悦', '张铭倩', '王俊贤', '沙赛玉', '韩天雨', '徐硕', '邢铭宸', '孙镱洋', '徐振博', '杨文静', '杜娟', '孟祥瑞', '王燕', '杨程翔',
    #    '杨明成', '王永鹏', '郝翼', '诸葛瑞柯', '尹凯越', '高玉豪', '谷瑞鑫', '李子昊', '王馨博', '王俊'],
    #   [93.5, 88.0, 83.5, 80.5, 89.0, 88.0, 89.0, 90.0, 95.5, 76.5, 86.5, 98.5, 76.5, 84.0, 82.5, 84.0, 82.0, 86.0, 87.5,
    #    78.5, 80.5, 71.0, 96.5, 82.0, 84.5, 80.0, 83.0, 83.0, 83.0, 86.5, 74.5, 75.0, 86.0, 79.0, 95.5, 84.5, 72.0, 68.5,
    #    63.0, 79.0, 78.0, 59.0, 63.5, 74.0, 62.0, 65.0, 73.5, 65.0, 60.0, 62.5, 75.5, 60.0, 67.5, 70.0, 59.0, 51.5, 0.0,
    #    0.0],
    #   [112.0, 104.0, 102.0, 106.0, 104.0, 103.0, 104.0, 100.0, 74.0, 95.0, 112.0, 86.0, 96.0, 96.0, 97.0, 81.0, 102.0,
    #    92.0, 97.0, 91.0, 89.0, 77.0, 82.0, 105.0, 77.0, 71.0, 54.0, 76.0, 92.0, 76.0, 70.0, 92.0, 80.0, 87.0, 52.0,
    #    73.0, 64.0, 78.0, 86.0, 52.0, 68.0, 70.0, 85.0, 83.0, 71.0, 60.0, 66.0, 53.0, 41.0, 55.0, 29.0, 59.0, 40.0, 36.0,
    #    22.0, 18.0, 0.0, 0.0],
    #   [80.5, 75.0, 89.0, 80.5, 81.5, 70.0, 79.5, 91.5, 73.5, 77.0, 64.0, 86.0, 43.5, 67.0, 51.5, 72.5, 64.0, 61.5, 45.0,
    #    59.0, 60.0, 33.5, 51.5, 65.0, 67.5, 67.0, 71.5, 59.0, 45.0, 45.0, 48.5, 34.0, 46.0, 47.0, 78.0, 37.0, 54.0, 49.0,
    #    26.0, 37.5, 36.0, 36.5, 30.0, 33.0, 59.0, 28.5, 35.5, 34.0, 19.0, 39.0, 27.5, 16.0, 38.5, 16.0, 21.0, 15.5, 0.0,
    #    0.0],
    #   [92.0, 84.0, 84.0, 87.0, 77.0, 82.0, 71.0, 73.0, 79.0, 83.0, 82.0, 69.0, 79.0, 57.0, 74.0, 65.0, 57.0, 57.0, 77.0,
    #    62.0, 64.0, 77.0, 58.0, 65.0, 54.0, 61.0, 65.0, 63.0, 65.0, 53.0, 48.0, 54.0, 46.0, 57.0, 53.0, 42.0, 48.0, 51.0,
    #    56.0, 56.0, 48.0, 42.0, 50.0, 42.0, 46.0, 60.0, 33.0, 47.0, 39.0, 39.0, 34.0, 45.0, 24.0, 24.0, 25.0, 20.0, 0.0,
    #    0.0],
    #   [91.0, 97.0, 96.0, 94.0, 90.0, 87.0, 89.0, 79.0, 85.0, 96.0, 89.0, 86.0, 87.0, 72.0, 82.0, 68.0, 78.0, 83.0, 74.0,
    #    82.0, 67.0, 86.0, 70.0, 49.0, 64.0, 70.0, 55.0, 54.0, 60.0, 63.0, 74.0, 73.0, 60.0, 52.0, 43.0, 63.0, 73.0, 65.0,
    #    65.0, 38.0, 49.0, 65.0, 59.0, 52.0, 41.0, 55.0, 25.0, 32.0, 32.0, 27.0, 21.0, 40.0, 34.0, 24.0, 19.0, 23.0, 0.0,
    #    0.0],
    #   ['道法', 86.0, 88.0, 94.0, 71.0, 88.0, 83.0, 84.0, 79.0, 90.0, 66.0, 72.0, 65.0, 86.0, 91.0, 75.0, 75.0, 73.0, 73.0,
    #    50.0, 73.0, 74.0, 85.0, 62.0, 65.0, 73.0, 76.0, 75.0, 68.0, 70.0, 69.0, 68.0, 80.0, 69.0, 73.0, 73.0, 66.0, 55.0,
    #    56.0, 51.0, 67.0, 57.0, 60.0, 46.0, 60.0, 54.0, 50.0, 59.0, 64.0, 51.0, 28.0, 54.0, 35.0, 42.0, 42.0, 41.0, 41.0,
    #    0.0, 0.0],
    #   ['历史', 83.0, 91.0, 77.0, 86.0, 70.0, 86.0, 67.0, 65.0, 77.0, 63.0, 48.0, 60.0, 75.0, 71.0, 57.0, 70.0, 59.0, 54.0,
    #    74.0, 58.0, 68.0, 71.0, 77.0, 65.0, 71.0, 58.0, 76.0, 68.0, 53.0, 61.0, 70.0, 45.0, 65.0, 54.0, 46.0, 68.0, 59.0,
    #    47.0, 48.0, 60.0, 53.0, 53.0, 52.0, 41.0, 36.0, 44.0, 43.0, 37.0, 47.0, 35.0, 44.0, 28.0, 31.0, 33.0, 37.0, 47.0,
    #    0.0, 0.0],
    #   [638.0, 627.0, 625.5, 605.0, 599.5, 599.0, 583.5, 577.5, 574.0, 556.5, 553.5, 550.5, 543.0, 538.0, 519.0, 515.5,
    #    515.0, 506.5, 504.5, 503.5, 502.5, 500.5, 497.0, 496.0, 491.0, 483.0, 479.5, 471.0, 468.0, 453.5, 453.0, 453.0,
    #    452.0, 449.0, 440.5, 433.5, 425.0, 414.5, 395.0, 389.5, 389.0, 385.5, 385.5, 385.0, 369.0, 362.5, 335.0, 332.0,
    #    289.0, 285.5, 285.0, 283.0, 277.0, 245.0, 224.0, 216.0, 0.0, 0.0]], [
    #      ['姓名', '秦昊', '柏昕彤', '冯雨晴', '李勇昊', '郑文轩', '祝怀美', '王福栋', '刘航宇', '孙文旭', '尤冠霖', '杜文慧', '王宇浩', '李清睿', '鲍明浩', '赵梦雪',
    #       '高家旺', '李子涵', '杨曦', '曹哲', '张曦月', '鲍广欣', '秦国强', '胡姊洋', '郑昊阳', '刘洪举', '高明庆', '杨文静', '闫慧欣', '闵功堂', '王悦', '高男子',
    #       '朱万达', '沙赛玉', '周浩', '朱梓萌', '郭恩杰', '于怀鑫', '邢铭宸', '王俊贤', '徐振博', '王永鹏', '张铭倩', '尹凯越', '孟祥瑞', '杨程翔', '徐硕', '韩天雨',
    #       '杜娟', '王燕', '诸葛瑞柯', '郝翼', '王俊', '王馨博', '高玉豪', '杨明成', '李子昊', '谷瑞鑫'],
    #      ['语文', 98.0, 103.0, 99.0, 96.0, 100.0, 101.0, 98.0, 99.0, 99.0, 100.0, 101.0, 88.0, 94.0, 95.0, 97.0, 94.0,
    #       103.0, 96.0, 96.0, 95.0, 91.0, 95.0, 94.0, 95.0, 80.0, 88.0, 93.0, 88.0, 85.0, 99.0, 76.0, 91.0, 73.0, 92.0,
    #       88.0, 83.0, 90.0, 94.0, 85.0, 88.0, 82.0, 87.0, 79.0, 84.0, 75.0, 80.0, 70.0, 67.0, 79.0, 77.0, 88.0, 76.0,
    #       77.0, 72.0, 61.0, 57.0, 56.0],
    #      ['数学', 114.0, 111.0, 112.0, 108.0, 107.0, 109.0, 106.0, 113.0, 107.0, 110.0, 104.0, 104.0, 101.0, 113.0, 103.0,
    #       98.0, 92.0, 66.0, 110.0, 106.0, 104.0, 89.0, 92.0, 99.0, 85.0, 109.0, 92.0, 104.0, 88.0, 74.0, 71.0, 73.0,
    #       109.0, 82.0, 96.0, 79.0, 71.0, 71.0, 81.0, 77.0, 66.0, 57.0, 47.0, 70.0, 76.0, 48.0, 74.0, 64.0, 40.0, 40.0,
    #       36.0, 48.0, 50.0, 36.0, 46.0, 22.0, 9.0],
    #      ['英语', 90.0, 85.0, 94.0, 85.0, 80.0, 78.0, 84.0, 74.0, 78.0, 70.0, 87.0, 84.0, 81.0, 61.0, 67.0, 72.0, 62.0,
    #       83.0, 62.0, 66.0, 62.0, 71.0, 58.0, 69.0, 74.0, 53.0, 57.0, 44.0, 37.0, 77.0, 72.0, 47.0, 53.0, 58.0, 54.0,
    #       47.0, 57.0, 43.0, 53.0, 34.0, 48.0, 33.0, 49.0, 34.0, 44.0, 38.0, 29.0, 49.0, 34.0, 27.0, 18.0, 35.0, 26.0,
    #       24.0, 18.0, 24.0, 12.0],
    #      ['物理', 90.0, 91.0, 90.0, 100.0, 89.0, 91.0, 81.0, 90.0, 86.0, 83.0, 84.0, 87.0, 94.0, 83.0, 76.0, 80.0, 71.0,
    #       81.0, 76.0, 66.0, 71.0, 61.0, 72.0, 65.0, 77.0, 71.0, 68.0, 68.0, 74.0, 50.0, 65.0, 64.0, 60.0, 56.0, 52.0,
    #       55.0, 28.0, 45.0, 63.0, 73.0, 73.0, 50.0, 35.0, 59.0, 53.0, 39.0, 64.0, 37.0, 44.0, 40.0, 33.0, 20.0, 38.0,
    #       32.0, 30.0, 27.0, 27.0],
    #      ['道法', 97.0, 96.0, 94.0, 96.0, 95.0, 94.0, 96.0, 94.0, 96.0, 89.0, 96.0, 96.0, 85.0, 94.0, 87.0, 92.0, 90.0,
    #       95.0, 85.0, 91.0, 88.0, 94.0, 85.0, 82.0, 85.0, 81.0, 90.0, 96.0, 96.0, 79.0, 86.0, 85.0, 86.0, 85.0, 75.0,
    #       82.0, 88.0, 87.0, 52.0, 77.0, 79.0, 83.0, 86.0, 69.0, 81.0, 85.0, 65.0, 68.0, 82.0, 64.0, 61.0, 72.0, 36.0,
    #       42.0, 43.0, 62.0, 64.0],
    #      ['历史', 97.0, 92.0, 89.0, 92.0, 95.0, 92.0, 93.0, 86.0, 85.0, 98.0, 78.0, 87.0, 88.0, 86.0, 91.0, 84.0, 98.0,
    #       93.0, 82.0, 82.0, 80.0, 79.0, 86.0, 75.0, 83.0, 79.0, 75.0, 74.0, 81.0, 71.0, 79.0, 86.0, 62.0, 67.0, 74.0,
    #       77.0, 81.0, 69.0, 74.0, 55.0, 53.0, 81.0, 82.0, 61.0, 48.0, 84.0, 66.0, 51.0, 48.0, 62.0, 60.0, 42.0, 29.0,
    #       48.0, 46.0, 44.0, 35.0],
    #      ['总分', 586.0, 578.0, 578.0, 577.0, 566.0, 565.0, 558.0, 556.0, 551.0, 550.0, 550.0, 546.0, 543.0, 532.0, 521.0,
    #       520.0, 516.0, 514.0, 511.0, 506.0, 496.0, 489.0, 487.0, 485.0, 484.0, 481.0, 475.0, 474.0, 461.0, 450.0,
    #       449.0, 446.0, 443.0, 440.0, 439.0, 423.0, 415.0, 409.0, 408.0, 404.0, 401.0, 391.0, 378.0, 377.0, 377.0,
    #       374.0, 368.0, 336.0, 327.0, 310.0, 296.0, 293.0, 256.0, 254.0, 244.0, 236.0, 203.0]]]
    # [[['姓名', '语文', '数学', '英语', '物理', '化学', '道法', '历史', '总分'], ['秦昊', 93.5, 112.0, 80.5, 92.0, 91.0, 86.0, 83.0, 638.0],
    #   ['孙文旭', 88.0, 104.0, 75.0, 84.0, 97.0, 88.0, 91.0, 627.0],
    #   ['柏昕彤', 83.5, 102.0, 89.0, 84.0, 96.0, 94.0, 77.0, 625.5],
    #   ['王福栋', 80.5, 106.0, 80.5, 87.0, 94.0, 71.0, 86.0, 605.0],
    #   ['郑文轩', 89.0, 104.0, 81.5, 77.0, 90.0, 88.0, 70.0, 599.5],
    #   ['李勇昊', 88.0, 103.0, 70.0, 82.0, 87.0, 83.0, 86.0, 599.0],
    #   ['杜文慧', 89.0, 104.0, 79.5, 71.0, 89.0, 84.0, 67.0, 583.5],
    #   ['冯雨晴', 90.0, 100.0, 91.5, 73.0, 79.0, 79.0, 65.0, 577.5]],
    #  [['姓名', '语文', '数学', '英语', '物理', '道法', '历史', '总分'], ['秦昊', 98.0, 114.0, 90.0, 90.0, 97.0, 97.0, 586.0],
    #   ['柏昕彤', 103.0, 111.0, 85.0, 91.0, 96.0, 92.0, 578.0], ['冯雨晴', 99.0, 112.0, 94.0, 90.0, 94.0, 89.0, 578.0],
    #   ['李勇昊', 96.0, 108.0, 85.0, 100.0, 96.0, 92.0, 577.0], ['郑文轩', 100.0, 107.0, 80.0, 89.0, 95.0, 95.0, 566.0],
    #   ['祝怀美', 101.0, 109.0, 78.0, 91.0, 94.0, 92.0, 565.0], ['王福栋', 98.0, 106.0, 84.0, 81.0, 96.0, 93.0, 558.0]]]

    # 处理各科分数
    for i in range(科目数量):
        # print(科目字典)
        # 读取个人各科成绩，前面已经准备好各人对应的各科成绩
        个人各科成绩[i] = 科目字典[i].get(username)
        # 将个人各科排名添加进列表
        个人各科成绩排名.append(各科成绩排名[i].index(个人各科成绩[i]))
        print(科目name[i], 个人各科成绩[i])

    # 处理分段分数
    # 获取个人分段
    print(个人各科成绩排名)
    print(个人各科成绩)
    所处分段 = (个人各科成绩排名[-1] + 1) // 10
    for i in range(科目数量):
        # 计算平均分
        各科目成绩 = data_col[i + 1][(所处分段) * 10:(所处分段 + 1) * 10 + 1]

        各科分段平均分.append(sum(各科目成绩) / len(各科目成绩))

    # 创建文件夹
    # 调用函数
    file = "{0}".format(username)
    创建文件夹(file)  # 这些都是函数！！！！！！！！！！
    饼状图()  # 为了方便直观直接以中文定义
    保存分段与个人对比()
    各科全班与分段对比()
    折线图()
    保存txt()

    web.open('cjfx.qinhao2008.top')

else:
    print('对不起，没有找到相关学生')