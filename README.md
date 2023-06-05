# Task-progress-visualization
一个利用excel表格与pyecharts图的python实战
## 运行环境
python环境、需要安装pyecharts、openpyxl、bs4、pandas、numpy库
## 代码位置
本程序代码主文件：excelOutput.py

读取的表格xslx文件位于excel子文件下

## 完成功能
读取excel表，根据数据类型生成进度网页图表
通过交互，自动生成指定时间内的周报

## 注意事项
发生过一次异常，即图表在edge、chrome中不显示
原因：在internet连接中中使用代理。
解决方法：cmd-inetcpl.cpl-连接-取消勾选-终端exit退出
再次打开html文件，即可正常显示

