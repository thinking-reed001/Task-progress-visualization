from bs4 import BeautifulSoup 

# 读取道岔检查HTML 文件
with open(r"Task-progress-visualization-main\newfile\standingSystem\html\道岔检查完成度.html", 'r', encoding='utf-8') as f:
    html = f.read()
# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html, 'html.parser')
# 找到 title 标签，并修改其文本内容
title_tag = soup.find('title')
title_tag.string = "道岔检查完成度"
# 将修改后的 HTML 内容写入文件
with open(r"Task-progress-visualization-main\newfile\standingSystem\html\道岔检查完成度.html", 'w', encoding='utf-8') as f:
    f.write(str(soup))


# 读取附带曲线检查HTML 文件
with open(r"Task-progress-visualization-main\newfile\standingSystem\html\附带曲线检查完成度.html", 'r', encoding='utf-8') as f:
    html = f.read()
# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html, 'html.parser')
# 找到 title 标签，并修改其文本内容
title_tag = soup.find('title')
title_tag.string = "附带曲线检查完成度"
# 将修改后的 HTML 内容写入文件
with open(r"Task-progress-visualization-main\newfile\standingSystem\html\附带曲线检查完成度.html", 'w', encoding='utf-8') as f:
    f.write(str(soup))


# 读取区间完成度HTML 文件
with open(r"Task-progress-visualization-main\newfile\standingSystem\html\区间完成度.html", 'r', encoding='utf-8') as f:
    html = f.read()
# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html, 'html.parser')
# 找到 title 标签，并修改其文本内容
title_tag = soup.find('title')
title_tag.string = "区间完成度"
# 将修改后的 HTML 内容写入文件
with open(r"Task-progress-visualization-main\newfile\standingSystem\html\区间完成度.html", 'w', encoding='utf-8') as f:
    f.write(str(soup))


# 读取整数完成度HTML 文件
with open(r"Task-progress-visualization-main\newfile\standingSystem\html\整数完成度.html", 'r', encoding='utf-8') as f:
    html = f.read()
# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html, 'html.parser')
# 找到 title 标签，并修改其文本内容
title_tag = soup.find('title')
title_tag.string = "整数完成度"
# 将修改后的 HTML 内容写入文件
with open(r"Task-progress-visualization-main\newfile\standingSystem\html\整数完成度.html", 'w', encoding='utf-8') as f:
    f.write(str(soup))



# 读取整数完成度HTML 文件
with open(r"Task-progress-visualization-main\newfile\standingSystem\html\正矢检查完成度.html", 'r', encoding='utf-8') as f:
    html = f.read()
# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html, 'html.parser')
# 找到 title 标签，并修改其文本内容
title_tag = soup.find('title')
title_tag.string = "正矢检查完成度"
# 将修改后的 HTML 内容写入文件
with open(r"Task-progress-visualization-main\newfile\standingSystem\html\正矢检查完成度.html", 'w', encoding='utf-8') as f:
    f.write(str(soup))