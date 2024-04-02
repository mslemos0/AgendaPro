import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def Calculadora():
    app = ctk.CTk()
    app.geometry("600x300")


    def submit():
        try:
            a = float(my_entry.get())
            b = float(my_entry2.get())
            sum = a + b
            my_label.configure(text=f'O Resultado da soma é {sum}')
        except ValueError:
            my_label.configure(text=f'Digite um Número')
            
        
    notebook = ctk.CTkTabview(app)
    notebook.pack(padx=20,pady=20)

    Soma =notebook.add("Soma")
    Subtração =notebook.add("Subtração")
    Multiplicação = notebook.add("Multiplicação")
    Divisão = notebook.add("Divisão")
    
    def sub_submit():
        try:
            a = float(my_sub_entry.get())
            b = float(my_sub_entry2.get())
            
            sub = a - b
            my_sub.configure(text=f'O Resultado da Subtração é {sub}')
        except ValueError:
            my_sub.configure(text=f'Digite um Número')


    def mult_submit():
        try:
            a = float(my_mult_entry.get())
            b = float(my_mult_entry2.get())
            mult = a * b
            my_mult.configure(text=f'O Resultado da Multiplicação é {mult}')
        except ValueError:
            my_mult.configure("Digite um Número")
            
    def div_submit():
        try:
            a = float(my_div_entry.get())
            b = float(my_div_entry2.get())
            div = a / b
            my_div.configure(text=f'O Resultado da Divisão é {div}')
        except ValueError:
            my_div.configure("Digite um Número")
            

    my_label = ctk.CTkLabel (Soma,text="", font=("Roboto", 24))
    my_label.pack()
    my_entry = ctk.CTkEntry (Soma, 
                            placeholder_text="Digite um Número")
    my_entry.pack()
    my_label2 = ctk.CTkLabel (Soma, text="", font=("Roboto", 24))

    my_label2.pack()
    my_entry2 = ctk.CTkEntry(Soma, 
                            placeholder_text="Digite um Número")
    my_entry2.pack(pady=10)
    my_button_soma = ctk.CTkButton(Soma, text="Some!", command=submit)
    my_button_soma.pack(pady=10)

    my_sub = ctk.CTkLabel(Subtração, text="", font=("Roboto", 24))
    my_sub.pack()
    my_sub_entry = ctk.CTkEntry(Subtração, 
                                placeholder_text="Digite um Número")
    my_sub_entry.pack()
    my_sub_entry2 = ctk.CTkEntry(Subtração, 
                                placeholder_text="Digite um Número")
    my_sub_entry2.pack(pady=38)
    

    my_button_sub = ctk.CTkButton(Subtração, text="Subtraia!", command=sub_submit)
    my_button_sub.pack(pady=10)
    
    
    my_mult = ctk.CTkLabel(Multiplicação, text="", font=("Roboto", 24))
    my_mult.pack()
    my_mult_entry = ctk.CTkEntry(Multiplicação, 
                                 placeholder_text="Digite um Número")
    my_mult_entry.pack()
    my_mult2 = ctk.CTkLabel(Multiplicação, text="", font=("Roboto", 24))
    my_mult2.pack()
    my_mult_entry2 = ctk.CTkEntry(Multiplicação, 
                                  placeholder_text="Digite um Número")
    my_mult_entry2.pack(pady=10)
    my_mult_button = ctk.CTkButton(Multiplicação, text="Multiplique!", command= mult_submit)
    my_mult_button.pack(pady=10)
    
    
    my_div = ctk.CTkLabel(Divisão, text="", font=("Roboto", 24))
    my_div.pack()
    my_div_entry = ctk.CTkEntry(Divisão, 
                                placeholder_text="Digite um Número")
    my_div_entry.pack()
    my_div2 = ctk.CTkLabel(Divisão, text="",font=("Roboto", 24))
    my_div2.pack()
    my_div_entry2 = ctk.CTkEntry(Divisão, 
                                 placeholder_text="Digite um Número")
    my_div_entry2.pack(pady=10)
    
    my_div_button = ctk.CTkButton(Divisão, text= "Divida!", command=div_submit)
    my_div_button.pack(pady=10)
    app.mainloop()
    
Calculadora()