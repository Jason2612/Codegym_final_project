import tkinter as tk
from PIL import ImageTk, Image


# class LoginForm:
#     def __init__(self,window):
#         self.window = window
#         self.window.title("Final Project")
#         self.window.geometry("560x450")
#         self.window.resizable(0,0)

#         # Ảnh nền
#         self.bg_frame = Image.open('C:\\Users\\Phong\\Desktop\\My Testing Project\\Final Project\\img\\1900851.png')
#         photo = ImageTk.PhotoImage(self.bg_frame)
#         self.bg_panel = tk.Label(self.window, image=photo)
#         self.bg_panel.image = photo
#         self.bg_panel.pack(fill='both', expand='yes')

#         # Login form frame
#         self.lgn_frame = tk.Frame(self.window, bg = "#F3F2F2", width='250', height='300', )
#         self.lgn_frame.place(x=160, y=70)

#         self.txt = 'Login'
#         self.heading = tk.Label(self.lgn_frame, text = self.txt, font=('yu gothic ui', 20, 'bold'), fg='black')
#         self.heading.place(x=85, y=5)

# def page():
#     window = tk.Tk()
#     LoginForm(window)
#     window.mainloop()

# page()

#Create an instance of tkinter frame or window
win= tk.Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
#Define a new function to open the window
def open_win():
   new= tk.Toplevel(win)
   new.geometry("750x250")
   new.title("New Window")
   #Create a Label in New window
   tk.Label(new, text="Hey, Howdy?", font=('Helvetica 17 bold')).pack(pady=30)
#Create a label
tk.Label(win, text= "Click the below button to Open a New Window", font= ('Helvetica 17 bold')).pack(pady=30)
#Create a button to open a New Window
tk.Button(win, text="Open", command=open_win).pack()
win.mainloop()