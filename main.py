import tkinter as tk
from tkinter import ANCHOR, LEFT, messagebox
import time
import datetime
import show_history_module

def newTask():
    task = my_entry.get()
    if task != "":
        task_lb.insert(tk.END, task)
        my_entry.delete(0,'end')
    else:
        messagebox.showwarning("warning", "Please enter some task")

def doneTask():
    task = task_lb.get(ANCHOR)
    if task != "":
        done_lb.insert(tk.END, task)
        task_lb.delete(ANCHOR)
    else:
        messagebox.showwarning("warning", "please choose one item")

def deleteTask():
    task_lb.delete(ANCHOR)

def countdown():
        total_seconds = int(entry_hour.get()) * 3600 + int(entry_min.get()) * 60 + int(entry_second.get())
        while total_seconds >= 0:
            minute,second = (total_seconds//60, total_seconds % 60)
            hour = 0
            if minute > 60:
                hour , minute = (minute // 60, minute % 60)

            
            mins.set(minute)
            hrs.set(hour)
            sec.set(second)

            time_display_frame.update()
            time.sleep(1)
            
            if total_seconds == 0:
                hrs.set('00')
                mins.set('00')
                sec.set('00')
            total_seconds -= 1

def reset_time():
    hrs.set('00')
    mins.set('00')
    sec.set('00')

def showHistory():
    history = []
    for i in history:
        history.insert(tk.END, i)
        
    new_window = tk.Toplevel(window)
    new_window.geometry("750x250")
    new_window.title("History")
    history_listbox = tk.Listbox(
        new_window,
        width=50,
        height=25,
        font=('Times',12),
        bd=0,
        fg='#464646',
        highlightthickness=1,
        selectbackground='#a6a6a6',
        activestyle='none',
    )
    history_listbox.pack(fill=tk.BOTH)

    new_window.mainloop()

# Khoi tao giao dien
window = tk.Tk()
window.geometry('500x450+500+200')
window.title('To Do List')
window.config(bg='#223441')
window.resizable(width=False, height=False)

# Heading label
heading_label = tk.Label(
    window,
    text="Working Bae",
    font=("times", 20),
    bg="#AEB6BF"
)
heading_label.pack(side=tk.TOP, fill=tk.BOTH)

# Khoi tao dong ho dem nguoc
time_display_frame=tk.Frame(window)
time_display_frame.place(x=127, y=60)

# Hien thi dong ho dem nguoc
hrs=tk.StringVar()
tk.Entry(time_display_frame, textvariable=hrs, width=2, font='arial 50').grid(row=3, column=1,pady=10)
hrs.set('00')

mins = tk.StringVar()
tk.Entry(time_display_frame, textvariable=mins, width=2, font='arial 50').grid(row=3,column=2,pady=10)
mins.set('00')

sec = tk.StringVar()
tk.Entry(time_display_frame, textvariable=sec, width=2, font="arial 50").grid(row=3,column=3,pady=10)
sec.set('00')

# Frame cho entry dien thoi gian
entry_time_frame = tk.Frame(window)
entry_time_frame.place(x=290, y=210)

# Entry dien thoi gian cho dong ho dem nguoc
entry_hour = tk.Entry(entry_time_frame, width=3, font=("arial 15"))
entry_min = tk.Entry(entry_time_frame, width=3, font=("arial 15"))
entry_second = tk.Entry(entry_time_frame, width=3, font=("arial 15"))
entry_hour.grid(row=1, column=1)
entry_min.grid(row=1,column=2)
entry_second.grid(row=1,column=3)

# Nut start
set_time_btn = tk.Button(entry_time_frame, width=3, text="Start", font=("arial 12"), command=countdown)
set_time_btn.grid(row=1, column=4)

# Nut reset
# reset_time_btn = tk.Button(time_display_frame, width=3, text="Reset", font=("arial 14"), command=reset_time)
# reset_time_btn.grid(row=0, column=1)

# Khoi tao frame cho list box
frame_task_lb = tk.Frame(window)
frame_task_lb.place(x=50, y=250)

# label task list
task_label = tk.Label(
    frame_task_lb,
    text="Tasks",
    font=("times", 12),
    bg="#AEB6BF"
)
task_label.pack(side=tk.TOP, fill=tk.BOTH)

# Task list list box
task_lb = tk.Listbox(
    frame_task_lb,
    width=25,
    height=12,
    font=('Times',10),
    bd=0,
    fg='#464646',
    highlightthickness=1,
    selectbackground='#a6a6a6',
    activestyle='none',
)
task_lb.pack(side=tk.LEFT, fill=tk.BOTH)

# Khoi tao frame cho done list
frame_done_lb = tk.Frame(window)
frame_done_lb.place(x=290, y=250)

# label done list
done_label = tk.Label(
    frame_done_lb,
    text="Done",
    font=("times", 12),
    bg="#AEB6BF"
)
done_label.pack(side=tk.TOP, fill=tk.BOTH)

# Done list list box
done_lb = tk.Listbox(
    frame_done_lb,
    width=25,
    height=12,
    font=('Times',10),
    bd=0,
    fg='#464646',
    highlightthickness=1,
    selectbackground='#a6a6a6',
    activestyle='none'
)
done_lb.pack(side=tk.LEFT, fill=tk.BOTH)


# Task list 
task_list = []
for item in task_list:
    task_lb.insert(tk.END, item)

# Done list
done_list = []
for item in done_list:
    done_lb.insert(tk.END, item)


# Thanh keo cho task lb
sb_task = tk.Scrollbar(frame_task_lb)
sb_task.pack(side=tk.RIGHT, fill=tk.BOTH)
task_lb.config(yscrollcommand=sb_task.set)
sb_task.config(command=task_lb.yview)

# Thanh keo cho done lb
sb_done = tk.Scrollbar(frame_done_lb)
sb_done.pack(side=tk.RIGHT, fill=tk.BOTH)
done_lb.config(yscrollcommand=sb_done.set)
sb_done.config(command=done_lb.yview)

# Entry nhap task
my_entry = tk.Entry(
    window,
    font=('times', 15),
    width=11
)
my_entry.place(x=50, y=210)

# Frame cho button add va del
button_frame = tk.Frame(window)
button_frame.place(x=157, y=210)

addTask_btn = tk.Button(
    button_frame,
    text='Add',
    font=('times',10),
    bg='#c5f776',
    command=newTask
)
addTask_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

delTask_btn = tk.Button(
    button_frame,
    text='Del',
    font=('times',10),
    bg='#ff8b61',
    command=deleteTask
)
delTask_btn.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

# Nut done task
done_task_btn = tk.Button(
    window,
    text="=>",
    bg="#58D68D",
    font=(15),
    command=doneTask
)
done_task_btn.place(x=240, y=320)



window.mainloop()


