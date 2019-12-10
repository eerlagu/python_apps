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
