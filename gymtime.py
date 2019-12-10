from tkinter import *
import winsound
import time
#create Tk window
root = Tk()
root.geometry('300x150')
#set name of window
root.title('Timer')

#initalise values from user (spinbox values)
item_1 = IntVar()
def set_act_time():
    item_1.get()

item_2 = IntVar()
def set_rst_time():
    item_2.get()
    
limit = IntVar()
def set_limit():
    limit.get()
    
#item 1 spinbox
var1 = StringVar(root)
item_1 = Spinbox(root, from_= 0, to = 59, width = 5, textvariable=var1)
item_1.grid(row = 1, column = 0)

var2 = StringVar(root)
item_2 = Spinbox(root, from_= 0, to = 59, width = 5, textvariable=var2)
item_2.grid(row = 2, column = 0)

var3 = StringVar(root)
limit = Spinbox(root, from_= 0, to = 599, width = 5, textvariable=var3)
limit.grid(row = 0, column = 0)

set_act_time = Button(root, text = 'Set active timer', width = 15, command = set_act_time).grid(row = 1, column = 1)
set_rst_time = Button(root, text = 'Set rest timer', width = 15, command = set_rst_time).grid(row = 2, column = 1)
set_limit = Button(root, text="Set loops", width = 15, command = set_limit).grid(row = 0, column = 1)

def gym_timer(frequency=2000, duration=1000, flag = True):
    act_time = item_1.get()
    rst_time = item_2.get()
    time_limit = limit.get()
    for i in range(int(time_limit)):
        winsound.Beep(frequency, duration)
        time.sleep(int(act_time))
        winsound.Beep(frequency, duration)
        time.sleep(int(rst_time))
        
def reset():
    var1.set("0")
    var2.set("0")
    var3.set("0")
start_btn = Button(root, text = 'start', width = 10, bg = 'green', command = gym_timer).grid(row = 3, column = 0)
stop_btn = Button(root, text = 'stop', width = 15, bg = 'yellow', command = reset).grid(row = 3, column = 1)
close_btn = Button(root, text = 'cancel', width = 20, bg = 'red', command = root.destroy).grid(row = 4, column = 0)
root.mainloop()