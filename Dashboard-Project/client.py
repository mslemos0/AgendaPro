import customtkinter as ctk
import socket
import sqlite3
from tkinter import *
from tkinter import messagebox
import hashlib

# Conectar ao servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('userdata.db')
cursor = conn.cursor()

def back_login2():
    pass_fg.destroy()
    visual()
    

def pass_fg_window():
    global pass_fg
    pass_fg = ctk.CTk()
    pass_fg.geometry("500x360")
    pass_fg.config(bg='#001220')
    pass_fg.title("Login")
    pass_fg.maxsize(500,360)
    
    def busca_usuario():
        username = seu_usuario.get()
        password = sua_senha_entry.get()
        
        # Verificar se os campos estão preenchidos
        if username != '' and password != '':
            # Verificar se o usuário já existe
            cursor.execute('SELECT username FROM userdata WHERE username =?', [username])
            if cursor.fetchone() is not None:
                hash_pass = hashlib.sha256(password.encode()).hexdigest()
                cursor.execute('UPDATE userdata SET password =? WHERE username =?', [hash_pass,username])
                conn.commit()
                messagebox.showinfo('Sua senha foi alterada com sucesso!')

                
         
    font1 = ('Helvetica', 25, 'bold')
    font2 = ('Arial', 17, 'bold')
    font3 = ('Arial', 13, 'bold')
    font4 = ('Arial', 13, 'bold', 'underline')
    
    image1 = PhotoImage(file="C:/Users/6123182/OneDrive - Thomson Reuters Incorporated/Desktop/Dashboard-Project/200x200.png")
    image1_label = Label(pass_fg, image=image1, bg='#001220')
    image1_label.place(x=0,y=50)
    image2 = PhotoImage(file="C:/Users/6123182/OneDrive - Thomson Reuters Incorporated/Desktop/Dashboard-Project/pngwing.com (4).png")
    image2_label = Label(pass_fg, image=image2, bg="#001220")
    image2_label.place(x=-175,y=0)
    
    # Elementos da interface de usuário
    seu_email_label = ctk.CTkLabel(pass_fg, text="Bem-Vindo", font=font1, bg_color="#121111")
    seu_email_label.place(x=230,y=20)
    seu_usuario = ctk.CTkEntry(pass_fg, placeholder_text="Usuário", font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3,placeholder_text_color='#a3a3a3', width=200,height=50)
    seu_usuario.place(x=200,y=80)
    sua_senha_entry = ctk.CTkEntry(pass_fg, placeholder_text="Senha", font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3,placeholder_text_color='#a3a3a3', width=200,height=50, show="*")
    sua_senha_entry.place(x=200,y=150)
    
    login_btn = ctk.CTkButton(pass_fg,font=font2,text_color='#fff', fg_color='#00965d',hover_color='#006e44', bg_color='#001220', cursor='hand2', corner_radius=5,width=120,text="Login", command=busca_usuario)
    login_btn.place(x=200,y=220)
    back_btn = ctk.CTkButton(pass_fg,font=font2,text_color='#fff', fg_color='#00965d',hover_color='#006e44', bg_color='#001220', cursor='hand2', corner_radius=5,width=120,text="Voltar", command=back_login2)
    back_btn.place(x=200,y=255)
    
    
    
    pass_fg.mainloop()
    
def pass_forgot():
    app.destroy()
    pass_fg_window()

def back_login():
    sign_up_window.destroy()
    visual()
    
def visual():
    global app
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = ctk.CTk()
    app.geometry("500x360")
    app.config(bg='#001220')
    app.title("Login")
    app.maxsize(500,360)
    
    font1 = ('Helvetica', 25, 'bold')
    font2 = ('Arial', 17, 'bold')
    font3 = ('Arial', 13, 'bold')
    font4 = ('Arial', 13, 'bold', 'underline')
    
    frame1 = ctk.CTkFrame(app, bg_color='#001220', fg_color='#001220', width=470,height=360)
    frame1.place(x=0,y=0)
    
    image1 = PhotoImage(file="C:/Users/6123182/OneDrive - Thomson Reuters Incorporated/Desktop/Dashboard-Project/200x200.png")
    image1_label = Label(app, image=image1, bg='#001220')
    image1_label.place(x=0,y=50)
    image2 = PhotoImage(file="C:/Users/6123182/OneDrive - Thomson Reuters Incorporated/Desktop/Dashboard-Project/pngwing.com (4).png")
    image2_label = Label(app, image=image2, bg="#001220")
    image2_label.place(x=-175,y=0)
    
    signup_label = ctk.CTkLabel(app, font=font1,text='Bem-Vindo!', text_color='#fff', bg_color='#001220')
    signup_label.place(x=230,y=20)
    
    
    global mensagem
    mensagem = ctk.CTkLabel(frame1, text="", font=("Roboto",24))
    mensagem.pack()

    global username_entry
    username_entry = ctk.CTkEntry(app, placeholder_text="Usuário", font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3,placeholder_text_color='#a3a3a3', width=200,height=50)
    username_entry.place(x=200,y=80)
    
    global password_entry
    password_entry = ctk.CTkEntry(app, placeholder_text="Senha", font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3,placeholder_text_color='#a3a3a3', width=200,height=50, show="*")
    password_entry.place(x=200,y=150)
    
    criar_conta_btn = ctk.CTkButton(app, text="Clique Aqui", command=sign_up, font=font4, text_color='#00bf77', fg_color='#012220',cursor='hand2', width=40 )
    criar_conta_btn.place(x=345,y=250)
    
    criar_conta_label = ctk.CTkLabel(app,font=font3, text='Não possui uma conta?', text_color='#fff', bg_color='#001220')
    criar_conta_label.place(x=200,y=250)
    
    login_btn = ctk.CTkButton(app,font=font2,text_color='#fff', fg_color='#00965d',hover_color='006e44', bg_color='#001220', cursor='hand2', corner_radius=5,width=120,text="Login", command=login)
    login_btn.place(x=200,y=220)
    
    forgot_pass_label = ctk.CTkButton(app, font=font2, text='Esqueceu a senha?', text_color='#fff', fg_color='#00965d',hover_color='006e44', bg_color='#001220', cursor='hand2', corner_radius=5, command=pass_forgot)
    forgot_pass_label.place(x=325,y=220)
    
    app.mainloop()

# Função para criar uma nova conta de usuário
def sign_up():
    app.destroy()
    global sign_up_window
    sign_up_window = ctk.CTk()
    sign_up_window.geometry("500x360")
    sign_up_window.config(bg='#001220')
    sign_up_window.title("Crie sua Conta!")
    sign_up_window.maxsize(450,360)
    
    # Função para criar uma nova conta de usuário
    def criar_conta():
        # Obter os dados do formulário
        username = seu_email_entry.get()
        password = sua_senha_entry.get()
        
        # Verificar se os campos estão preenchidos
        if username != '' and password != '':
            # Verificar se o usuário já existe
            cursor.execute('SELECT username FROM userdata WHERE username =?', [username])
            if cursor.fetchone() is not None:
                messagebox.showerror('Erro', 'Usuário já existe')
            else:
                # Criptografar a senha
                hash_pass = hashlib.sha256(password.encode()).hexdigest()
                
                # Inserir novo usuário no banco de dados
                cursor.execute('INSERT INTO userdata (username, password) VALUES (?, ?)', [username, hash_pass])
                conn.commit()
                messagebox.showinfo('Sucesso', 'Sua conta foi criada com sucesso!')
                
     
    font1 = ('Helvetica', 25, 'bold')
    font2 = ('Arial', 17, 'bold')
    font3 = ('Arial', 13, 'bold')
    font4 = ('Arial', 13, 'bold', 'underline')
    
    image1 = PhotoImage(file="C:/Users/6123182/OneDrive - Thomson Reuters Incorporated/Desktop/Dashboard-Project/200x200.png")
    image1_label = Label(sign_up_window, image=image1, bg='#001220')
    image1_label.place(x=0,y=50)
    image2 = PhotoImage(file="C:/Users/6123182/OneDrive - Thomson Reuters Incorporated/Desktop/Dashboard-Project/pngwing.com (4).png")
    image2_label = Label(sign_up_window, image=image2, bg="#001220")
    image2_label.place(x=-175,y=0)
    
    # Elementos da interface de usuário
    seu_email_label = ctk.CTkLabel(sign_up_window, text="Bem-Vindo", font=font1, bg_color="#121111")
    seu_email_label.place(x=230,y=20)
    seu_email_entry = ctk.CTkEntry(sign_up_window, placeholder_text="Usuário", font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3,placeholder_text_color='#a3a3a3', width=200,height=50)
    seu_email_entry.place(x=200,y=80)
    sua_senha_entry = ctk.CTkEntry(sign_up_window, placeholder_text="Senha", font=font2, text_color='#fff', fg_color='#001a2e', bg_color='#121111', border_color='#004780', border_width=3,placeholder_text_color='#a3a3a3', width=200,height=50, show="*")
    sua_senha_entry.place(x=200,y=150)
    criar_conta_btn = ctk.CTkButton(sign_up_window, text="Criar Conta", command=criar_conta, font=font2,text_color='#fff', fg_color='#00965d',hover_color='006e44', bg_color='#121111', cursor='hand2', corner_radius=5,width=120)
    criar_conta_btn.place(x=200,y=220)
    back_button = ctk.CTkButton(sign_up_window, text="Voltar", font=font2,text_color='#fff', fg_color='#00965d',hover_color='#006e44', bg_color='#121111', cursor='hand2', corner_radius=5,width=120, command=back_login)
    back_button.place(x=200,y=260)
    
    sign_up_window.mainloop()
    
# Função de login
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
    
    # Verificar se o login foi bem-sucedido
    if response == "Login Bem-Sucedido":
        dashboard(username)
    else: 
        messagebox.showerror('Erro', 'Login falhou. Tente novamente.')


# Função para exibir a dashboard
def dashboard(username):
    app.destroy()
    dashboard_window = ctk.CTk()
    dashboard_window.geometry("800x600")
    
    welcome_label = ctk.CTkLabel(dashboard_window, text=f"Bem-Vindo a Dashboard {username}", font=("Roboto", 24))
    welcome_label.pack(pady=20)
    check_var = ctk.StringVar(value="off")
    check_box = ctk.CTkCheckBox(dashboard_window,text="Gostaria de jogar um jogo?", variable=check_var, onvalue="on", offvalue="off" )
    
    check_box.pack()
    dashboard_window.mainloop()

# Função para exibir a interface de login


visual()
