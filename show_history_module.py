
"""
* ds todo : để add các việc cần làm
* ds done : để khi người dùng hoàn thành có thể chuyển việc cần làm thành done
* sau khi set giờ và công việc
* thực hiện đếm ngược
* khi kết thúc sẽ hiện ra công việc đã hoàn thành + thời gian hoàn thành

"""

        

from tkinter import BOTH, Toplevel
import tkinter


def showHistory():
    new_window = Toplevel(window)
    new_window.geometry("750x250")
    new_window.title("History")
    history_listbox = tkinter.Listbox(
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
    history_listbox.pack(fill=BOTH)

    new_window.mainloop()