import os
import sys
import time
from pathlib import Path
from threading import Thread
from tkinter import END, Tk, Canvas, Entry, Button, PhotoImage

father_path = os.path.dirname(os.path.realpath(sys.argv[0]))+'\\assets'
def relative_to_assets(path: str) -> Path:
    return father_path / Path(path)

window = Tk()
windowX = window.winfo_screenwidth()
windowY = window.winfo_screenheight()
cen_x = (windowX-400) / 2
cen_y = (windowY-225) / 2
window.geometry('%dx%d+%d+%d' % (400,225, cen_x,cen_y))
window.iconbitmap(father_path+'\\guanji.ico')


window.configure(bg = "#FFFFFF")
window.title('')
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 225,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    200.0,
    14.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    # command=lambda: print("button_1 clicked"),
    command=lambda:set1(),
    relief="flat"
)




button_1.place(
    x=140.0,
    y=125.0,
    width=121.0,
    height=33.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    97.5,
    85.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=69.0,
    y=67.0,
    width=57.0,
    height=34.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    247.5,
    85.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=219.0,
    y=67.0,
    width=57.0,
    height=34.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    174.0,
    85.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    324.0,
    85.0,
    image=image_image_3
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    # command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=49.0,
    y=8.0,
    width=12.0,
    height=12.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: zuixiaohua(),
    relief="flat"
)
button_3.place(
    x=29.0,
    y=8.0,
    width=12.0,
    height=12.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: guanbi(),
    relief="flat"
)


button_4.place(
    x=9.0,
    y=8.0,
    width=12.0,
    height=12.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    200.0,
    199.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=6.0,
    y=180.0,
    width=388.0,
    height=36.0
)

#开始
folder = os.path.exists('关机.txt')
if not folder:  # 创建
    f1 = open('关机.txt', 'w')
    f1.write('time=3600')
    f1.close()
f2 = open('关机.txt', 'r')
t = int(f2.read().strip().split('time=')[-1])

entry_1.delete(0,END)
entry_1.insert(0, str(t // 3600))
entry_2.delete(0,END)
entry_2.insert(0, str(t % 3600 // 60))
def zuixiaohua():
    window.iconify()
def set1():
    try:
        x1 = int(entry_1.get())
    except:
        x1 = 0
    try:
        x2 = int(entry_2.get())
    except:
        x2 = 0

    y = x1 * 3600 + x2 * 60
    entry_3.delete(0,END)
    entry_3.insert(0, '%s秒后关机' % y)
    f1 = open('关机.txt', 'w')
    f1.write('time=%s' % y)
    f1.close()
def guanbi():
    global window
    window.destroy()
def check():
    while 1:
        try:
            x=int(entry_1.get())
        except:
            x=0
        try:
            y=int(entry_2.get())
        except:
            y=0


        # print(x,y)
        t1=entry_3.get()

        if t1=='':
            entry_3.delete(0, END)
            entry_3.insert(0, 'x秒后关机，by.柒夜')
        elif t1=='x秒后关机，by.柒夜':
            pass
        else:
            try:
                t2=int(entry_3.get().replace('秒后关机',''))
                if t2<=0:
                    # print('关机！！！')
                    os.system("shutdown -s -t 0 ")
                    return
                else:
                    t2-=1
                    entry_3.delete(0,END)
                    entry_3.insert(0,'%s秒后关机' % t2)
            except:
                entry_3.delete(0, END)
                entry_3.insert(0, 'xx秒后关机')
        time.sleep(1)
thread_1 = Thread(target=check)
thread_1.start()

# window.overrideredirect(1) #隐藏标题栏会出现无法移动的问题
window.attributes("-toolwindow", True)

window.resizable(False, False)
window.mainloop()
