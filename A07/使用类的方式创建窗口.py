import tkinter

from main_frame import MainFrame

#创建一个TK类的子类
#子类继承父类所有的方法和属性
class MainView(tkinter.Tk):
    # 构造方法
    def __init__(self):
        #必须调用父类的构造方法
        super().__init__()
        # 窗口居中显示
        self.center

        self.title('sousuo')

        self.resizable(width=False,height=False)

        container =tkinter.Frame(master=self,bg='red')


        #将Frame显示出来
        container.pack(fill=tkinter.BOTH , expand =True)





    def center(self):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        windows_width = 800
        windows_height = 500
        x = (screen_width - windows_width) // 2
        y = (screen_height - windows_height) // 2
        win.geometry('%dx%d+%d+%d' % (windows_width, windows_height, x, y))



if __name__=='__main__':
    win = MainView()

    win.mainloop()