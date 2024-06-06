import pandas as pd
import json

# 保存数据到文件
def saveFile(filePath, data):
    # 写入data数据到filePath文件
    with open(filePath, "w") as f:
        f.write(data)

# 读取Excel数据
data = pd.read_excel("file/translation.xlsx")

# 将数据转换为JSON格式
json_data = data.to_json(orient='records')
print(f'json_data:{json_data}')

# 写入JSON数据到txt文件
saveFile("file/translation.json", json_data)

# 读取JSON数据
with open("file/translation.json", "r") as f:
    json_data = f.read()

# 解析JSON数据
data = json.loads(json_data)

cn = '<resources xmlns:tools="http://schemas.android.com/tools">'
jp = cn

# 遍历JSON数据
def traverse_json(data):
    if isinstance(data, dict):
        # for key, value in data.items():
        #     print(f"Key: {key}")
        #     traverse_json(value)
        global cn
        cn += f'<string name="{data["@@locale"]}">{data["zh_CN"]}</string>\n'
        global jp
        jp += f'<string name="{data["@@locale"]}">{data["ja_JP"]}</string>\n'
    elif isinstance(data, list):
        for item in data:
            traverse_json(item)
    else:
        print(f"Value: {data}")

# 调用遍历函数
traverse_json(data)

# 写入数据到文件
saveFile("file/strings_cn.xml", cn)
saveFile("file/strings_jp.xml", jp)