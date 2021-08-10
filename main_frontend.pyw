from tkinter import *  
import backend as bk

# Objeto que recebe de backend a classe Metodos()
backend = bk.Metodos()

# Instância Janela
janela = Tk()
janela.title('Eu sei a Marca')
logo = PhotoImage(file='logo.png')
janela.wm_iconphoto(True, logo)
janela.configure(background='#2e2e2e')
janela.geometry('650x500')

""" 
    Instâncias Widgtes 
"""
grey_color = '#e3e3e3'
back_janela_color = janela.cget('background')
# Label do Titulo na Tela
lb_titulo = Label(janela, text='Descubra a marca do roteador', font=('Calibri', 25, 'bold'),
                bg=janela.cget('background'), fg=grey_color)
lb_titulo.pack(pady='10')

# Labels e Entrys da interação com usuário
lb_concentrador = Label(
    janela, background=back_janela_color, foreground=grey_color, 
    font=('Calibri', 14), text='Digite o NOME ou IP do Concentrador'
)
# Entry concentrador 
ent_concentrador = Entry(janela, background='#121212', fg=grey_color, 
font=('Calibri', 12, 'bold'), justify='center', width=36, relief=FLAT)
# Label Login
lb_login = Label(
    janela, background=back_janela_color, foreground=grey_color, 
    font=('Calibri', 14), text='Digite o LOGIN (pppoe) do cliente'
)
# Entry Login
ent_login = Entry(janela, background='#121212', fg=grey_color, selectbackground='#1d232b',
font=('Calibri', 12, 'bold'), justify='center', width=36, relief=FLAT)

# Label Saida 
lb_output = Label(
    janela, background=back_janela_color, fg='white', text='\nDesenvolvido por Eduardo Filho', 
    font=('calibri', 20, 'bold') 
    )

# Instancia botão descobrir
btn_descobre = Button(
    janela, background='#4784e6', fg='white', text='Descobrir', 
    command=lambda:backend.valida_entrada(ent_concentrador, ent_login, lb_output, frame_layout),
    font=('calibri', 12, 'bold'), width=36, relief=FLAT,
    activebackground=back_janela_color, activeforeground='#4784e6', cursor='plus'
    )

""" 
     Instâncias de Botões para Acesso Remoto
"""
# Frame vai organizar botões de acesso remoto
frame_layout = Frame(janela, bg=back_janela_color)
# label que vai dizer 'Acesso Remoto'
lb_acesso = Label(frame_layout, background=back_janela_color, fg='white', text='Acesso Remoto', font=('calibri', 16, 'bold'))
# Botão que abrirá IP do cliente na PORTA 80 Padrão
btn_acesso_80 = Button(frame_layout, background=back_janela_color, command=lambda:backend.acesso_remoto(),
fg='#4784e6', text='Porta :80', font=('calibri', 14, 'bold'), relief='flat', width=25, 
activebackground='#4784e6', activeforeground='white', cursor='plus'
)
# Botão que abrirá IP do cliente na PORTA 54321
btn_acesso_54321 = Button(frame_layout, background=back_janela_color, command=lambda:backend.acesso_remoto_porta_54321(),
fg='#4784e6', text='Porta :54321', font=('calibri', 14, 'bold'), relief='flat', width=25, 
activebackground='#4784e6', activeforeground='white', cursor='plus'
)
"""
    Ativa PACK dentro Frame LAYOUT
"""
lb_acesso.pack(pady='5')
btn_acesso_80.pack(side='left', anchor='e',pady='13', padx='5')
btn_acesso_54321.pack(side='right', anchor='w',pady='3')

"""
    Exibe na tela instâncias de Widgets no empacotador PACK
"""
lb_concentrador.pack(pady='3')
ent_concentrador.pack(pady='1')
lb_login.pack(pady='3')
ent_login.pack(pady='1')    
btn_descobre.pack(pady='20')
lb_output.pack(pady='5')

# Gera Loop em janela
janela.mainloop()