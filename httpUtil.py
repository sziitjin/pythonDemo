import requests

url = 'https://mzapi.life911.cn/mzLifeApi/getMzWallpaperCategories'
params = '{"num":10,"state":true}'
response = requests.post(url, json=params)
if response.status_code == 200:
    result = response.json()  # 如果API返回的是JSON数据
    # 处理结果
    print(result)
else:
    print(f'请求失败:{response.json()}')
