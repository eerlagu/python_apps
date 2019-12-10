import tkinter
import time
import winsound

window = tkinter.Tk()
window.title("gym timer")

def gym_timer(frequency, duration, act_time, rest_time):
    winsound.Beep(frequency, duration)
    time.sleep(act_time)
    winsound.Beep(frequency, duration)
    time.sleep(rest_time)

tkinter.Label(window, text = "Active time").pack() 
tkinter.Entry(window).pack() 

tkinter.Label(window, text = "Rest time").pack() 
tkinter.Entry(window).pack()

start_button = tkinter.Button(window, text='Start', width=10, bg="green", command=gym_timer(2000, 1000, 30, 10)).pack(side="right")
stop_button = tkinter.Button(window, text='Stop', width=10, bg="yellow", command=window.quit).pack(side="left")
close_button = tkinter.Button(window, text='Close', width=10, bg="red", command=window.destroy).pack(side="bottom")

window.mainloop()

'''r = tk.Tk() 
r.title('gymtime clock')

tk.Label(r, text = "Active time").grid(row = 0) # this is placed in 0 0
# 'Entry' is used to display the input-field
tk.Entry(r).grid(row = 0, column = 1) # this is placed in 0 1

tk.Label(r, text = "Rest time").grid(row = 1) # this is placed in 1 0
tk.Entry(r).grid(row = 1, column = 1) # this is placed in 1 1
 
start_button = tk.Button(r, text='Start', width=10, bg="green", command=r.destroy)
stop_button = tk.Button(r, text='Stop', width=10, bg="yellow", command=r.destroy)
close_button = tk.Button(r, text='Close', width=10, bg="red", command=r.destroy)
stop_button.pack(side = "right")
start_button.pack(side = "left")
close_button.pack(side="bottom") 
r.mainloop()'''