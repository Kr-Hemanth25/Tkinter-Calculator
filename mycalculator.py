import tkinter as tk
root=tk.Tk()
cal=""
def addcal(symbol):
    global cal
    cal+=str(symbol)
    text_res.delete(1.0,"end")
    text_res.insert(1.0,cal)
def evaluate():
    try:
       global cal
       resu=str(eval(cal))
       text_res.delete(1.0,"end")
       text_res.insert(1.0,resu)
    except:
        clearfield()
        text_res.insert(1.0,"error")

def clearfield():
    global cal
    cal=""
    text_res.delete(1.0,"end")


text_res=tk.Text(root,height=3,width=30,font=("bold",15))
text_res.grid(columnspan=4)
btn1=tk.Button(root,text="1",command=lambda:addcal("1"),width=5,font=("bold",10))
btn1.grid(row=2,column=0)
btn2=tk.Button(root,text="2",command=lambda:addcal("2"),width=5,font=("bold",10))
btn2.grid(row=2,column=1)
btn3=tk.Button(root,text="3",command=lambda:addcal("3"),width=5,font=("bold",10))
btn3.grid(row=2,column=2)
btn4=tk.Button(root,text="4",command=lambda:addcal("4"),width=5,font=("bold",10))
btn4.grid(row=3,column=0)
btn5=tk.Button(root,text="5",command=lambda:addcal("5"),width=5,font=("bold",10))
btn5.grid(row=3,column=1)
btn6=tk.Button(root,text="6",command=lambda:addcal("6"),width=5,font=("bold",10))
btn6.grid(row=3,column=2)
btn7=tk.Button(root,text="7",command=lambda:addcal("7"),width=5,font=("bold",10))
btn7.grid(row=4,column=0)
btn8=tk.Button(root,text="8",command=lambda:addcal("8"),width=5,font=("bold",10))
btn8.grid(row=4,column=1)
btn9=tk.Button(root,text="9",command=lambda:addcal("9"),width=5,font=("bold",10))
btn9.grid(row=4,column=2)
btn0=tk.Button(root,text="0",command=lambda:addcal("0"),width=5,font=("bold",10))
btn0.grid(row=5,column=1)
btnc=tk.Button(root,text="clear",command=lambda:clearfield(),width=10,font=("bold",10))
btnc.grid(row=6,column=1,columnspan=2)
btne=tk.Button(root,text="=",command=evaluate,width=10,font=("bold",10))
btne.grid(row=6,column=0,columnspan=2)
# btnba=tk.Button(root,text="bs",command=lambda:backspace,width=10,font=("bold",10))
# btnba.grid(row=6,column=2)
btno=tk.Button(root,text="(",command=lambda:addcal("("),width=5,font=("bold",10))
btno.grid(row=5,column=0)
btc1=tk.Button(root,text=")",command=lambda:addcal(")"),width=5,font=("bold",10))
btc1.grid(row=5,column=2)
btns=tk.Button(root,text="-",command=lambda:addcal("-"),width=5,font=("bold",10))
btns.grid(row=3,column=3)
btnmum=tk.Button(root,text="*",command=lambda:addcal("*"),width=5,font=("bold",10))
btnmum.grid(row=4,column=3)
btnd=tk.Button(root,text="/",command=lambda:addcal("/"),width=5,font=("bold",10))
btnd.grid(row=5,column=3)
btnadd=tk.Button(root,text="+",command=lambda:addcal("+"),width=5,font=("bold",10))
btnadd.grid(row=2,column=3)
root.maxsize()
root.mainloop()