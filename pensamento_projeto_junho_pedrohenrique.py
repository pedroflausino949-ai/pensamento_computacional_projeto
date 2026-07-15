from tkinter import *

# ==========================
# Janela
# ==========================

janela = Tk()
janela.title("Sistema de Agendamento - Barbearia")
janela.geometry("800x650")
janela.resizable(False, False)

# ==========================
# Variáveis
# ==========================

c1_nome = ""
c1_servico = ""
c1_horario = ""

c2_nome = ""
c2_servico = ""
c2_horario = ""

c3_nome = ""
c3_servico = ""
c3_horario = ""

# ==========================
# Funções
# ==========================

def cadastrar():

    global c1_nome, c2_nome, c3_nome

    nome = entrada_nome.get()

    if nome == "":
        resultado["text"] = "Digite o nome."
        return

    if c1_nome == "":
        c1_nome = nome
        resultado["text"] = "Cliente cadastrado na vaga 1."

    elif c2_nome == "":
        c2_nome = nome
        resultado["text"] = "Cliente cadastrado na vaga 2."

    elif c3_nome == "":
        c3_nome = nome
        resultado["text"] = "Cliente cadastrado na vaga 3."

    else:
        resultado["text"] = "Não há vagas disponíveis."


def agendar():

    global c1_servico,c1_horario
    global c2_servico,c2_horario
    global c3_servico,c3_horario

    nome = entrada_nome.get()
    servico = entrada_servico.get()
    horario = entrada_horario.get()

    if nome == c1_nome:
        c1_servico = servico
        c1_horario = horario
        resultado["text"] = "Agendamento realizado."

    elif nome == c2_nome:
        c2_servico = servico
        c2_horario = horario
        resultado["text"] = "Agendamento realizado."

    elif nome == c3_nome:
        c3_servico = servico
        c3_horario = horario
        resultado["text"] = "Agendamento realizado."

    else:
        resultado["text"] = "Cliente não encontrado."


def listar():

    texto = ""

    if c1_nome != "":
        texto += f"{c1_nome} | {c1_servico} | {c1_horario}\n"

    if c2_nome != "":
        texto += f"{c2_nome} | {c2_servico} | {c2_horario}\n"

    if c3_nome != "":
        texto += f"{c3_nome} | {c3_servico} | {c3_horario}\n"

    if texto == "":
        texto = "Nenhum agendamento."

    resultado["text"] = texto


def cancelar():

    global c1_servico,c1_horario
    global c2_servico,c2_horario
    global c3_servico,c3_horario

    nome = entrada_nome.get()

    if nome == c1_nome:
        c1_servico = ""
        c1_horario = ""
        resultado["text"] = "Agendamento cancelado."

    elif nome == c2_nome:
        c2_servico = ""
        c2_horario = ""
        resultado["text"] = "Agendamento cancelado."

    elif nome == c3_nome:
        c3_servico = ""
        c3_horario = ""
        resultado["text"] = "Agendamento cancelado."

    else:
        resultado["text"] = "Cliente não encontrado."


def alterar():

    global c1_servico,c1_horario
    global c2_servico,c2_horario
    global c3_servico,c3_horario

    nome = entrada_nome.get()
    servico = entrada_servico.get()
    horario = entrada_horario.get()

    if nome == c1_nome:
        c1_servico = servico
        c1_horario = horario
        resultado["text"] = "Agendamento alterado."

    elif nome == c2_nome:
        c2_servico = servico
        c2_horario = horario
        resultado["text"] = "Agendamento alterado."

    elif nome == c3_nome:
        c3_servico = servico
        c3_horario = horario
        resultado["text"] = "Agendamento alterado."

    else:
        resultado["text"] = "Cliente não encontrado."


def buscar():

    nome = entrada_nome.get()

    if nome == c1_nome:
        resultado["text"] = f"{c1_nome}\n{c1_servico}\n{c1_horario}"

    elif nome == c2_nome:
        resultado["text"] = f"{c2_nome}\n{c2_servico}\n{c2_horario}"

    elif nome == c3_nome:
        resultado["text"] = f"{c3_nome}\n{c3_servico}\n{c3_horario}"

    else:
        resultado["text"] = "Cliente não encontrado."


def horarios():

    resultado["text"] = """
08:00
09:00
10:00
11:00
13:00
14:00
15:00
16:00
17:00
"""


def relatorio():

    total = 0

    if c1_servico != "":
        total += 1

    if c2_servico != "":
        total += 1

    if c3_servico != "":
        total += 1

    resultado["text"] = f"Total de agendamentos: {total}"


# ==========================
# Interface
# ==========================

titulo = Label(
    janela,
    text="Sistema de Agendamento - Barbearia",
    font=("Arial",18,"bold")
)
titulo.pack(pady=15)

Label(janela,text="Nome do Cliente").pack()

entrada_nome = Entry(janela,width=40)
entrada_nome.pack()

Label(janela,text="Serviço").pack()

entrada_servico = Entry(janela,width=40)
entrada_servico.pack()

Label(janela,text="Horário").pack()

entrada_horario = Entry(janela,width=40)
entrada_horario.pack(pady=5)

Button(janela,text="1 - Cadastrar Cliente",width=25,command=cadastrar).pack(pady=3)

Button(janela,text="2 - Agendar Horário",width=25,command=agendar).pack(pady=3)

Button(janela,text="3 - Listar Agendamentos",width=25,command=listar).pack(pady=3)

Button(janela,text="4 - Cancelar Agendamento",width=25,command=cancelar).pack(pady=3)

Button(janela,text="5 - Alterar Agendamento",width=25,command=alterar).pack(pady=3)

Button(janela,text="6 - Buscar Cliente",width=25,command=buscar).pack(pady=3)

Button(janela,text="7 - Horários Disponíveis",width=25,command=horarios).pack(pady=3)

Button(janela,text="8 - Relatório do Dia",width=25,command=relatorio).pack(pady=3)

Button(janela,text="9 - Sair",width=25,command=janela.destroy).pack(pady=10)

resultado = Label(
    janela,
    text="",
    justify=LEFT,
    font=("Arial",12),
    width=60,
    height=10,
    relief="solid"
)

resultado.pack(pady=15)

janela.mainloop()