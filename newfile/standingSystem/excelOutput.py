import os
import pandas as pd
import openpyxl
import pyecharts.options as opts
from pyecharts.charts import Gauge, Bar
from datafile import file_path,file_path_last

#file1 与file2是为了自动生成周报和旬报设计的
# 读取第一个xlsx文件
file1 = pd.read_excel(file_path, sheet_name=None)
# 读取第二个xlsx文件
file2 = pd.read_excel(file_path_last, sheet_name=None)

#df1是为了生成网页设计的
sheet_name1 = "Sheet1"
df1 = pd.read_excel(file_path,sheet_name=sheet_name1) #读取Sheet1
qujian_list =df1['线路区间'].tolist() 
changdu_list =df1['长度\日期'].tolist()
heji_tag = df1['合计'].tolist()

jingtai_list =[0]*len(qujian_list) #1
paishui_list =[0]*len(qujian_list) #3
qiaohan_list =[0]*len(qujian_list) #5
for i in range(len(heji_tag)):    #heji_tag是最后一行的合计列表
    if(heji_tag[i] == 9): #1+3+5
        jingtai_list[i] = 1
        paishui_list[i] = 1
        qiaohan_list[i] = 1
    elif(heji_tag[i] == 8): #3+5 
        paishui_list[i] = 1
        qiaohan_list[i] = 1
    elif(heji_tag[i] == 6): #1+5 
        jingtai_list[i] = 1
        qiaohan_list[i] = 1
    elif(heji_tag[i] == 5): #5 
        qiaohan_list[i] = 1
    elif(heji_tag[i] == 4): #4
        paishui_list[i] = 1
        jingtai_list[i] = 1
    elif(heji_tag[i] == 3): #3
        paishui_list[i] = 1
    elif(heji_tag[i] == 1): #1
        jingtai_list[i] = 1




#生成月度html表
chart3 = Bar() 
chart3.add_xaxis(qujian_list) 
#横坐标参数
chart3.set_global_opts(
    title_opts=opts.TitleOpts(title="区间完成度"),
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(
            interval=0, # 设置坐标轴刻度的显示间隔，0为全部显示
            rotate=90,  # 设置标签文字旋转角度，单位为度
            font_size=8 # 设置标签文字大小
        )
    )
)

chart3.add_yaxis('静态检查', jingtai_list ,itemstyle_opts={'color':'yellow'}) 
chart3.add_yaxis('排水沟清理', paishui_list ,itemstyle_opts={'color':'red'}) 
chart3.add_yaxis('桥涵检查/其他项目', qiaohan_list ,itemstyle_opts={'color':'green'}) 
chart3.render(r"Task-progress-visualization-main\newfile\standingSystem\html\区间完成度.html", page_title="区间完成度")



#指定整数内容
sheet_name2 = "Sheet2"
df2 = pd.read_excel(file_path,sheet_name=sheet_name2) #读取Sheet2
zhengshu_list =df2['内容\日期'].tolist() 
heji_tag2 = df2['合计'].tolist()

#整数完成度
chart4 = Bar() 
chart4.add_xaxis(zhengshu_list) 
chart4.set_global_opts(
    title_opts=opts.TitleOpts(title="整数完成度"),
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(
            interval=0, # 设置坐标轴刻度的显示间隔，0为全部显示
            rotate=0,  # 设置标签文字旋转角度，单位为度
            font_size=12 # 设置标签文字大小
        )
    )
)
chart4.add_yaxis('整月进度', heji_tag2) 
chart4.render(r"Task-progress-visualization-main\newfile\standingSystem\html\整数完成度.html", page_title="整数完成度")

#读取表3
sheet_name3 = "Sheet3"
df3 = pd.read_excel(file_path,sheet_name=sheet_name3) #读取Sheet1
#读取正矢总量
quxian_total = df3.iloc[0,1]  #读取正矢总量的字符串 
quxian_total = quxian_total.replace("，",",")  #将所有中文逗号变成英文格式
quxian_total = quxian_total.replace("、",",")  
quxian_total = quxian_total.replace("k","K")  #统一k格式
quxian_total = [item.strip() for item in quxian_total.split(",")]  #列表推导式删除空格、以英文逗号隔开


#读取正矢检查流
quxian_jindu = df3.iloc[0,2:34] #为正矢检查行的series数据类型，虽然不符合0即第一行的常识
quxian_jindu = list(quxian_jindu)

quxian_jindu_out =[]  #统计实际曲线正矢检查量
for i in range(len(quxian_jindu)):   #遍历整个列表
    if(type(quxian_jindu[i]) == str  ):  #判断第i项是否是字符串类型
        quxian_jindu[i] = quxian_jindu[i].replace("k","K") #转换小写k为大写
        quxian_jindu[i] = quxian_jindu[i].replace("，",",")  #将所有中文逗号变成英文格式
        quxian_jindu[i] = quxian_jindu[i].split(',') #按照逗号分隔
        quxian_jindu[i] = [x.strip() for x in quxian_jindu[i] if x.strip()]  #列表推导式删除空格
        if set(quxian_jindu[i]).issubset(set(quxian_total)):    #判断清洗过后的数据是否符合曲线正矢检查的内容
            a = quxian_jindu[i] #创建一个a的列表
            for j in range(len(a)):
                quxian_jindu_out.append(a[j])  
#创建纵坐标               
zhengshi_barvalue =[0]*len(quxian_total) 
for i in range(len(quxian_jindu_out)):    #遍历完成列表
    for j in range(len(quxian_total)):    #用总列表逐个匹配
        if(quxian_jindu_out[i] == quxian_total[j]):
             zhengshi_barvalue[j] = int(quxian_jindu_out[i] == quxian_total[j])*100 #布朗值转化整数
              
#生成正矢完成度图表
chart0 = Bar() 
chart0.add_xaxis(quxian_total) 
chart0.add_yaxis('曲线正矢检查完成度', zhengshi_barvalue) 
chart0.set_global_opts(
    title_opts=opts.TitleOpts(title="正矢检查完成度"),
    yaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(
            formatter="{value}%"
        )
    ),
    datazoom_opts=[opts.DataZoomOpts()]
)
chart0.render(r"Task-progress-visualization-main\newfile\standingSystem\html\正矢检查完成度.html", page_title="正矢检查完成度")


#读取附带曲线总量
fudai_total = df3.iloc[1,1]  #读取附带曲线总量的字符串 
fudai_total = fudai_total.replace("，",",")  #将所有中文逗号变成英文格式
fudai_total = fudai_total.replace("、",",")
fudai_total = [item.strip() for item in fudai_total.split(",")]  #列表推导式删除空格、以英文逗号隔开
#读取附带曲线检查流
fudai_jindu = df3.iloc[1,2:34] #为附带检查行的series数据类型
fudai_jindu = list(fudai_jindu)
fudai_jindu_out =[]  #创建一个统计实际附带曲线检查条数的列表
for i in range(len(fudai_jindu)):   #遍历每日实际检查列表
    if(type(fudai_jindu[i]) == str  ):  #判断第i项是否是字符串类型
        fudai_jindu[i] = fudai_jindu[i].replace("，",",")  #有，的话将所有中文逗号变成英文格式
        fudai_jindu[i] = fudai_jindu[i].split(',') #按照str里的英逗号分隔
        fudai_jindu[i] = [x.strip() for x in fudai_jindu[i] if x.strip()]  #列表推导式删除空格
        if set(fudai_jindu[i]).issubset(set(fudai_total)):    #判断清洗过后的数据是否是附带曲线检查的内容
            a = fudai_jindu[i] #创建一个a的列表
            for j in range(len(a)):
                fudai_jindu_out.append(a[j])  
#创建纵坐标               
fudai_barvalue =[0]*len(fudai_total)
for i in range(len(fudai_jindu_out)):    #遍历完成列表
    for j in range(len(fudai_total)):    #用总列表逐个匹配
        if(fudai_jindu_out[i] == fudai_total[j]):
            fudai_barvalue[j] = int(fudai_jindu_out[i] == fudai_total[j])*100 #布朗值转化整数 *3
            
#生成附带曲线完成度图表
chart1 = Bar() 
chart1.add_xaxis(fudai_total) 
chart1.add_yaxis('附带曲线检查完成度', fudai_barvalue) 
chart1.set_global_opts(
    title_opts=opts.TitleOpts(title="附带曲线检查完成度"),
    yaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(
            formatter="{value}%"
        )
    )
)
chart1.render(r"Task-progress-visualization-main\newfile\standingSystem\html\附带曲线检查完成度.html",page_title="附带曲线检查完成度")



#读取道岔检查总量
daocha_total = df3.iloc[2,1]  #读取附带曲线总量的字符串 
daocha_total = daocha_total.replace("，",",")  #将所有中文逗号变成英文格式
daocha_total = [item.strip() for item in daocha_total.split(",")]  #列表推导式删除空格、以英文逗号隔开
#读取道岔检查流
daocha_jindu = df3.iloc[2,2:34] #为附带检查行的series数据类型
daocha_jindu = list(daocha_jindu)
daocha_jindu_out =[]  #创建一个统计实际道岔检查条数的列表
for i in range(len(daocha_jindu)):   #遍历每日实际检查列表
    if(type(daocha_jindu[i]) == str  ):  #判断第i项是否是字符串类型
        daocha_jindu[i] = daocha_jindu[i].replace("、",",")
        daocha_jindu[i] = daocha_jindu[i].replace("，",",")  #有，的话将所有中文逗号变成英文格式
        daocha_jindu[i] = daocha_jindu[i].split(',') #按照str里的英逗号分隔
        daocha_jindu[i] = [x.strip() for x in daocha_jindu[i] if x.strip()]  #列表推导式删除空格
        if set(daocha_jindu[i]).issubset(set(daocha_total)):    #判断清洗过后的数据是否是道岔检查的内容
            a = daocha_jindu[i] #创建一个a的列表
            for j in range(len(a)):
                daocha_jindu_out.append(a[j])  
#创建纵坐标               
daocha_barvalue =[0,0,0,0,0] 
for i in range(len(daocha_jindu_out)):    #遍历完成列表
    for j in range(len(daocha_total)):    #用总列表逐个匹配
        if(daocha_jindu_out[i] == daocha_total[j]):
                 daocha_barvalue[j] = int(daocha_jindu_out[i] == daocha_total[j])*100 #布朗值转化整数
#生成道岔检查完成度图表
chart2 = Bar() 
chart2.add_xaxis(daocha_total) 
chart2.add_yaxis('道岔检查完成度', daocha_barvalue) 
chart2.set_global_opts(
    title_opts=opts.TitleOpts(title="道岔检查完成度"),
    yaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(
            formatter="{value}%"
        )
    )
)
chart2.render(r"Task-progress-visualization-main\newfile\standingSystem\html\道岔检查完成度.html", page_title="道岔检查完成度")





# 运行html_title_named文件，这是不用在开头import的方法
with open(r"Task-progress-visualization-main\newfile\standingSystem\html_title_named.py", 'r', encoding='utf-8') as f:
    code = compile(f.read(), r"Task-progress-visualization-main\newfile\standingSystem\html_title_named.py", 'exec')
    exec(code)






#做周报、做旬报
print("尊敬的主人，今天是否做周报或旬报\n如果是，按下Y键；\n如果不做,按任意键，不要按电源哦")
just_date = input()
if ((just_date == "y")|(just_date == "Y")):
    print("从何时算起，例如2023年1月24号则输入：24")
    start_day = input()
    start_day = int(start_day) #变成整数型
    print("以何时结束，例如2023年2月3号则输入：3")
    end_day = input()
    end_day = int(end_day)  #变成整数型
    if(end_day < start_day):   #有上个月的内容的情况
        print('执行跨月合并...')
        output_path = r'Task-progress-visualization-main\newfile\standingSystem\xunANDzhou\生成的旬周报（跨月）.xlsx'
        data = {}
        for name, sheet1 in file1.items():
            if name in file2:
                sheet2 = file2[name]
                data[name] = pd.concat(
                    [sheet1.iloc[:,0:2],sheet2.iloc[:, start_day+1:33], sheet1.iloc[:, 2:end_day+2]], axis=1
                ) #sheet1作为当前月份的表格，sheet2作为上一月份表格
        # 将提取出的数据存储为新的 xlsx 文件
        with pd.ExcelWriter(output_path) as writer:
            for name, df in data.items():
                df.to_excel(writer, index=False, sheet_name=name)
        print("需要跨月合并的报文已生成，快去xunANDzhou文件夹下看看吧")                  
    elif(end_day > start_day):  #只是本月的内容的情况
        print('不需要跨月合并...')
        output1_path = r'Task-progress-visualization-main/newfile/standingSystem/xunANDzhou/生成的旬周报（不跨月）.xlsx'
        # 遍历所有表格，提取第一行标签为a的列至第一行标签为b的列的数据
        data = {}
        for name, sheet1 in file1.items():
                data[name] = pd.concat(
                    [sheet1.iloc[:,0:2],sheet1.iloc[:, start_day+1:end_day+2]], axis=1
                )
        # 将提取出的数据存储为新的 xlsx 文件
        with pd.ExcelWriter(output1_path) as writer:      
            for name, df in data.items():
                df.to_excel(writer, index=False, sheet_name=name) 
        print("无需跨月合并的报文已生成，快去xunANDzhou文件夹下看看吧") 
    else:
        print("您的输入不符合规范，再见")
elif((just_date != "y")|(just_date != "Y")):
    print("再见")
 
 
