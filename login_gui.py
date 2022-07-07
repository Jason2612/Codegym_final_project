import tkinter as tk
from PIL import ImageTk, Image


class LoginForm:
    def __init__(self,window):
        self.window = window
        self.window.title("Final Project")
        self.window.geometry("560x450")
        self.window.resizable(0,0)

        # Ảnh nền
        self.bg_frame = Image.open('C:\\Users\\Phong\\Desktop\\My Testing Project\\Final Project\\img\\1900851.png')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = tk.Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # Login form frame
        self.lgn_frame = tk.Frame(self.window, bg = "#F3F2F2", width='250', height='300', )
        self.lgn_frame.place(x=160, y=70)

        self.txt = 'Login'
        self.heading = tk.Label(self.lgn_frame, text = self.txt, font=('yu gothic ui', 20, 'bold'), fg='black')
        self.heading.place(x=85, y=5)

def page():
    window = tk.Tk()
    LoginForm(window)
    window.mainloop()

page()