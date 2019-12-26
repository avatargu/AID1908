import sys

if (sys.version_info > (3, 0)):
    from tkinter import *
    from tkinter import messagebox
else:
    from Tkinter import *

root = Tk()  # 创建tkinter窗口
root = mainloop()
root.title('2048(达内科技)')  # 设置标题文字
root.resizable(width=False, height=False)  # 固定宽和高
















