import calendar

print('Python 生成日历')
yy = int(input('输入年份：'))
mm = int(input('输入月份：'))
print(calendar.month(yy, mm))
