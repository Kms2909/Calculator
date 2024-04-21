from tkinter import *


first_no=second_no=op=None

def get_digit(digit):
    current= result_label['text']
    new = current + str(digit)
    result_label.configure(text=new)
    
def clear():
    result_label.configure(text='')
    
def get_op(operator):
    global first_no,op
    first_no=int(result_label['text'])
    op=operator
    result_label.config(text='')
    
def get_result():
    global first_no,second_no,op
    second_no=int(result_label['text'])
    if op=='+':
        result_label.config(text=str(first_no+second_no))
    elif op=='-':
        result_label.config(text=str(first_no-second_no))
    elif op=='*':
        result_label.config(text=str(first_no*second_no))
    else:
        if second_no==0:
            result_label.configure(text='Error')
        else:
            result_label.config(text=str(round(first_no/second_no)))
root=Tk()
root.title('Calculator')
root.geometry('300x300')
root.resizable(0,0)
root.configure(background='grey')
result_label=Label(root,text='',bg='grey',fg='white')
result_label.grid(row=0,column=0,columnspan=5,sticky='w',pady=(10,15))
result_label.config(font=('verdana','30','bold'))

btn7=Button(root,text=7,fg='black',bg='grey',width=4,height=1,command=lambda:get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',20))

btn8=Button(root,text=8,fg='black',bg='grey',width=4,height=1,command=lambda:get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',20))

btn9=Button(root,text=9,fg='black',bg='grey',width=4,height=1,command=lambda:get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',20))

btndiv=Button(root,text='/',fg='black',bg='grey',width=4,height=1,command=lambda:get_op('/'))
btndiv.grid(row=1,column=3)
btndiv.config(font=('verdana',20))

btn4=Button(root,text=4,fg='black',bg='grey',width=4,height=1,command=lambda:get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',20))

btn5=Button(root,text=5,fg='black',bg='grey',width=4,height=1,command=lambda:get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',20))

btn6=Button(root,text=6,fg='black',bg='grey',width=4,height=1,command=lambda:get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',20))

btnmul=Button(root,text='*',fg='black',bg='grey',width=4,height=1,command=lambda:get_op('*'))
btnmul.grid(row=2,column=3)
btnmul.config(font=('verdana',20))

btn1=Button(root,text=1,fg='black',bg='grey',width=4,height=1,command=lambda:get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',20))

btn2=Button(root,text=2,fg='black',bg='grey',width=4,height=1,command=lambda:get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',20))

btn3=Button(root,text=3,fg='black',bg='grey',width=4,height=1,command=lambda:get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',20))

btnsub=Button(root,text='-',fg='black',bg='grey',width=4,height=1,command=lambda:get_op('-'))
btnsub.grid(row=3,column=3)
btnsub.config(font=('verdana',20))


btnclear=Button(root,text='C',fg='black',bg='grey',width=4,height=1,command=lambda:clear())
btnclear.grid(row=4,column=0)
btnclear.config(font=('verdana',20))

btn0=Button(root,text=0,fg='black',bg='grey',width=4,height=1,command=lambda:get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',20))

btnequal=Button(root,text='=',fg='black',bg='grey',width=4,height=1,command=get_result)
btnequal.grid(row=4,column=2)
btnequal.config(font=('verdana',20))

btnadd=Button(root,text='+',fg='black',bg='grey',width=4,height=1,command=lambda:get_op('+'))
btnadd.grid(row=4,column=3)
btnadd.config(font=('verdana',20))








root.mainloop()