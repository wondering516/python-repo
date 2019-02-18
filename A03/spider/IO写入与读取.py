
# 写入
with open("test.txt", "wt") as out_file:
    out_file.write("在write文件中写入数据")

# 读取
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)