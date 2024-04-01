import customtkinter as ctk
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

def register():
    app.destroy()
    register = ctk.CTk()
    register.geometry("400x200")
    register.mainloop()

def dashboard():
    app.destroy()
    dashboard = ctk.CTk()
    dashboard.geometry("800x600")
    dashboard.mainloop()

def login():
    username = username_entry.get()
    client.send(username.encode())
    message = client.recv(1024).decode()
    mensagem.configure(text=message)
    
    password = password_entry.get()
    client.send(password.encode())
    message = client.recv(1024).decode()
    mensagem.configure(text=message)

    response = client.recv(1024).decode()
    mensagem.configure(text=response)
    
    if response == "Login Bem-Sucedido":
        dashboard()
        
    else: 
        register()
        

def visual():
    
    
    global app
        
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = ctk.CTk()
    app.geometry("600x400")
    
    global mensagem
    mensagem = ctk.CTkLabel(app, text="", font=("Roboto",24))
    mensagem.pack()

    global username_entry
    username_entry = ctk.CTkEntry(app, placeholder_text="Digite seu username")
    username_entry.pack()
    
    global password_entry
    password_entry = ctk.CTkEntry(app, placeholder_text="Digite Sua Senha", show="*")
    password_entry.pack()
    
    login_btn = ctk.CTkButton(app, text="Login", command=login)
    login_btn.pack()
    
    app.mainloop()

visual()
