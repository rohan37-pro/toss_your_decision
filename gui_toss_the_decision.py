import pandas
import random
from matplotlib import pyplot as plt
from tkinter import *

lis1=[]
toss_history = []

def dictionary():
    global disvalue
    global dis
    dis = {}
    disvalue = []
    for i in lis1:
        a = toss_history.count(i)
        dis[i] = a
        disvalue.append(a)
    


def his_tab():
    dictionary()
    xyz = {'     parameter  ':lis1,'     number of outcome':disvalue}
    tabl = pandas.DataFrame(xyz)
    type(tabl)
    roota = Tk()
    labela = Label(roota,text=str(tabl))
    labela.pack()


    roota.mainloop()
    

def clear_his():
    toss_history.clear()
    dis.clear()

def toss_once():
    num_para = len(lis1)
    ran_num = random.randint(0,num_para-1)
    toss_history.append(lis1[ran_num])
    print(lis1[ran_num])
    

def toss():
    num_para = len(lis1)
    for i in range(int(entry1.get())):
        ran_num = random.randint(0,num_para-1)
        toss_history.append(lis1[ran_num])
    print(toss_history)
    
def history():
    print(toss_history)
    root_his = Tk()
    labelhis = Label(root_his,text=str(toss_history))
    labelhis.pack()

    
    root_his.mainloop()

def bar_graph():
    dictionary()
    for i in lis1:
        plt.bar(i,dis[i])
    plt.xlabel('parameter')
    plt.ylabel('number of outcome')
    plt.title('toss bargraph')
    plt.show()
    
def pie_chart():
    dictionary()
    plt.pie(disvalue,labels=lis1,wedgeprops={'edgecolor':'black'},shadow = True,
            autopct='%1.1f%%')
    plt.title('toss pie chart')
    
    plt.show()

def total_toss():
    roots = Tk()
    labels = Label(roots,
                   text='total number of toss    :  '+str(len(toss_history)))
    labels.pack()
    
    roots.mainloop()

def percent_tab():
    dictionary()
    per = []
    total_toss = len(toss_history)
    if total_toss != 0:
        for i in lis1:
            per.append(dis[i]*100/total_toss)
    else:
        for i in lis1:
            per.append(0)
    
    xyz = {'   parameter   /':lis1,'    percentage':per}
    tebl = pandas.DataFrame(xyz)
    
    rootb = Tk()

    labels = Label(rootb,text=str(tebl))
    labels.pack()
    
    rootb.mainloop()
    
 
def done():
    global entry1
    
    if entry.get() =='':
        pass
    else:
        lis1.append(entry.get())
        
    root2 = Tk()
    button3 = Button(root2,text='toss once',command=toss_once)
    button3.grid(row=0,column=0)
    entry1 = Entry(root2)
    entry1.grid(row=1,column=0)
    button4 = Button(root2,text='toss multiple times',command=toss)
    button4.grid(row=1,column=1)
    button5 = Button(root2,text='history',command=history)
    button5.grid(row=2,column=0)
    button6 = Button(root2,text='history table',command=his_tab)
    button6.grid(row=2,column=1)
    button7 = Button(root2,text='clear history',command=clear_his)
    button7.grid(row=2,column=2)
    button8 = Button(root2,text='show bar graph',command=bar_graph)
    button8.grid(row=2,column=3)
    button9 = Button(root2,text='show pie chart',command=pie_chart)
    button9.grid(row=3,column=0)
    button10 = Button(root2,text='number of total toss',command=total_toss)
    button10.grid(row=3,column=1)
    button11 = Button(root2,text='percentage table',command=percent_tab)
    button11.grid(row=3,column=2)
    
                      
    root2.mainloop()


def more():
    global entry
    global a
    if entry.get() == '':
        pass
    else:
        lis1.append(entry.get())
    print(lis1)
    entry = Entry(root)
    entry.grid(row=a,column=0)
    button = Button(root,text='enter more parameter',command=more)
    button.grid(row=a,column=1)
    button2 = Button(root,text='done',command=done)
    button2.grid(row=a,column=2)
    a+=1
    



root = Tk()
a=1
label = Label(root,text='enter your parameters to toss')
label.grid(row=0,column=0)
entry = Entry(root)
entry.grid(row=a,column=0)
button = Button(root,text='enter more parameter',command=more)
button.grid(row=a,column=1)
button2 = Button(root,text='done',command=done)
button2.grid(row=a,column=2)
a+=1

root.mainloop()
