'''
tkinter
创建窗口   输入框 按钮 静态文本

添加控件 按钮点击

添加事件
'''


'''
创建一个窗口,并显示出来

'''
import  tkinter

if __name__ =='__main__':
    '''
    1. 创建一个窗口, 兵线输出来
    '''
    #创建一个窗口
    win = tkinter.Tk()

    #所有控件和事件一定要放在mainloop之上
    '''
    2. 改变窗口大小
    '''
    #窗口居中显示
    screen_width=win.winfo_screenwidth()
    screen_height=win.winfo_screenheight()
    windows_width= 800
    windows_height=500
    x = (screen_width -windows_width)//2
    y = (screen_height- windows_height)//2
    win.geometry('%dx%d+%d+%d'%(windows_width, windows_height,x,y))


    #修改窗口的标题
    win.wm_title('搜索引擎')


    #固定窗口大小
    #两个值必须是布尔值 ture代表可以改变
    win.resizable(width=False,height=False)

    container = tkinter.Frame(master=self, bg='red')

    container.pack(fill=tkinter.BOTH, expand=True)







    #调用消息循环
    win.mainloop()
