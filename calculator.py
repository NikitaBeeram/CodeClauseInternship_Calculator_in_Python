from tkinter import *
import math
root=Tk()
root.title("Scientific Calculator")
root.resizable(width=False, height=False)
root.geometry("520x407+200+100")
e = Frame(root)

e=Entry(root,width=42,borderwidth=5,font=('Cambria',16,'bold'),bd=7,justify='right',fg="white",bg="grey")
e.grid(row=0,column=0,columnspan=4,pady=10)

def value(num):
    current =e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))
def clear():
    e.delete(0,END)
def add():
    global f_num
    f_num = e.get()
    global operation
    operation="add"
    e.delete(0,END)
def sub():
    global f_num
    f_num = e.get()
    global operation
    operation="sub"
    e.delete(0,END)
def mul():
    global f_num
    f_num = e.get()
    global operation
    operation="mul"
    e.delete(0,END)
def div():
    global f_num
    f_num = e.get()
    global operation
    operation="div"
    e.delete(0,END)
def cos():
    res = math.cos(math.radians(float(e.get())))
    e.delete(0,END)
    e.insert(0,res)
def sin():
    res = math.sin(math.radians(float(e.get())))
    e.delete(0,END)
    e.insert(0,res)
def tan():
    res = math.tan(math.radians(float(e.get())))
    e.delete(0,END)
    e.insert(0,res)
def pi():
    e.delete(0,END)
    res = math.pi
    e.insert(0,res)
def cosh():
    res = math.cosh(math.radians(float(e.get())))
    e.delete(0,END)
    e.insert(0,res)
def sinh():
    res = math.sinh(math.radians(float(e.get())))
    e.delete(0,END)
    e.insert(0,res)
def tanh():
    res = math.tanh(math.radians(float(e.get())))
    e.delete(0,END)
    e.insert(0,res)
def squareroot():
    res = math.sqrt(float(e.get()),1/2)
    e.delete(0,END)
    e.insert(0,res)
def cuberoot():
    res = math.pow(float(e.get()),1/10)
    e.delete(0,END)
    e.insert(0,res)
def delete():
    num=e.get()[:-1]
    e.delete(0,END)
    e.insert(0,num)
def pm():
    num = e.get()
    e.delete(0,END)
    e.insert(0,-(float(num)))
def CE():
    e.delete(0,END)
    e.insert(0,0)
def log():
    res = math.log(float(e.get()))
    e.delete(0,END)
    e.insert(0,res)
def log10():
    res = math.log10(float(e.get()))
    e.delete(0,END)
    e.insert(0,res)
def log2():
    res = math.log2(float(e.get()))
    e.delete(0,END)
    e.insert(0,res)
def e_val():
    e.delete(0,END)
    e.insert(0,math.e)
def exp():
    res = math.exp(float(e.get()))
    e.delete(0,END)
    e.insert(0,res)
def deg():
    res = math.degrees(float(e.get()))
    e.delete(0,END)
    e.insert(0,res)
def mod():
    global f_num 
    f_num = float(e.get())
    global operation
    operation = "mod"
    e.delete(0,END)
def lgamma():
    res = math.lgamma(float(e.get()))
    e.delete(0,END)
    e.insert(0,res)
def byx():
    res = 1.0/float(e.get())
    e.delete(0,END)
    e.insert(0,res)
def absolute():
    res = abs(float(e.get()))
    e.delete(0,END)
    e.insert(0,res)
def factorial():
    num = float(e.get())
    if(not num.is_integer()):
        print("not an integer")
        return
    
    res = math.factorial(int(num))
    e.delete(0,END)
    e.insert(0,res)

def equal():
    s_num=e.get()                 
    e.delete(0,END)
    if(operation=="add"):
        e.insert(0,float(f_num)+float(s_num))
    if(operation=="sub"):
        e.insert(0,float(f_num)-float(s_num))
    if(operation=="mul"):
        e.insert(0,float(f_num)*float(s_num))
    if(operation=="div"):
        e.insert(0,float(f_num)/float(s_num))
    if(operation=="mod"):
        e.insert(0,float(f_num)%float(s_num))

button_1 = Button(root,text="1",command=lambda: value(1),bg="grey",fg="white",width=10,height=2,font=('Cambria',16,'bold'))
button_2 = Button(root,text="2",command=lambda: value(2),bg="grey",fg="white",width=10,height=2,font=('Cambria',16,'bold'))
button_3 = Button(root,text="3",command=lambda: value(3),bg="grey",fg="white",width=10,height=2,font=('Cambria',16,'bold'))
button_4 = Button(root,text="4",command=lambda: value(4),bg="grey",fg="white",width=10,height=2,font=('Cambria',16,'bold'))
button_5 = Button(root,text="5",command=lambda: value(5),bg="grey",fg="white",width=10,height=2,font=('Cambria',16,'bold'))
button_6 = Button(root,text="6",command=lambda: value(6),bg="grey",fg="white",width=10,height=2,font=('Cambria',16,'bold'))
button_7 = Button(root,text="7",command=lambda: value(7),bg="grey",fg="white",width=10,height=2,font=('Cambria',16,'bold'))
button_8 = Button(root,text="8",command=lambda: value(8),bg="grey",fg="white",width=10,height=2,font=('Cambria',16,'bold'))
button_9 = Button(root,text="9",command=lambda: value(9),bg="grey",fg="white",width=10,height=2,font=('Cambria',16,'bold'))
button_0 = Button(root,text="0",command=lambda: value(0),bg="grey",fg="white",width=10,height=2,font=('Cambria',16,'bold'))
button_dot = Button(root,text=".",command=lambda: value("."),width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_clear = Button(root,text="Clear",command=clear,width=10,height=2,bg="light blue",font=('Cambria',16,'bold'))
button_CE = Button(root,text="CE",command=CE,width=10,height=2,bg="light blue",font=('Cambria',16,'bold'))
button_del=Button(root,text="DEL",command=delete,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_add = Button(root,text="+",command=add,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_equal = Button(root,text="=",command=equal,width=10,height=2,bg="red",fg="white",font=('Cambria',16,'bold'))
button_sub = Button(root,text="-",command=sub,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_mul = Button(root,text="*",command=mul,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_div = Button(root,text="/",command=div,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_pm = Button(root,text=chr(177),command=pm,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_squareroot = Button(root,text="\u221A",command=squareroot,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_cos = Button(root,text="cos",command=cos,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_sin = Button(root,text="sin",command=sin,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_tan = Button(root,text="tan",command=tan,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_cuberoot = Button(root,text="\u221B",command=cuberoot,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_pi = Button(root,text="pi",command=pi,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_cosh = Button(root,text="cosh",command=cosh,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_sinh = Button(root,text="sinh",command=sinh,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_tanh = Button(root,text="tanh",command=tanh,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_log = Button(root,text="log",command=log,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_log10 = Button(root,text="log10",command=log10,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_log2 = Button(root,text="log2",command=log2,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_e = Button(root,text="e",command=e_val,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_exp = Button(root,text="exp",command=exp,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_gamma = Button(root,text="gamma",command=lgamma,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_1byx = Button(root,text="1/x",command=byx,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_deg = Button(root,text="deg",command=deg,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_mod = Button(root,text="mod",command=mod,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_abs = Button(root,text="|x|",command=absolute,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))
button_factorial = Button(root,text="x!",command=factorial,width=10,height=2,bg="blue",fg="white",font=('Cambria',16,'bold'))

button_1.grid(row=2,column=0)
button_2.grid(row=2,column=1)
button_3.grid(row=2,column=2)
button_add.grid(row=1,column=3)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_sub.grid(row=2,column=3)
button_7.grid(row=4,column=0)
button_8.grid(row=4,column=1)
button_9.grid(row=4,column=2)
button_mul.grid(row=3,column=3)
button_0.grid(row=5,column=0)
button_dot.grid(row=5,column=1)
button_div.grid(row=4,column=3)
button_equal.grid(row=5,column=3)
button_clear.grid(row=1,column=0)
button_CE.grid(row=1,column=1)
button_pm.grid(row=5,column=2)
button_del.grid(row=1,column=2)
button_squareroot.grid(row=1,column=4)
button_cos.grid(row=1,column=5)
button_sin.grid(row=1,column=6)
button_tan.grid(row=1,column=7)
button_cuberoot.grid(row=2,column=4)
button_cosh.grid(row=2,column=5)
button_sinh.grid(row=2,column=6)
button_tanh.grid(row=2,column=7)
button_pi.grid(row=3,column=4)
button_log.grid(row=3,column=5)
button_log10.grid(row=3,column=6)
button_log2.grid(row=3,column=7)
button_e.grid(row=4,column=4)
button_exp.grid(row=4,column=5)
button_gamma.grid(row=4,column=6)
button_1byx.grid(row=4,column=7)
button_deg.grid(row=5,column=4)
button_mod.grid(row=5,column=5)
button_abs.grid(row=5,column=6)
button_factorial.grid(row=5,column=7)

def Standard():
    root.resizable(width=False,height=False)
    root.geometry("520x407+0+0")
def Scientific():
    root.resizable(width=False,height=False)
    root.geometry("1041x407+0+0")
def mexit():
    return
menubar = Menu(root)
Filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=Filemenu)
Filemenu.add_command(label="Standard",command=Standard)
Filemenu.add_command(label="Scientific",command=Scientific)
Filemenu.add_separator()
Filemenu.add_command(label="Exit",command=mexit)

root.config(menu=menubar)
root.mainloop()