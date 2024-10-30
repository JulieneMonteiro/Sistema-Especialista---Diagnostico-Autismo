import tkinter as tk
from tkinter import messagebox, ttk

# Cores do Aplicativo
cor_fundo = "#1E1E1E"
cor_fontePrincipal = "#FFFFFF"
cor_fonteSecundaria = "#837B6F"

# Configurações da Janela Principal
janela = tk.Tk()
janela.title("Diagnóstico de Autismo")
janela.geometry("800x400")
janela.configure(bg=cor_fundo)
janela.resizable(False, False)

# Mostra o Título da janela
titulo = tk.Label(janela, text="Diagnóstico de Autismo", font=("Helvetica", 22, "bold"), bg=cor_fundo, fg=cor_fontePrincipal)
titulo.pack(pady=5, ipadx=5, ipady=5)

# Subtítulo, aviso importante.
instrucoes = tk.Label(janela, text="Esse formulário não substitui uma avaliação profissional completa.", font=("Helvetica", 13), bg=cor_fundo, fg=cor_fonteSecundaria)
instrucoes.pack(pady=7)

# Rodapé com o nome dos integrantes do grupo.
rodape = tk.Label(janela, text="Grupo Desenvolvedor: Juliene, Diego, Maria Julia, Gabriel Torres, Gabriel da Silva", font=("Helvetica", 8), bg=cor_fundo, fg=cor_fonteSecundaria)
rodape.pack(side="bottom", pady=10)

# Perguntas e opções de resposta específicas.
perguntas = [
    # Pergunta 1
    ("O paciente tem dificuldades em manter uma conversa ou iniciar interações?", 
     "Sim, o paciente evita iniciar conversas e responde de maneira muito limitadas.", 
     "Não, o paciente mantém conversas normais, sem dificuldades aparentes.", 
     "O paciente responde perguntas mas raramente iniciar uma conversa."),
    # Pergunta 2
    ("O paciente mostra falta de reciprocidade emocional?", 
     "Sim, o paciente não responde adequadamente a demonstrações de afeto e parece indiferente.", 
     "Não, o paciente responde emocionalmente como esperado.", 
     "Às vezes, o paciente responde com gestos de afeto, mas não de forma constante"),
    # Pergunta 3
    ("O paciente mantém contato visual durante as interações?", 
     "Não, o paciente evita completamente o contato visual.", 
     "Sim, o paciente mantém contato visual normal durante a conversa.", 
     "O paciente faz contato visual, mas apenas brevemente."),
    # Pergunta 4
    ("O paciente apresenta movimentos repetitivos como balançar ou agitar as mãos?", 
     "Sim, o paciente balança o corpo frequentemente", 
     "Não, o paciente não apresenta esse tipo de comportamento", 
     "O paciente tem comportamentos repetitivos ocasionais, mas não com frequência."),
    # Pergunta 5
    ("O paciente segue rotinas rígidas e reage mal a mudanças?", 
     "Sim, o paciente fica muito ansioso com qualquer alteração na rotina.", 
     "Não, o paciente lida bem com mudanças na rotina.", 
     "O paciente prefere rotinas, mas consegue lidar com pequenas mudanças."),
    # Pergunta 6
    ("O paciente tem fixação em interesses incomuns?", 
     "Sim, o paciente passa horas focado em um único tema ou objeto", 
     "Não, o paciente tem interesses diversos e variados.", 
     "O paciente mostra interesse por tópicos específicos, mas sem uma fixação incomum."),
    # Pergunta 7
    ("O paciente tem hipersensibilidade a sons, luzes ou texturas", 
     "Sim, o paciente se incomoda muito com barulhos altos e texturas de certas roupas.", 
     "Não, o paciente não mostra sinais de sensibilidade anormal a estímulos.", 
     "O paciente é sensível a estímulos sensoriais, mas consegue se adaptar na maioria das vezes."),
    # Pergunta 8
    ("O paciente evita certos tipos de alimentos devido a textura ou sabor?", 
     "Sim, o paciente só come alimentos com texturas específicas e rejeita a maioria dos outros", 
     "Não, o paciente come alimentos sem restrições relacionadas à textura ou sabor.", 
     "O paciente tem preferências alimentares, mas ainda come uma variedade razoável de alimentos."),
    # Pergunta 9
    ("O paciente cobre os ouvidos ou se afasta em ambientes barulhentos?", 
     "Sim, o paciente cobre os ouvidos sempre que há barulho ou multidão", 
     "Não, o paciente lida bem com ambientes barulhentos.", 
     "O paciente às vezes demonstra desconforto em ambientes barulhentos, mas não com frequência."),
]

respostas = []  # Lista para armazenar as respostas
indice_pergunta = 0  # Índice para rastrear a pergunta atual

# Função para exibir a próxima pergunta
def mostrar_pergunta():
    global indice_pergunta

    # Limpa os botões anteriores
    for widget in janela.winfo_children():
        if isinstance(widget, ttk.Radiobutton):
            widget.pack_forget()

    # Verificação se o Indíce é existente para ativação do formulário
    if indice_pergunta < len(perguntas):
        pergunta, texto_sim, texto_nao, texto_talvez = perguntas[indice_pergunta]
        label_pergunta.config(text=pergunta)

        # Atualização dos textos dos botões conforme a pergunta
        botaoSim.config(text=texto_sim, value=texto_sim)
        botaoNao.config(text=texto_nao, value=texto_nao)
        botaoTalvez.config(text=texto_talvez, value=texto_talvez)
        
        # Exibe os botões com textos específicos
        botaoSim.pack(pady=5)
        botaoNao.pack(pady=5)
        botaoTalvez.pack(pady=5)
        botaoConfirmar.pack(pady=20)
    else:
        # Exibe a mensagem de conclusão quando todas as perguntas foram respondidas
        label_pergunta.pack_forget()
        botaoConfirmar.pack_forget()
        mensagem_conclusao.pack()

# Função para salvar a resposta e passar para a próxima pergunta
def confirmar_resposta():
    global indice_pergunta

    # Aviso no caso da não seleção de nenhuma das respostas
    if not resposta_selecionada.get():
        messagebox.showwarning("Aviso", "Cada pergunta é obrigatória.") 
        return  # Sai da função sem avançar
    respostas.append(resposta_selecionada.get())
    indice_pergunta += 1
    mostrar_pergunta()

# Label para exibir a pergunta atual
label_pergunta = tk.Label(janela, text="", font=("Helvetica", 16), bg=cor_fundo, fg=cor_fontePrincipal)
label_pergunta.pack(pady=20)

# Variável para armazenar a resposta selecionada
resposta_selecionada = tk.StringVar()
resposta_selecionada.set("")

estilo_radiobutton = ttk.Style()
estilo_radiobutton.configure("TRadiobutton", background=cor_fundo, foreground=cor_fontePrincipal, font=("Helvetica", 12))

# Cria botões de resposta
botaoSim = ttk.Radiobutton(janela, text="", variable=resposta_selecionada, style="TRadiobutton")
botaoNao = ttk.Radiobutton(janela, text="", variable=resposta_selecionada, style="TRadiobutton")
botaoTalvez = ttk.Radiobutton(janela, text="", variable=resposta_selecionada, style="TRadiobutton")

# Cria o botão de confirmação da resposta
botaoConfirmar = ttk.Button(janela, text="Confirmar", command=confirmar_resposta)
botaoConfirmar.config(width=25) 
botaoConfirmar.pack(pady=20)

# Exibir a primeira pergunta
mostrar_pergunta()

# Mensagem de conclusão
mensagem_conclusao = tk.Label(janela, text="Teste concluído! Obrigado por responder.", font=("Helvetica", 16), bg=cor_fundo, fg=cor_fontePrincipal)

# Executando a Janela
janela.mainloop()
