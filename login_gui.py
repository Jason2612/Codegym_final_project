
import tkinter as tk
from tkinter import ANCHOR, Place, font
from PIL import ImageTk, Image
import os


class LoginForm:
   def __init__(self,window_login):
        self.window = window_login
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
        self.lgn_frame = tk.Frame(
         self.window, 
         bg = "#F3F2F2", 
         width='250', 
         height='300'
         )
        self.lgn_frame.place(x=160, y=70)

        self.txt = 'Login'
        self.heading = tk.Label(
         self.lgn_frame, 
         text = self.txt, 
         font=('yu gothic ui', 20, 'bold'), 
         fg='black'
         )
        self.heading.place(x=85, y=5)

        self.username_frame = tk.Frame(self.lgn_frame)
        self.username_frame.place(x=15, y=90)

        self.username_text = 'Username'
        self.username_label = tk.Label(
         self.username_frame, 
         text= self.username_text, 
         font=('Arial' ,10), 
         fg='black'
         )
        self.username_label.pack(side=tk.LEFT)

        # Khung nhap username
        self.username_verify = tk.StringVar()
        self.username_input = tk.Entry(
         self.username_frame,
         textvariable=self.username_verify,
         width=15, 
         font=('Arial', 13), 
         fg='black'
         )
        self.username_input.pack(side=tk.RIGHT)

        self.password_frame = tk.Frame(self.lgn_frame)
        self.password_frame.place(x=17, y=130)

        self.password_text = 'Password'
        self.password_label = tk.Label(
         self.password_frame, 
         text= self.password_text, 
         font=('Arial' ,10), 
         fg='black'
         )
        self.password_label.pack(side=tk.LEFT)
        
        # Khung nhap password
        self.password_verify = tk.StringVar()
        self.password_input = tk.Entry(
         self.password_frame, 
         textvariable=self.password_verify, 
         width=15, 
         font=('Arial', 13), 
         fg='black',
         show='*'
         )
        self.password_input.pack(side=tk.RIGHT)

        # Button login and register
        self.login_btn_txt = 'Login'
        self.login_btn = tk.Button(
         self.lgn_frame, 
         text=self.login_btn_txt, 
         width=5, 
         font=('Arial', 10), 
         fg='black',
         command=self.login_verify
         )
        self.login_btn.place(x=50, y=200)

        self.register_btn_txt = 'register'
        self.register_btn = tk.Button(
         self.lgn_frame, 
         text=self.register_btn_txt, 
         width=5, 
         font=('Arial', 10), 
         fg='black', 
         command=self.register_window
         )
        self.register_btn.place(x=150, y=200)

   
   # Ham hien thi cua so dang ki tai khoan
   def register_window(self):
      self.window_regs = tk.Toplevel(self.window)
      self.window_regs.geometry("400x300+200+200")
      self.window_regs.title("Register")

      self.username = tk.StringVar()
      self.password = tk.StringVar()

      label = tk.Label(
         self.window_regs, 
         text='Please fill in your info', 
         bg='#73C6B6', 
         fg='black',
         font=('Arial', 15)
         )
      label.pack(pady=20)

      username_lable = tk.Label(
         self.window_regs, 
         text="Username * ", 
         font=('Arial', 13)
         )
      username_lable.pack()

      self.username_entry = tk.Entry(
         self.window_regs, 
         textvariable=self.username,
         font=('Arial', 12)
         )
      self.username_entry.pack()

      password_lable = tk.Label(
         self.window_regs, 
         text="Password * ", 
         font=('Arial', 13)
         )
      password_lable.pack()

      self.password_entry = tk.Entry(
         self.window_regs, 
         textvariable=self.password,
         font=('Arial', 12)
         )
      self.password_entry.pack()

      tk.Button(
         self.window_regs, 
         text="Register", 
         width=10, 
         height=1, 
         bg='#73C6B6', 
         command=self.register_user
         ).pack(pady=5)

   # Ham dang ki tai khoan
   def register_user(self):
 
      username_info = self.username.get()
      password_info = self.password.get()
   
      file = open(username_info, "w")
   
      file.write(username_info + "\n")
      file.write(password_info)
      file.close()
   
      self.username_entry.delete(0, tk.END)
      self.password_entry.delete(0, tk.END)

      # Thong bao da dang ki thanh cong
      tk.Label(self.window_regs, 
      text="Registration Success", 
      fg="green", 
      font=("calibri", 11)
      ).pack()
   
   def login_verify(self):
      username_check = self.username_verify.get()
      password_check = self.password_verify.get()

      self.username_input.delete(0, tk.END)
      self.password_input.delete(0, tk.END)

      list_of_files = os.listdir()

      if username_check in list_of_files:
         file_check = open(username_check, "r")
         verify = file_check.read().splitlines()
         if password_check == verify[1]:
            self.login_success()
         else:
            self.wrong_password()
      else:
         self.user_not_found()
   
   def login_success(self):
      self.login_success_window = tk.Toplevel(self.window)
      self.login_success_window.title("Success")
      self.login_success_window.geometry("200x200+200+200")
      tk.Label(self.login_success_window, text="Login Success").pack()
      tk.Button(self.login_success_window, text="OK", command=self.delete_login_success_window).pack(pady=10)
   
   def delete_login_success_window(self):
      self.login_success_window.destroy()
      self.window.destroy()
      import main

   def wrong_password(self):
      self.wrong_password_window = tk.Toplevel(self.window)
      self.wrong_password_window.title("Success")
      self.wrong_password_window.geometry("200x200+200+200")
      tk.Label(self.wrong_password_window, text="Invalid Password ").pack()
      tk.Button(self.wrong_password_window, text="OK", command=self.delete_wrong_password_window).pack(pady=10)

   def delete_wrong_password_window(self):
      self.wrong_password_window.destroy()

   def user_not_found(self):
      self.user_not_found_window = tk.Toplevel(self.window)
      self.user_not_found_window.title("Success")
      self.user_not_found_window.geometry("200x200+200+200")
      tk.Label(self.user_not_found_window, text="User Not Found").pack()
      tk.Button(self.user_not_found_window, text="OK", command=self.delete_user_not_found_window).pack(pady=10)
   
   def delete_user_not_found_window(self):
      self.user_not_found_window.destroy()
   

def page():
    window_login = tk.Tk()
    LoginForm(window_login)
    window_login.mainloop()

page()
