from datetime import datetime
weekdays = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期天"]
#读取当月excel文件
now = datetime.now()
now_str = str(now)
year_number = int(now_str[0:4])
mon_number = int(now_str[5:7])
day_number = int(now_str[8:10])

#file_path被引用
file_path = "D:\\myfile\\pythonFile\\Task-progress-visualization-main\\newfile\standingSystem\\excel\\" + str(mon_number)  + "月.xlsx" #打开对应月份文件
file_path_last = "D:\\myfile\\pythonFile\\Task-progress-visualization-main\\newfile\standingSystem\\excel\\" + str(mon_number-1) + "月.xlsx"

# 构造datetime对象
date = datetime(year_number ,mon_number,day_number)
# 调用weekday()方法获取星期几，返回值为0~6，分别表示周一到周日 

weekday = date.weekday()  
weekday_str = weekdays[weekday]
print("今天是"+str(year_number)+"年"+str(mon_number)+"月"+str(day_number)+"日",str(weekday_str))




 



