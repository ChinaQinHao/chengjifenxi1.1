import xlrd
from matplotlib import font_manager
from pylab import *
import os
import tkinter as tk
from tkinter import filedialog
import webbrowser as web
import tkinter
#from tkinter import ttk


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
    root = tk.Tk()
    root.withdraw()
    global f_path
    f_path = filedialog.askopenfilename()
    return ('{}'.format(f_path))


my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")

# print('已开启参赛指引')
# print('指引:请输入3')
# a = int(input('请输入读取文件的数量(纯数字)'))
#
# print('请选择要分析的成绩单（此次选择决定饼状图与条形图分析）')
# print('指引:请选择名称为"3.xls"的成绩单')

弹出读取次数()
第一次读取 = 打开文件资源管理器()



# print('指引:请依次选择"2.xls""1.xls"')


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
    分段成绩 = 各科分段平均分[:-1]
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
    位置 = data_col_history[0][0].index(username)
    各科历次成绩 = []
    各科历次成绩字典 = []
    for j in range(len(data_col_history)):
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





# 按列读取
data_col = [sheet_1.col_values(i) for i in range(sheet_1.ncols)]
# 按行读取
data_row = []

for row in range(sheet_1.nrows):
    data_row.append(sheet_1.row_values(row))
# print(data_col)
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
username = input("请输入您的姓名")
# 暂时修改

if username in allname:
    print('查询到以下结果')

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