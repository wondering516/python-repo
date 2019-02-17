# 导入urllib库中的request模块
from urllib import request

# 构建出一个url - 资源的唯一标识 - 统一资源定位器
url = "https://maoyan.com/board"

# 发送请求 - 打开连接
# f = request.urlopen(url)
# data = f.read()
# print(data)
# f.close() # 手动释放资源

# 使用python3.x中with写法 - 可以自动释放资源,我们不需要手动去释放.
# python中的块使用缩进四格的方式
with request.urlopen(url) as resp:
    # 不推荐大家使用tab键
    data = resp.read() # 读取内容
    result = data.decode()
    print(result)
    # 希望将result结果保存到当前目录下的baidu.html文件中
    with open('猫眼榜单.html','w+',encoding='utf-8') as fp:
        fp.write(result) # 写入