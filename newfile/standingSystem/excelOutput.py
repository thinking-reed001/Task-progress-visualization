import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Gauge, Bar


#指定区间内容
file_path =r"C:\Users\Administrator\AppData\Local\Programs\Python\Python310\newfile\standingSystem\excel\Total.xlsx"
sheet_name1 = "Sheet1"
df1 = pd.read_excel(file_path,sheet_name=sheet_name1) #读取Sheet1

qujian_list =df1['线路区间'].tolist() 
changdu_list =df1['长度\日期'].tolist()
heji_tag = df1['合计'].tolist()


jingtai_list =[0]*len(qujian_list) #1
paishui_list =[0]*len(qujian_list) #3
qiaohan_list =[0]*len(qujian_list) #5
for i in range(len(heji_tag)):
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
    elif(heji_tag[i] == 4): #5
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
chart3.add_yaxis('桥涵检查', qiaohan_list ,itemstyle_opts={'color':'green'}) 
chart3.render(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python310\newfile\standingSystem\html\区间完成度.html")



#指定整数内容
sheet_name2 = "Sheet2"
df2 = pd.read_excel(file_path,sheet_name=sheet_name2) #读取Sheet2
zhengshu_list =df2['内容\日期'].tolist() 
heji_tag2 = df2['合计'].tolist()

#整数完成度
chart4 = Bar() 
chart4.add_xaxis(zhengshu_list) 
chart4.set_global_opts(
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(
            interval=0, # 设置坐标轴刻度的显示间隔，0为全部显示
            rotate=0,  # 设置标签文字旋转角度，单位为度
            font_size=12 # 设置标签文字大小
        )
    )
)
chart4.add_yaxis('整月进度', heji_tag2) 
chart4.render(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python310\newfile\standingSystem\html\整数完成度.html")

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
zhengshi_barvalue =[0,0,0,0,0] 
for i in range(len(quxian_jindu_out)):    #遍历完成列表
    for j in range(len(quxian_total)):    #用总列表逐个匹配
        if(quxian_jindu_out[i] == quxian_total[j]):
             zhengshi_barvalue[j] = int(quxian_jindu_out[i] == quxian_total[j])*100 #布朗值转化整数
              
#生成正矢完成度图表
chart0 = Bar() 
chart0.add_xaxis(quxian_total) 
chart0.add_yaxis('曲线正矢检查完成度', zhengshi_barvalue) 
chart0.set_global_opts(
    yaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(
            formatter="{value}%"
        )
    )
)
chart0.render(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python310\newfile\standingSystem\html\正矢检查完成度.html")


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
fudai_barvalue =[0,0,0,0,0] 
for i in range(len(fudai_jindu_out)):    #遍历完成列表
    for j in range(len(fudai_total)):    #用总列表逐个匹配
        if(fudai_jindu_out[i] == fudai_total[j]):
            fudai_barvalue[j] = int(fudai_jindu_out[i] == fudai_total[j])*100 #布朗值转化整数 *3
            
#生成附带曲线完成度图表
chart1 = Bar() 
chart1.add_xaxis(fudai_total) 
chart1.add_yaxis('附带曲线检查完成度', fudai_barvalue) 
chart1.set_global_opts(
    yaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(
            formatter="{value}%"
        )
    )
)
chart1.render(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python310\newfile\standingSystem\html\附带曲线检查完成度.html")



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
    yaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(
            formatter="{value}%"
        )
    )
)
chart2.render(r"C:\Users\Administrator\AppData\Local\Programs\Python\Python310\newfile\standingSystem\html\道岔检查完成度.html")
