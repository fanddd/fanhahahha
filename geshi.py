# # 读取 data1.txt 文件内容
# with open("data1.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#
# # 构造所需格式的列表
# info = [
#     {'name': line.split('|')[0], 'pwd': line.split('|')[1], 'email': line.split('|')[2].strip()}
#     for line in lines
# ]
#
# # 打印结果以验证
# print(info)

# v1 = (11, 22, 33)
# v2 = [44, 55, 66]
# # 将元组中的元素追加到列表中
# v2.extend(v1)
# print(v2)

