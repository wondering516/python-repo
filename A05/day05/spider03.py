'''
异常处理
    程序在运行过程中, 出现了一些未知错误

    捕获异常
    try:
        可能出现异常的代码
    except:
        对异常进行处理
'''

a = 10
b = 0
try:
    c = a / b
    print('a / b = ' + str(c))
except:
    print('除数不能是0')

print('结束')