import time

print('按下回车开始计时。')
input('')
startTime = time.time()
print('开始计时：')
while True:
    if round(time.time() - startTime) > 60:
        print('结束：')
        print('计时时间：{0}'.format(round(time.time() - startTime, 2)))
        break
    else:
        time.sleep(1)
        print('开始计时：{0}'.format(round(time.time() - startTime)))
