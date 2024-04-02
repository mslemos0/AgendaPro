import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark")

app = ctk.CTk()
app.geometry("400x200")

# Cria um notebook
notebook = ctk.CTkNotebook(app)
notebook.pack(padx=20, pady=20)

# Cria as abas
aba1 = ctk.CTkFrame(notebook)
aba2 = ctk.CTkFrame(notebook)

# Define o título de cada aba
notebook.add(aba1, text="Aba 1")
notebook.add(aba2, text="Aba 2")

# Adiciona conteúdo às abas
# ... (Aqui você pode adicionar widgets específicos a cada aba)

app.mainloop()
